from __future__ import unicode_literals
import youtube_dl
ydl_opts = {
'outtmpl': '/Folder Name/%(title)s'+'.mp4',
'format':' (bestvideo[width>=?1080]/bestvideo)+bestaudio/best',
'allsubtitles': True,
    'writesubtitles': True,
    'convertsubtitles':True,
   
    'subtitleslangs':'en',
    'postprocessors': [{
        'key': 'FFmpegSubtitlesConvertor',
        'format': 'srt',
    }],
}
url = input("Enter your URL: ")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	ydl.download([url])
print("Downloaded!")
