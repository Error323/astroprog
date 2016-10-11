#!/usr/bin/env python

import sys
import sigmaclip as sc
import numpy as np
import matplotlib.pyplot as pl
from scipy import interpolate
from astropy.io import fits


def fit_nearest(rmsmap, rows, cols):
    nearest = np.zeros((rows, cols))
    size = (rows/rmsmap.shape[0], cols/rmsmap.shape[1])
    for i in range(cols):
        for j in range(rows):
            nearest[i, j] = rmsmap[i/size[0], j/size[1]]
    return nearest


def fit_bilinear(rmsmap, rows, cols):
    bilinear = np.zeros((rows, cols))
    return bilinear


def find_islands(data):
    islands = []

    return islands

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: {} <image.fits>".format(sys.argv[0])
        sys.exit(1)

    print "Reading {} as fits image:".format(sys.argv[1])
    img = fits.open(sys.argv[1])

    data = img[0].data[0, 0]
    shape = data.shape
    print " Object: {}".format(img[0].header['OBJECT'])
    print " Date:   {}".format(img[0].header['DATE-OBS'])
    print " Size:   {}x{}".format(shape[0], shape[1])

    # store raw image
    pl.imshow(data)
    pl.title('{}'.format(img[0].header['OBJECT']))
    pl.colorbar()
    pl.savefig('raw.png', format='png')
    pl.close()

    # store rmsmap
    rms_size = 32
    sigmas = 3
    rms_map = sc.rms_map(data, rms_size, rms_size, sigmas, 100)
    pl.imshow(rms_map, interpolation='nearest')
    pl.colorbar()
    pl.title('{}x{} RMS Map of `{}\''.format(rms_size, rms_size, img[0].header['OBJECT']))
    pl.savefig('rmsmap.png', format='png')
    pl.close()
    
    # store interpolated rmsmap using nearest neighbour
    rms_map_nearest = fit_nearest(rms_map, shape[0], shape[1])
    indices = data < rms_map_nearest*2
    nearest = data
    nearest[indices] = np.nan
    pl.imshow(nearest, interpolation='nearest')
    pl.colorbar()
    pl.title('{} above rms'.format(img[0].header['OBJECT']))
    pl.savefig('nearest.png', format='png')
    pl.close()


