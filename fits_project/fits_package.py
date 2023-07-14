import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits



def open_fits(filename, print_info=True):
    """
    Function to open fits file
    
    Parameters: 
    filename (str): name of .fits filename 
    print (bool): True (default) - prints a summary of the file contents and .fits header
                  False - doesn't print file contents

    Returns:
    header :
    data (ndarray): Array of the data from the .fits file

    """
    fits_image_filename = fits.util.get_testdata_filepath(filename)
    hdul = fits.open(fits_image_filename)
    
    if print_info==True:
        ### print a summary of the file contents
        print('\n\nINFO ABOUT FITS FILE:')
        print('---------------------')
        hdul.info()

        ### print the contents of the .fits header
        print('\n\nFITS HEADER:')
        print('------------')
        print(repr(hdul[0].header))
    
    header = hdul[0].header
    ### visualization
    data = hdul[1].data
    
    # close the file
    hdul.close()

    return header, data

def visualize(data):
    """
    Parameters:
    data (ndarray): Array of the data from the .fits file

    Outputs:
    A plot visualizing the data from the .fits file
    """
    plt.imshow(data)
    plt.show()

    return

test_header, test_data = open_fits('test0.fits')
visualize(test_data)