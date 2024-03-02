import ffmpeg
import tkinter as tk
from tkinter import filedialog

# Function to get the stream information of a video
def get_video_info(video_path):
    try:
        probe = ffmpeg.probe(video_path)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        audio_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'audio'), None)
        return video_stream, audio_stream
    except ffmpeg.Error as e:
        print(e.stderr)
        raise e

# Function to convert video 2 to match video 1's properties
def convert_video(match_video_info, input_video_path, output_video_path):
    video_stream, audio_stream = match_video_info

    ffmpeg.input(input_video_path).output(
        output_video_path,
        vcodec=video_stream['codec_name'],
        acodec=audio_stream['codec_name'],
        video_bitrate=video_stream['bit_rate'],
        audio_bitrate=audio_stream['bit_rate'],
        vf='scale=' + str(video_stream['width']) + ':' + str(video_stream['height'])
    ).run(overwrite_output=True)

# Function to open file dialogue to select files
def open_file_dialog(title):
    root = tk.Tk()
    root.withdraw()  # Close the root window
    file_path = filedialog.askopenfilename(title=title, filetypes=[("Video files", "*.mp4 *.avi *.mkv")])
    root.destroy()
    return file_path

# Main script starts here
if __name__ == "__main__":
    # Open file dialogues to select the two videos
    video1_path = open_file_dialog('Select the first video (to match properties)')
    video2_path = open_file_dialog('Select the second video (to convert)')

    if video1_path and video2_path:
        # Get video and audio information from video 1
        video1_info = get_video_info(video1_path)

        # Set output path (you can modify this to your liking)
        output_video_path = video2_path.rsplit(".", 1)[0] + "_converted.mp4"

        # Convert video 2 to match video 1's properties
        convert_video(video1_info, video2_path, output_video_path)

        print(f"Conversion completed. The converted video is saved as '{output_video_path}'.")
    else:
        print("Video files were not selected correctly.")
