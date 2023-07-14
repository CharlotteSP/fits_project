Introduction
============

A python module to extract info from FITS file. 


Motivation
----------

Once upon a time, sometime:
    * One was lazy 
    * One did not want to open a Jupyter notebook or a python file to get data from a FITS file 
    * One was already working on a program and needs to quickly check some parameters from a FITS file

So one created ``cmfits``!


Usage
-----

Call ``cmdfits`` with various flags from the command line. It is necessary to provide at least one FITS
file in the command line to operate from.

The following flags can be used:

 -h, --help       show this help message and exit
 -d, --date       Display date from FITS header
 -t, --time       Display time from FITS header
 -l, --latitude   Display latitude from FITS header
 -o, --longitude  Display longitude from FITS header
 --ra             Display RA from FITS header
 --dec            Display DEC from FITS header
 --exposure       Display exposure time from FITS header
 -v, --viewer     Display FITS file images






