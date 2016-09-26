#!/usr/bin/env python


def parse_as_tuple(filename):
    """Parses a Berkeley weather data file as a list of tuples

    Keyword arguments:
    filename -- the name of the file to parse
    """
    data = []

    with open(filename, 'r') as f:
        # TODO: Write your parser here that returns a list of tuples (called
        # data) with each tuple consisting of:
        #   (int(year), int(month), float(anomaly), float(error))
        pass

    return data


def parse_as_lists(filename):
    """Parses a Berkeley weather data file as a number of lists

    Keyword arguments:
    filename -- the name of the file to parse
    """
    year, month, anomaly, error = [], [], [], []

    with open(filename, 'r') as f:
        # TODO: Write your parser here that returns four lists each containing
        # a column of data:
        #  * year contains the years as integers
        #  * month contains the months as integers
        #  * anomaly contains the anomalies as floats
        #  * error contains the errors as floats
        pass

    return year, month, anomaly, error


def collect_at(filenames, year, month):
    """Collects data for a specific year and month

    Keyword arguments:
    filenames -- list of all filenames to consider
    year -- the year as four digit integer e.g. 2016
    month -- the month as a three letter word e.g. 'Jan' or 'Oct'
    """
    anomaly = []

    # TODO: Write your code here

    return anomaly


def compute_annual_mean(filename):
    """Computes annual mean

    Keyword arguments:
    filename -- the name of the file
    """
    year, anomaly, error = [], [], []

    # TODO: Write your code here, be careful computing average errors

    return year, anomaly, error
