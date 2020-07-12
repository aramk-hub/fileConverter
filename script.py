# This is a python script that allows for the conversion
# of a file to an audio file.

import youtube_dl

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

# This function checks if 'yes' or 'no' inputs are valid.
# Essentially, checks for spelling errors and other invalid answers.

def check_input(inpt):
    if inpt != "yes":
        if inpt != "no":
            return False
    return True


# The script begins here. Order is as follows:
# 1. Ask for URL
# 2. Playlist?
# 3. If playlist, want audio of all vids or a range?
# 4. If not a playlist, any timestamps?

link = input("Enter the URL of the youtube video you wish to convert: ")
pl = input("Is the video a playlist? Enter 'yes' or 'no'.")

pl_input = check_input(pl)
while not good_input:
    pl = input("Invalid answer.Is the video a playlist? Please enter 'yes' or 'no'.")
    good_input = check_input(pl)

if_playlist = check_pl(pl)
if (if_playist):
    all_vids = True
    range_exists = input("""Would you like to download only specific videos of the playlist? 
                                Enter 'yes' or 'no'.""")

    range_input = check_input(range_exists)
    while not range_input:
        range_exists = input("""Invalid answer. Would you like to download only specific videos of the playlist? 
                                Enter 'yes' or 'no'.""")
        range_input = check_input(pl)

    if (range_exists):
        all_vids = False
        
        
        # Add an input check for ints
        vid_range = list(map(int, input("Enter the videos you would like to download: Ex. '1 3 7 8'").split()))
else:
    ts = input("""Invalid answer. Are there any timestamps in which you would like to separate the video? 
                    Enter 'yes' or 'no'.""")

    ts_input = check_input(ts)
    while not ts_input:
        ts = input("""Invalid answer. Are there any timestamps in which you would like to separate the video? 
                    Enter 'yes' or 'no'.""")
        ts_input = check_input(ts)
    if_timestamps = check_ts(ts)
    if (if_timestamps):
        timestamps = get_timestamps()
