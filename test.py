#!/usr/bin/env python
from __future__ import unicode_literals, print_function
import ffmpeg
import sys
import praw

def submissionHandling(submission):
	url = submission.url

	if (url.endswith('mp4') or url.endswith('.webm')):
		print('Direct Link Provided')
	elif "imgur" in url:
	  url = (url.rstrip("gifv") + "mp4")
	else:
		print('Not a gif')
		return

	try:
		probe = ffmpeg.probe(url)
	except ffmpeg.Error as e:
		print(e.stderr, file=sys.stderr)
		sys.exit(1)

	video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
	if video_stream is None:
		print('No video stream found', file=sys.stderr)
		sys.exit(1)

	if ("mp4" in url):
		flair = (video_stream['duration']).strip('0')         # FOR MP4
	elif ('webm' in url):
		flair = (video_stream['tags']['DURATION']).strip('0:') # FOR WEBM

	flair = (str(round(float(flair),2)) + ' seconds')
	print(flair)
	submission.mod.flair(flair)
	return
