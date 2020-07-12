# This is a python script that allows for the conversion
# of a file to an audio file.

import youtube_dl

# The URL that the user gives. Will open and download the
# video from the URL, using urlopen.
link = input("Enter the URL of the youtube video you wish to convert: ")
pl = input("Is the video playlist? Enter 'yes' or 'no'.")
if_playlist = check_pl(pl)
if (if_playist):
    all_vids = True
    range_exists = input("Would you like to download only specific videos of the playlist? Enter 'yes' or 'no'.")
    if (range_exists):
        all_vids = False
        vid_range = list(map(int, input("Enter the videos you would like to download: Ex. '1 3 7 8'").split())
else:
    ts = input("Are there any timestamps in which you would like to separate the video? Enter 'yes' or 'no'. ")
    if_timestamps = check_ts(ts)
    if (if_timestamps):
        timestamps = get_timestamps()



# This function sets up the boolean value for whether or not 
# the URL given is a playlist.
def check_pl(pl):
    if pl == "yes":
        return True
    else:
        return False

# This function sets up the boolean value for whether or not 
# the user wants to use timestamps tp separate audio.
def check_ts(ts):
    if ts == "yes":
        return True
    else:
        return False

# This function will take care of asking the user for the 
# actual timestamps.
def get_timestamps():
    return list(input("""Enter the timestamps which you would like 
                            to separate the audio in the following fashion:
                                '18:11 21:32 42:57'.""").split())

