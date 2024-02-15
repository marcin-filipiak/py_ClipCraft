## Description:

This Python program, named "ClipCraft," is designed to download YouTube videos and extract a specified segment from them. The script utilizes the pytube library to fetch the video from YouTube and moviepy for cutting and editing purposes.

## How it works:

Input Parameters:

* url: YouTube video URL.
* output_file: Desired name for the output video file.
* --start_time: Beginning time of the video segment to be extracted (optional).
* --end_time: End time of the video segment to be extracted (optional).

Downloading:

The program downloads the YouTube video using the provided URL, with an optional opening of the video in a web browser.
It selects a progressive stream with a file extension of 'mp4' and a resolution of '720p' for download.

Segment Extraction:

If --start_time and --end_time are provided, the program uses ffmpeg to extract the specified segment from the downloaded video.
The resulting video segment is saved with the given output_file name.

Clean-up:
        Temporary files are removed after processing.

## How to Run:

Open a terminal.
Run the script using the following command:

`python3 script_name.py url output_file [--start_time HH:MM:SS] [--end_time HH:MM:SS]`

Replace script_name.py with the actual script name, url with the YouTube video URL, output_file with the desired output file name, and optional --start_time and --end_time for specifying the segment.

Note: Ensure that you have the necessary dependencies (pytube and moviepy) installed before running the script.
