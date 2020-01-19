from __future__ import unicode_literals
import youtube_dl
ydl_opts = {'format':' (bestvideo[width>=?1920]/bestvideo)+bestaudio/best'}
url = input("Enter your URL:")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	ydl.download([url])
print("Downloaded!")
