import sys
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


# Check if the URL is a valid YouTube URL.

def valid_url(URL):
    pattern = "(https:\\/\\/)?(www\\.)?youtube\\.com\\/watch\\?v=[a-zA-Z0-9_\\-]{11}(([#\\&\\?]?)(?:t=|start=)(\\d+)s)?"
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
    return list(input("""Enter the timestamps which you would like 
                            to separate the audio in the following fashion:
                                '18:11 21:32 42:57'.""").split())


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
