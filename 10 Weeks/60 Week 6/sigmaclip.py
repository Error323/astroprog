#!/usr/bin/env python

import sys
import numpy as np
from matplotlib import pyplot as pl
from astropy.io import fits


def rms(data):
    """Computes the root mean squared of the data

    Keyword arguments:
    data -- a numpy array
    """
    return np.sqrt(np.mean(np.square(data[np.isfinite(data)])))


def sigma_clip(data, n, m):
    """Perform sigma-clipping on the provided data

    Keyword arguments:
    data -- a numpy array
    n -- number of standard deviations away from the median
    m -- max number of iterations
    """
    data = data[np.isfinite(data)].ravel()

    for i in range(m):
        num = data.size
        centroid = np.median(data)
        std = n * np.std(data)
        data = data[(data >= centroid - std) & (data <= centroid + std)]
        if num == data.size:
            break

    return np.min(data), np.max(data)


def rms_map(data, rows, cols, n, m):
    """Returns an rms map of the provided data

    Keyword arguments:
    data -- a numpy 2 dimensional array
    rows -- number of rows to divide image into
    cols -- number of columns to divide image into
    n -- max number of standard deviations away from centroid
    m -- max number of iterations
    """
    rmsmap = np.zeros((rows, cols))
    size = (data.shape[0]/rows, data.shape[1]/cols)
    for col in range(cols):
        for row in range(rows):
            cell = data[size[0]*row:size[0]*(row+1), size[1]*col:size[1]*(col+1)]
            cell = cell[np.isfinite(cell)]

            if cell.size == 0:
                rmsmap[row, col] = np.nan
                continue

            low, high = sigma_clip(cell, n, m)
            cell = cell[(cell > low) & (cell < high)]
            rmsmap[row, col] = rms(cell)

    return rmsmap


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: {} <image.fits>".format(sys.argv[0])
        sys.exit(1)

    print "Reading {} as fits image:".format(sys.argv[1])
    img = fits.open(sys.argv[1])

    shape = (img[0].header['NAXIS1'], img[0].header['NAXIS1'])
    print " Object: {}".format(img[0].header['OBJECT'])
    print " Date:   {}".format(img[0].header['DATE-OBS'])
    print " Size:   {}x{}".format(shape[0], shape[1])

    data = img[0].data[0,0]
    pl.imshow(data)
    pl.title('{}'.format(img[0].header['OBJECT']))
    pl.colorbar()
    pl.savefig('raw.png', format='png')
    pl.close()

    
    low, high = sigma_clip(data, 2, 10)
    print "\nrms:         {}".format(rms(data))
    print "lower bound: {}".format(low)
    print "upper bound: {}".format(high)

    cellsize = 64
    rows = shape[0]/cellsize
    cols = shape[1]/cellsize
    rmsmap = rms_map(data, rows, cols, 4, 10)
    pl.imshow(rmsmap, interpolation='nearest')
    pl.colorbar()
    pl.title('{}x{} RMS Map of `{}\''.format(rows, cols, img[0].header['OBJECT']))
    pl.savefig('rmsmap.png', format='png')
    pl.close()
    print "\nSaved image as raw.png"
    print "Saved rms map as rmsmap.png"
