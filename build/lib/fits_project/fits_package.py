import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

def open_fits(filename):
    fits_image_filename = fits.util.get_testdata_filepath(filename)
    hdul = fits.open(fits_image_filename)

    ### print a summary of the file contents
    print('\n\nINFO ABOUT FITS FILE:')
    print('---------------------')
    hdul.info()
    return

open_fits('test0.fits')