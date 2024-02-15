from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import argparse
import os


def timetosec(cz):
    try:
        h, m, s = map(int, cz.split(':'))
        il_s = h * 3600 + m * 60 + s
        return il_s
    except ValueError:
        print("ERROR! Time format (HH:MM:SS).")



def download_data(url, output_file, start_time=None, end_time=None):

	print('Wait, I am downloading...')

	yt = YouTube(url)
	webbrowser.open(url)
	video_stream = yt.streams.filter(progressive=True).filter(file_extension='mp4').filter(res='720p').first()
	video_stream.download(filename='t_'+output_file)
	print('Video downloaded.')

	if (start_time != None):
		ffmpeg_extract_subclip("t_"+output_file, start_time, end_time, targetname=output_file)
		print('Selected part of video is ready')
		os.remove('t_'+output_file)
	else:
		os.rename('t_'+output_file, output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='I am downloading selected part of video from youtube')
    parser.add_argument('url', type=str, help='url to video on youtube')
    parser.add_argument('output_file', type=str, help='output file')
    parser.add_argument('--start_time', type=str, help='begining time of video (HH:MM:SS)')
    parser.add_argument('--end_time', type=str, help='end time of video (HH:MM:SS)')

    args = parser.parse_args()

    start_time = args.start_time if args.start_time else None
    end_time = args.end_time if args.end_time else None

    download_data(args.url, args.output_file, timetosec(start_time), timetosec(end_time))
