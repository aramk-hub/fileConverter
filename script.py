# This is a python script that allows for the conversion
# of a file to an audio file.

import sys
import youtube_dl
import ffmpeg


# This function downloads a single YouTube video, not a
# playlist or a video with timestamps.

def download_vid(lnk):
    options = {
        'format': 'best',
        'outtmpl': '/Users/aramkazorian/Desktop/%(title)s'+'.mp4',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([lnk])


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


# The script begins here. Order is as follows:
# 1. Ask for URL
# 2. Playlist?
# 3. If playlist, want audio of all vids or a range?
# 4. If not a playlist, any timestamps?
print("Welcome to the file converter! Here, you can convert YouTube videos to "
      "wav files for audio and include "
      "timestamps as well. Please, type 'quit' at anytime if you wish to exit.")
link = input("Enter the URL of the youtube video you wish to convert: ")
check_input(link)
pl = input("Is the video a playlist? Enter 'yes' or 'no'. ")

good_input = check_input(pl)

while not good_input:
    pl = input("Invalid answer. Is the video a playlist? Enter 'yes' or 'no'. ")
    good_input = check_input(pl)

if_playlist = check_playlist(pl)
if if_playlist:
    all_vids = True
    range_exists = input("""Would you like to download only specific videos 
    of the playlist? Enter 'yes' or 'no'. """)

    range_input = check_input(range_exists)
    while not range_input:
        range_exists = input("""Invalid answer. Would you like to download 
        only specific videos of the playlist? Enter 'yes' or 'no'. """)
        range_input = check_input(range_exists)

    if range_exists:
        all_vids = False

        # Add an input check for ints
        vid_range = list(map(int, input("Enter the videos you would like to "
                                        "download: Ex. '1 3 7 8' ").split()))
else:
    ts = input("""Are there any timestamps in which you would like to 
    separate the video? Enter 'yes' or 'no'. """)

    ts_input = check_input(ts)
    while not ts_input:
        ts = input("""Invalid answer. Are there any timestamps in which you 
        would like to separate the video? Enter 'yes' or 'no'. """)
        ts_input = check_input(ts)
    if_timestamps = check_ts(ts)
    if if_timestamps:
        timestamps = get_timestamps()
    else:
        download_vid(link)
        sys.exit()
