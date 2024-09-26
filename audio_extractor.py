# Simple Python Program to read a video file and extract audio from it
# Using moviepy library

import moviepy.editor

print("----- Audio Extractor Program in Python -----")

# Input video file
print("(use file extension while typing the file names)")
videoname = input("Enter name of the video file: ")
imported_video = moviepy.editor.VideoFileClip(videoname)

# Extract Audio
extracted_audio = imported_video.audio

# Save Extracted audio
audioname = input("Enter name to save audio file: ")
extracted_audio.write_audiofile(audioname)

print("Extracted audio has been saved successfully!")