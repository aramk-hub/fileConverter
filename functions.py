import sys
import os
import youtube_dl
import re


# This function downloads a single YouTube video, not a
# playlist or a video with timestamps.

def download_single_vid(lnk):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '/Users/aramkazorian/Desktop/%(title)s' + '.mp4',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([lnk])


# This function will take care of downloading an entire playlist, without
# any ranges.

def download_playlist(lnk):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '/Users/aramkazorian/Desktop/%(title)s' + '.mp4',
        'noplaylist': False,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([lnk])


# This function will download a playlist with ranges given by the user.
# I.e. if given the range [1, 3, 5, 7], this function will only download
# the 1st, 3rd, 5th, and 7th video of the playlist.

def download_with_range(lnk, range_str):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '/Users/aramkazorian/Desktop/%(title)s' + '.mp4',
        'playlist_items': range_str,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([lnk])


# This function takes in a link and a list of timestamps, formatted as strings.
# The function will download the video in separate audio files specified by the
# by the user. The way to accomplish this is by using the ffmpeg module to
# our advantage and pass in the arguments as if it was a ffmpeg command, through
# the system.

def download_with_timestamps(lnk, time_lst):
    timestamps = calc_timestamps(time_lst)


# This function will calculate the amount of seconds, so that ffmpeg
# can be used with the timestamps.
def calc_timestamps(times):
    result = []
    i = 0
    for time in times:
        hours = int(time[:2]) * 3600
        minutes = int(time[3:5]) * 60
        seconds = int(time[6:])
        result[i] = hours + minutes + seconds
        i += 1
    return result


# This function checks the format of the timestamps.
def check_timestamps(lst):
    pattern = ""


# Check if the URL is a valid YouTube URL.

def valid_url(URL):
    pattern = "(https:\\/\\/)?(www\\.)?youtube\\.com\\/watch\\?v=[" \
              "a-zA-Z0-9_\\-]{11}(([#\\&\\?]?)(?:t=|start=)(\\d+)s)? "
    return bool(re.match(pattern, URL))


# This function will ask for the URL again, if invalid. This is for individual
# videos.

def reenter_url():
    url = input(
        "Invalid URL. Please make sure the URL given is a valid YouTube URL.")
    check_input(url)
    while not valid_url(url):
        url = input(
            "Invalid URL. Please make sure the URL given is a valid YouTube URL.")
        check_input(url)
    return url


# This function sets up the boolean value for whether or not
# the URL given is a playlist.

def check_playlist(pllst):
    if pllst == "yes":
        return True
    else:
        return False


# This function will take care of using a while loop to keep asking the user
# for a valid answer to the question asked, if the answer is invalid.
# This function will only take care of invalid answers for 'yes' or 'no'
# questions.

def check_invalids(inpt, prompt):
    while not inpt:
        answer = input(prompt)
        inpt = check_input(inpt)
    return answer


# This function sets up the boolean value for whether or not
# the user wants to use timestamps tp separate audio.

def check_ts(timestamp):
    if timestamp == "yes":
        return True
    else:
        return False


# This function will take care of asking the user for the
# actual timestamps.

def get_timestamps():
    return list(input("Enter the timestamps which you would like to separate "
                      "the audio in the following fashion: "
                      "'00:18:11 01:21:32 01:42:57'. "
                      "This is in HH:mm:ss format.").split())


# This function checks if 'yes' or 'no' inputs are valid.
# Essentially, checks for spelling errors and other invalid answers.
# If input is 'quit', the program is exited immediately.

def check_input(inpt):
    if inpt == "quit":
        sys.exit()
    if inpt != "yes":
        if inpt != "no":
            return False
    return True
