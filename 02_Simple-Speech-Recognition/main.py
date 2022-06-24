from functions import *
import sys

filename = sys.argv[1]

audio_url = upload(filename)
save_transcript(audio_url, "output")

# Run this command in terminal --> python main.py dont_speak-no_doubt.wav