#!/usr/bin/env python

import sys
import sigmaclip as sc
import numpy as np
import matplotlib.pyplot as pl
from scipy import interpolate
from astropy.io import fits


def fit_nearest(rmsmap, rows, cols):
    """Returns a nearest neighbour interpolation of the rmsmap that is rows x cols

    Keyword arguments:
    rmsmap -- the 2d rmsmap
    rows -- result rows
    cols -- result columns
    """

    nearest = np.zeros((rows, cols))
    return nearest


def fit_bilinear(rmsmap, rows, cols):
    """Returns a bilinear interpolation of the rmsmap that is rows x cols

    Keyword arguments:
    rmsmap -- the 2d rmsmap
    rows -- result rows
    cols -- result columns
    """

    bilinear = np.zeros((rows, cols))
    return bilinear


def find_islands(data):
    """Returns a list of tuples containing island center positions

    Keyword arguments:
    data -- the 2d data
    """
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
    rms_map_bilinear = fit_bilinear(rms_map, shape[0], shape[1])
    indices = data < rms_map_bilinear*5
    bilinear = data
    bilinear[indices] = np.nan
    pl.imshow(bilinear, interpolation='nearest')
    pl.colorbar()
    pl.title('{} above rms'.format(img[0].header['OBJECT']))
    pl.savefig('bilinear.png', format='png')
    pl.close()


