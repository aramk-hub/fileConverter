# This is a python script that allows for the conversion
# of a file to an audio file.

import youtube_dl
import os.path
import subprocess
import ssl
import urllib.request

# The URL that the user gives. Will open and download the
# video from the URL, using urlopen.
link = input("Enter the URL of the video you wish to convert: ")
times_exist = False
if_timestamps = input("Are there any timestamps in which you would like to separate the video? Enter 'yes' or 'no'. ")
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# if (if_timestamps == "yes"):
#     times_exist = True
#     times = list(input("Enter timestamps in the following fashion, '18:11 21:22 24:54'.").split()

def download_vid(URL):
    vid_file = 'temp_file.mp4'
    video = urllib.request.urlopen(URL, context=ctx)
    with open(vid_file, 'wb') as f:
        f.write(video.read())
    return vid_file

def convert_to_audio(video):
    root, ext = os.path.splitext(video)
    os.rename(video, root + '.wav')


vid = download_vid(link)
#convert_to_audio(vid)


