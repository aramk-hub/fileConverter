# This is a python script that allows for the conversion
# of a file to an audio file. I read and used the documentation
# of youtube-dl to help download videos using the processing options
# given by the user.
import sys
import functions


# The script begins here. Order is as follows:
# 1. Ask for URL
# 2. Playlist?
# 3. If playlist, want audio of all vids or a range?
# 4. If not a playlist, any timestamps?
print("Welcome to the file converter! Here, you can convert YouTube videos to "
      "wav files for audio and include "
      "timestamps as well. Please, type 'quit' at anytime if you wish to exit.")
link = input("Enter the URL of the youtube video you wish to convert: ")
functions.check_input(link)

pl = input("Is the video a playlist? Enter 'yes' or 'no'. ")

good_input = functions.check_input(pl)

while not good_input:
    pl = input("Invalid answer. Is the video a playlist? Enter 'yes' or 'no'. ")
    good_input = functions.check_input(pl)

if_playlist = functions.check_playlist(pl)

if if_playlist:
    all_vids = True
    range_exists = input("""Would you like to download only specific videos
    of the playlist? Enter 'yes' or 'no'. """)

    range_input = functions.check_input(range_exists)
    while not range_input:
        range_exists = input("""Invalid answer. Would you like to download
        only specific videos of the playlist? Enter 'yes' or 'no'. """)
        range_input = functions.check_input(range_exists)

    if range_exists == 'yes':
        all_vids = False

        # Add an input check for ints
        vid_range = input("Enter the videos you would like to "
                                        "download, or enter '0' if you want "
                                        "all: Ex. '1 3 7-9'. ")
        functions.download_with_range(link, vid_range)

    else:
        functions.download_playlist(link)
else:
    matches = functions.valid_url(link)
    if not matches:
        link = functions.reenter_url()
    ts = input("""Are there any timestamps in which you would like to
    separate the video? Enter 'yes' or 'no'. """)

    ts_input = functions.check_input(ts)
    while not ts_input:
        ts = input("""Invalid answer. Are there any timestamps in which you
        would like to separate the video? Enter 'yes' or 'no'. """)
        ts_input = functions.check_input(ts)
    if_timestamps = functions.check_ts(ts)
    if if_timestamps:
        timestamps = functions.get_timestamps()
        functions.download_with_timestamps(link, timestamps)
        sys.exit()
    else:
        functions.download_single_vid(link)
        sys.exit()
