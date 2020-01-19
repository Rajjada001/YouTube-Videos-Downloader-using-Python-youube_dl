from __future__ import unicode_literals
import youtube_dl
url = input("Enter your URL:")

ydl = youtube_dl.YoutubeDL({
    'outtmpl': '/tmp/testvideo.mp4',
    'format':' bestvideo+bestaudio'
})

ydl.download([url])
print("Downloaded!")