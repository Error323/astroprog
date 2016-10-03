## Using Arrays with Numpy
The subject of the fifth week are arrays. Python itself does not include 
arrays you will need Numpy for that. Numpy arrays are used throughout 
scientific software that is written in Python. Please read the 
following documentation available on the web:

* [What is Numpy?](http://docs.scipy.org/doc/numpy/user/whatisnumpy.html)
* [Numpy data types](http://docs.scipy.org/doc/numpy/user/basics.types.html)
* [Array creation](http://docs.scipy.org/doc/numpy/user/basics.creation.html)
* [Array indexing](http://docs.scipy.org/doc/numpy/user/basics.indexing.html)

For this week's assignment you will be writing a sigmaclipping algorithm and
creating an rms map of an actual fits image from the AARTFAAC project, first
examine sigmaclip.py from the [tarball](data.tar.gz). The assignment is divided
into three parts.

 1. Write a function `rms(data)` that computes the root-mean squared around the
    median of the data which is a numpy array. Make sure that the function is
    robust against NaNs and Infs.

 2. Write an iterative sigma clipping function `sigmaclip(data, n, m)`.  This
    function will iterate over the data, each time rejecting data points which
    lie `n` standard deviations away from the centroid. We define the centroid
    as the median, but it could also be the mean.  The function should then
    return a lower- and upperbound such that after at most `m` iterations these
    bounds are the min and max value of the remaining data. That is, the
    algorithm can stop iterating if the number of remaining data points between
    iteration $$i$$ and $$i+1$$ is equal or $$i+1 = m$$. Make sure that the
    function is robust against NaNs and Infs.

 3. Write a function `rmsmap(data, rows, cols, n, m)` that takes a 2D numpy
    array as data and performs the following steps:
    
    1. Split up the data into `rows x cols` cells.
    2. For each cell sigma clip `n` standard deviations.
    3. For each sigma clipped cell compute the rms.
    4. Stores and returns a 2d array of size `rows x cols` containing the rms value per cell.
