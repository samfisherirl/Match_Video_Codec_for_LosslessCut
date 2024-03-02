# Match_Video_Codec_for_LosslessCut

This script will:

- Open two file dialogues for selecting the two video files.
- Retrieve the video and audio codec, bitrate, and resolution information from video 1.
- Use ffmpeg to convert video 2 to match the properties of video 1 and save it with a new name.

To accomplish this task in Python, we can use the tkinter library for the file dialogue and ffmpeg-python, which is a wrapper around FFmpeg, a powerful multimedia framework that can handle video and audio processing.

First, make sure you have ffmpeg installed on your system and accessible via the command line, you can download it from https://ffmpeg.org/download.html. Then, install ffmpeg-python via pip if you haven't already:

```pip install ffmpeg-python```

Adjust filetypes in filedialog.askopenfilename if you want to allow for different video file extensions. Also, note that this script assumes the presence of both audio and video streams; if your source may not include an audio stream, you'll need to add additional checks and conditions.
