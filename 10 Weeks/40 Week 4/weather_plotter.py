#!/usr/bin/env python

import argparse
import weather_parser as wp
from matplotlib import pyplot as pl


def line_plot(x, y, e):
    """Plots y data, its error and saves it as png

    Keyword arguments:
    x -- list containing the x axis
    y -- list containing the data
    e -- list containing the error on the data
    """

    # TODO: Plot the data here

    pl.savefig('lineplot.png', format='png')
    pl.close()


def scatter_plot(x, y):
    """Plots x and y and saves it as png

    Keyword arguments:
    x -- list containing x axis data
    y -- list containing y axis data
    """
    assert(len(x) == len(y))

    # TODO: Plot the data here

    pl.savefig('scatterplot.png', format='png')
    pl.close()


def histogram_plot(data, bins):
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
    parser.add_argument('files', metavar='FILE', type=argparse.FileType('r'),
                        nargs='+', help="Files containing Berekley temperature \
                        data, supports glob patterns")
    return parser.parse_args()


if __name__ == "__main__":
    cfg = get_configuration()

    filenames = []
    for f in cfg.files:
        filenames.append(f.name)
        f.close()
    filenames.sort()

    # line plot
    year, anomaly, error = wp.compute_annual_mean(filenames[0])
    line_plot(year, anomaly, error)

    # scatter plot
    year, _, _, error = wp.parse_as_lists(filenames[0])
    scatter_plot(year, error)

    # histogram plot
    anomaly = wp.collect_at(filenames, 2000, 'Jan')
    histogram_plot(anomaly, 50)
