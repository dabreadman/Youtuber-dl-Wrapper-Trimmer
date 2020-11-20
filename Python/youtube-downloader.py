from __future__ import unicode_literals
import youtube_dl, os, time

strTime = input("Start time : ")
endTime = input("End time : ")
url = input("URL : ")

def formatTime (time):
    someList = []
    for i, c in enumerate(time):
        someList.append(c)
        if i%2 == 1:
            someList.append(':')
    return ''.join(someList)[:-1]

ydl_opts = {
    'format': 'bestaudio/best',
 #   specifies output directory
    'outtmpl': '/Clip/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# optional parameters
if url == "":
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
if strTime == "" and endTime != "":
    ydl_opts["postprocessor_args"] = ['-to', formatTime(endTime)]
elif strTime != "" and endTime == "":
    ydl_opts["postprocessor_args"] = ['-ss',formatTime(strTime)]
elif strTime != "" and endTime != "":
    ydl_opts["postprocessor_args"] = ['-ss',formatTime(strTime),'-to', formatTime(endTime)]

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

# rickroll
if url == "https://www.youtube.com/watch?v=dQw4w9WgXcQ":
    os.startfile('.\Clip\\Rick Astley - Never Gonna Give You Up (Video).mp3')
    time.sleep(211)

