import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits



def open_fits(filename):
    """
    Function to open fits file
    
    Parameters: 
    filename (str): name of .fits filename 

    Outputs:
    Prints .fits file info
    """
    fits_image_filename = fits.util.get_testdata_filepath(filename)
    hdul = fits.open(fits_image_filename)

    ### print a summary of the file contents
    print('\n\nINFO ABOUT FITS FILE:')
    print('---------------------')
    hdul.info()
    return

open_fits('test0.fits')