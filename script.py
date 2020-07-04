# This is a python script that allows for the conversion
# of a file to an audio file.

import urllib
from urllib.request import urlopen

# The URL that the user gives. Will open and download the
# video from the URL, using urlopen.
link = input("Enter the URL of the video you wish to convert: ")
times_exist = False
if_timestamps = input("Are there any timestamps in which you would like to separate the video? Enter 'yes' or 'no'. ")
if (if_timestamps == "yes"):
    times_exist = True
    times = list(input("Enter timestamps in the following fashion, '18:11 21:22 24:54'.").split()
