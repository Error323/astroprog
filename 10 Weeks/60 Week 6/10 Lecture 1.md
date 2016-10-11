## Sourcefinder (2/3)
Using our sigmaclipping and RMS map functions we will continue our work on
creating a source finder. This week we will use our sigmaclipped rmsmap to find
islands in our image that define our sources. We will implement three
functions.

  1. Implement the function `fit_nearest(rmsmap, cols, rows)` that given the
     `rmsmap` returns an interpolated map using nearest neighbour interpolation
     (see wikipedia/lecture) with `cols x rows` resolution.

  2. Implement the function `fit_bilinear(rmsmap, cols, rows)` that given the
     `rmsmap` returns an interpolated map using bilinear interpolation (see
     wikipedia/lecture) with `cols x rows` resolution.

  3. After filtering out the noise using our interpolated rmsmap, we will look
     for islands in the remaining data. Implement the function
     `find_islands(data)` that returns a list of positions. Each position is a
     tuple $$(x, y)$$ containing the center position of that island. 

Please download [rmsfit.py](rmsfit.py) and [sigmaclip.py](sigmaclip.py) and
implement the functions in `rmsfit.py`. Have fun!
