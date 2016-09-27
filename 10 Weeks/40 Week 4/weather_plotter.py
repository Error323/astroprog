#!/usr/bin/env python

import argparse
import weather_parser as wp
import glob
from matplotlib import pyplot as pl


def plot_line(x, y, e):
    """Plots y data, its error and saves it as png

    Keyword arguments:
    x -- list containing the x axis
    y -- list containing the data
    e -- list containing the error on the data
    """

    # TODO: Plot the data here

    pl.savefig('lineplot.png', format='png')
    pl.close()


def plot_scatter(x, y):
    """Plots x and y and saves it as png

    Keyword arguments:
    x -- list containing x axis data
    y -- list containing y axis data
    """
    assert(len(x) == len(y))

    # TODO: Plot the data here

    pl.savefig('scatterplot.png', format='png')
    pl.close()


def plot_histogram(data, bins):
    """Plots a histogram of data using a certain number of bins

    Keyword arguments:
    data -- list of numbers containing the data
    bins -- number of bins to use for the histogram
    """

    # TODO: Plot the data here

    pl.savefig('histogram.png', format='png')
    pl.close()


def get_configuration():
    """Returns a populated cli configuration"""
    parser = argparse.ArgumentParser()
    parser.add_argument('files', metavar='FILE', type=str,
                        nargs='+', help="Files containing Berekley temperature \
                        data, supports glob patterns")
    return parser.parse_args()


if __name__ == "__main__":
    cfg = get_configuration()
    
    filenames = []
    for pattern in cfg.files:
        filenames += glob.glob(pattern)

    print "Using {} files".format(len(filenames))

    # line plot
    year, anomaly, error = wp.compute_annual_mean(filenames[0])
    plot_line(year, anomaly, error)
    print "Created line plot"

    # scatter plot
    year, _, _, error = wp.parse_as_lists(filenames[0])
    plot_scatter(year, error)
    print "Created scatter plot"

    # histogram plot
    anomaly = wp.collect_at(filenames, 2000, 'Jan')
    plot_histogram(anomaly, 50)
    print "Created histogram plot"
