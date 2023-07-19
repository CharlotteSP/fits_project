"""A command line utlity to display various parameters of a FITS file
   and to browse through them."""
import argparse
import os
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from astropy.io import fits
from tabulate import tabulate


class FITSViewer:
    """Class to display a broswer for FITS files"""

    def __init__(self, fits_files):
        """Class Constructor

        Args:
            fits_files : Viewer class initated with FITS file(s)
        """
        self.fits_files = fits_files
        self.current_index = 0
        self.current_file = fits.open(self.fits_files[self.current_index])
        self.image_data = self.current_file[0].data

        # Create the figure and axis
        self.fig, self.ax = plt.subplots()
        self.image_plot = self.ax.imshow(self.image_data, cmap="gray")
        self.ax.set_title(self.fits_files[self.current_index])

        # Create buttons and connect them to the navigation functions
        self.next_button_ax = plt.axes([0.7, 0.03, 0.1, 0.04])
        self.next_button = Button(self.next_button_ax, "Next")
        self.next_button.on_clicked(self.next_image)

        self.prev_button_ax = plt.axes([0.81, 0.03, 0.1, 0.04])
        self.prev_button = Button(self.prev_button_ax, "Previous")
        self.prev_button.on_clicked(self.prev_image)

    def next_image(self, event):
        """Function to go the next image

        Args:
            event : Click event
        """
        if self.current_index < len(self.fits_files) - 1:
            self.current_index += 1
            self.current_file = fits.open(self.fits_files[self.current_index])
            self.image_data = self.current_file[0].data
            self.image_plot.set_data(self.image_data)
            self.ax.set_title(self.fits_files[self.current_index])
            plt.draw()

    def prev_image(self, event):
        """Function to go the previous image

        Args:
            event : Click event
        """
        if self.current_index > 0:
            self.current_index -= 1
            self.current_file = fits.open(self.fits_files[self.current_index])
            self.image_data = self.current_file[0].data
            self.image_plot.set_data(self.image_data)
            self.ax.set_title(self.fits_files[self.current_index])
            plt.draw()


def display_header_info(fits_files, attributes):
    """Displays header info about the FITS file.

    Args:
        fits_files : Take a single or a list of FITS files as input
        attributes : Command line attributes passed via argparse
    """
    data = []
    for fits_file in fits_files:
        try:
            with fits.open(fits_file) as hdul:
                header = hdul[0].header
                row = [fits_file]
                for attribute in attributes:
                    if attribute == "date":
                        row.append(header.get("DATE-OBS", "N/A"))
                    elif attribute == "time":
                        row.append(header.get("TIME-OBS", "N/A"))
                    elif attribute == "latitude":
                        row.append(header.get("LATITUDE", "N/A"))
                    elif attribute == "longitude":
                        row.append(header.get("LONGITUD", "N/A"))
                    elif attribute == "ra":
                        row.append(header.get("RA", "N/A"))
                    elif attribute == "dec":
                        row.append(header.get("DEC", "N/A"))
                    elif attribute == "exposure":
                        row.append(header.get("EXPTIME", "N/A"))
                    # Add more attributes as needed
                    else:
                        row.append(f"Unknown attribute: {attribute}")
                data.append(row)

        except OSError:
            print(f"Unable to open FITS file: {fits_file}")
        except Exception as e:
            print(f"An error occurred while processing {fits_file}: {str(e)}")

    if data:
        headers = ["FITS File"] + attributes
        print(tabulate(data, headers=headers, tablefmt="grid"))
        print("--------------------")


def add_argumnets_to_parser():
    parser = argparse.ArgumentParser(
        description="Display information from FITS header and view FITS images."
    )
    parser.add_argument("fits_files", nargs="+", help="Paths to the FITS files")
    parser.add_argument(
        "-d", "--date", action="store_true", help="Display date from FITS header"
    )
    parser.add_argument(
        "-t", "--time", action="store_true", help="Display time from FITS header"
    )
    parser.add_argument(
        "-l",
        "--latitude",
        action="store_true",
        help="Display latitude from FITS header",
    )
    parser.add_argument(
        "-o",
        "--longitude",
        action="store_true",
        help="Display longitude from FITS header",
    )
    parser.add_argument("--ra", action="store_true", help="Display RA from FITS header")
    parser.add_argument(
        "--dec", action="store_true", help="Display DEC from FITS header"
    )
    parser.add_argument(
        "--exposure", action="store_true", help="Display exposure time from FITS header"
    )
    parser.add_argument(
        "-v", "--viewer", action="store_true", help="Display FITS file images"
    )
    args = parser.parse_args()
    attributes = []
    if args.date:
        attributes.append("date")
    if args.time:
        attributes.append("time")
    if args.latitude:
        attributes.append("latitude")
    if args.longitude:
        attributes.append("longitude")
    if args.ra:
        attributes.append("ra")
    if args.dec:
        attributes.append("dec")
    if args.exposure:
        attributes.append("exposure")

    return parser

    attributes = []


def run_cli_script():
    parser = add_argumnets_to_parser()
    args = parser.parse_args()
    attributes = []
    if args.date:
        attributes.append("date")
    if args.time:
        attributes.append("time")
    if args.latitude:
        attributes.append("latitude")
    if args.longitude:
        attributes.append("longitude")
    if args.ra:
        attributes.append("ra")
    if args.dec:
        attributes.append("dec")
    if args.exposure:
        attributes.append("exposure")
    # Add more attributes as needed

    display_header_info(args.fits_files, attributes)

    # Show the plot when viewer is enabled
    if args.viewer:
        fits_viewer = FITSViewer(args.fits_files)
        plt.show()
