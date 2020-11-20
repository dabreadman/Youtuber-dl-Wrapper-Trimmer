# Youtuber-dl-Wrapper-Trimmer
Wrappers for Youtube-dl (and FFmpeg) to download audio and trim clips at specified timestamp

# Use
1. Download [Youtube.Trimmer.rar](https://github.com/dabreadman/Youtuber-dl-Wrapper-Trimmer/releases/tag/0.0.1)[](https://github.com/dabreadman/Youtuber-dl-Wrapper-Trimmer/releases/tag/0.0.1)
2. Create a shortcut to  `youtube-downloader.exe`
3.  Run  `youtube-downloader.exe`  or the shortcut
4.  `Start Time`  &  `End Time`  in format of  `HHMMSS`, eg.  `013430`  for  `1 Hour 34 Minutes 30 Seconds`.
5.  Trimmed clip will be placed in  `\Clip\`

## Demonstration
Starts at `1 Minute 30 Seconds` and ends at `2 Minutes 45 Seconds` for this [URL](https://www.youtube.com/watch?v=ZjDZrReZ4EI)

![alt text](https://github.com/dabreadman/Youtuber-dl-Wrapper-Trimmer/blob/main/Python/demo.jpg)
If no `Start Time` was entered, will start from `00:00:00`, if no `End Time` was entered, will end at the end.
The program will exit after finishing operation.

# Development

## Python
 [youtube-downloader.py](https://github.com/dabreadman/Youtuber-dl-Wrapper-Trimmer/blob/main/Python/youtube-downloader.py)
 
To modify output directory, modify `/Clip/` in 
`'outtmpl': '/Clip/%(title)s.%(ext)s'`
Stores trimmed audio files into `/Clip` of current directory by default.


### Py2exe
1. Download both [setup.py](https://github.com/dabreadman/Youtuber-dl-Wrapper-Trimmer/blob/main/Python/setup.py) and [youtube-downloader.py](https://github.com/dabreadman/Youtuber-dl-Wrapper-Trimmer/blob/main/Python/youtube-downloader.py).
2. Download [Py2exe](https://www.py2exe.org/index.cgi/FrontPage)
3. Run `python setup.py py2exe`
4. Rename `Dist` to any of your liking and create a shortcut to `youtube-downloader.exe` to use it any where.

### PyInstaller (Not Recommended, Slow Start Time)
1. Download [youtube-downloader.py](https://github.com/dabreadman/Youtuber-dl-Wrapper-Trimmer/blob/main/Python/youtube-downloader.py).
2. Enter the directory and  do `pyinstaller --onefile youtube-downloader.py`
3. The distribution is in `~\dist\youtube-downloader`
4.  Create a shortcut to `youtube-downloader.exe` to use it any where.
Read more on [PyInstaller](https://www.pyinstaller.org/)


## Powershell

 1. Download [yt.ps1](https://github.com/dabreadman/Youtuber-dl-Wrapper-Trimmer/blob/main/Powershell/yt.ps1)
 2. Edit **yt.ps1** with any text editor 
	  Recommends [Notepad++](https://notepad-plus-plus.org/downloads/) or [Visual Studio Code](https://code.visualstudio.com/download)
3. Change `D:\Youtube-DLG\youtube-dl.exe` to the directory where your [youtube-dl.exe](https://youtube-dl.org/) is installed.
4. Change `D:\Music\%(title)s.%(ext)s` to the directory where you want the final .mp3 audio file is placed.
     Alternatively, removing `-o 'D:\Music\%(title)s.%(ext)s' ` will place the trimmed .mp3 audio file in the same directory.
 5. Run **yt.ps1**, input `Start Time` & `End Time` in format of `HHMMSS`, eg. `013430` for `1 Hour 34 Minutes 30 Seconds`.

# Co-Author
Lexes Jan - https://github.com/lexesjan







