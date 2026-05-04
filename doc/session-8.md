Good morning/afternoon/evening.

This session introduced multidimensional data, including examples of what it looks like and how it can be stored. We then used the NiBabel library to work with a medical dataset (fMRI). First, we examined the size and structure of the data, and then we visualized some of the images it contains.
We also briefly discussed how lower-resolution data can be transformed into higher-resolution data, and how affine transformations are used to correctly map and position the images in space.

In the second half, we imported the seaborn library for plotting orbital launch system data. Thereafter, we familiarized ourselves with the analysis of fMRI data, plotting the time series of 3 different voxels. As the last index (time not defined) was kept constant, we were staying in the same axial slice. 

We then constructed the input signal with the length of nt (record data every 2s, 10s on, followed by 10s off). The next step was normalizing the time series data for all 3 points (locations).