# A music player based on yt-dlp
from yt_dlp import YoutubeDL
import yt_dlp
import json
import discord

URL = 'https://www.youtube.com/watch?v=BaW_jenozKc'
URL2 = 'https://www.youtube.com/watch?v=y3lP_gPjlUo'

ydl_opts = {
    'format': 'm4a/bestaudio/best',
    'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'quiet': True,
    'no_warnings': True,
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }]
}

def getDownloader():
    return yt_dlp.YoutubeDL(ydl_opts)
#with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#    # info = ydl.extract_info(URL)
#    info = ydl.extract_info(URL2)

    
#class musicSource(discord.FFmpegPCMAudio):
