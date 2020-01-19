from __future__ import unicode_literals
import youtube_dl
ydl_opts = {'format':' best[height<=?1080]'}
url = input("Enter your URL:")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	ydl.download([url])
print("Downloaded!")
