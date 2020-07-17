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
    os.system("ffmpeg -ss 0 -i $(youtube-dl -f 140 -g " + lnk + ") -t " +
              str(time_lst[0]) + " -c copy /Users/aramkazorian/Desktop/out.m4a")
    for i in range(len(time_lst) - 1):
        if i == len(time_lst) - 1:
            break
        t = time_lst[i+1] - time_lst[i]
        os.system("ffmpeg -ss " + str(time_lst[i]) +
                  " -i $(youtube-dl -f 140 -g " + lnk + ") -t " + str(t)
                  +
                  " -c copy /Users/aramkazorian/Desktop/out" + str(i+1) + ".m4a")
    os.system("ffmpeg -ss " + str(time_lst[len(time_lst) - 1])
              +
              " -i $(youtube-dl -f 140 -g " + lnk
              +
              ") -c copy /Users/aramkazorian/Desktop/out"
              +
              str(i+2) + ".m4a")


# This function will calculate the amount of seconds, so that ffmpeg
# can be used with the timestamps.
def calc_timestamps(times):
    result = []
    for time in times:
        hours = int(time[:2]) * 3600
        minutes = int(time[3:5]) * 60
        seconds = int(time[6:])
        result.append(hours + minutes + seconds)
    return result


# This function checks the format of the timestamps.
# Also checks the validity of the order they were placed.
# For example, timestamps cannot be entered as '00:18:11 00:09:11' as
# we cannot decide whether or not you want it vice versa or if there was
# a mistake in what you inputted.

def check_timestamps(lst):
    pattern = "[0-1][0-9]:[0-5][0-9]:[0-5][0-9]"
    valid = True
    for ele in lst:
        if not bool(re.match(pattern, ele)):
            valid = False
    calc = calc_timestamps(lst)
    if valid:
        valid = all(calc[i] < calc[i + 1] for i in range(len(calc) - 1))
    return valid, calc


# This function will ask for valid timestamps until they are given.

def need_valid_times():
    times = list(
        input("Invalid timestamp format. Please enter again, following "
              "the above format. ").split())
    check_input(times)
    valid_times, calc_times = check_timestamps(times)
    while not valid_times:
        times = list(
            input("Invalid timestamp format. Please enter again, following "
                  "the above format. ").split())
        check_input(times)
        valid_times, calc_times = check_timestamps(times)
    return calc_times


# Check if the URL is a valid YouTube URL.

def valid_url(url):
    pattern = "(https:\\/\\/)?(www\\.)?youtube\\.com\\/watch\\?v=[" \
              "a-zA-Z0-9_\\-]{11}(([#\\&\\?]?)(?:t=|start=)(\\d+)s)?"
    return bool(re.match(pattern, url))


# This function will ask for the URL again, if invalid. This is for individual
# videos.

def reenter_url():
    url = input(
        "Invalid URL. Please make sure the URL given is a valid YouTube URL. ")
    check_input(url)
    while not valid_url(url):
        url = input(
            "Invalid URL. Please make sure the URL given is a valid YouTube "
            "URL. ")
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
    lst = list(input("Enter the timestamps which you would like to separate "
                     "the audio in the following fashion: "
                     "'00:18:11 01:21:32 01:42:57'. "
                     "This is in HH:mm:ss format and must be in increasing "
                     "order. ").split())
    valid, calculated = check_timestamps(lst)
    if not valid:
        return need_valid_times()
    else:
        return calculated


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
