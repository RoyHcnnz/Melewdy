# A music player based on yt-dlp
from yt_dlp import YoutubeDL
import yt_dlp
import json
import discord

# Each song is a dict with keys: {title, url, ext, id}
class Playlist:
    """
    A playlist of song names with their youtube URLs to play
    """
    playlist: list
    currentIdx: int

    def __init__(self):
        self.playlist = []
        self.currentIdx = 0

    def __str__(self):
        str_ = ""
        for idx in range(len(self.playlist)):
            song = self.playlist[idx]
            if(idx == self.currentIdx):
                str_ += " -> "
            else:
                str_ += "    "
            str_ += song['title'] + ' ' + song['id'] + ' ' + song['ext'] + "\n"
            str_ += '        ' + song['url'] + "\n"
        return str_

    def add(self, songs: list):
        self.playlist.extend(songs)

    def getSong(self):
        return self.playlist[self.currentIdx]
    
    def next(self):
        self.currentIdx += 1
        return self.playlist[self.currentIdx]

# use asyncio to create a coroutine
class MusicPlayer:
    vc: discord.VoiceClient
    ytdl: yt_dlp.YoutubeDL
    playlist: Playlist
    currentSongInfo: dict

    def __init__(self, vc: discord.VoiceClient):
        self.vc = vc
        ydl_opts = {
            'format': 'm4a/bestaudio/best',
            'default_search': 'auto',
            'outtmpl': 'downloads/%(id)s.%(ext)s',
            'quiet': True,
            'no_warnings': True,
            # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
            'postprocessors': [{  # Extract audio using ffmpeg
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }]
        }
        self.ytdl = yt_dlp.YoutubeDL(ydl_opts)
        self.playlist = Playlist()

    def play(self):
        # if paused, resume
        musicPath = self.playlist.getSong()['url']
        self.vc.play(discord.FFmpegPCMAudio(source=musicPath))
    
    def addToPlaylist(self, song, idx):
        pass

    def addToPlaylistEnd(self, songs):
        self.playlist.add(songs)
    
    def addToPlaylistNext(self, song):
        pass
    
    def next(self):
        pass
    
    def stop(self):
        pass

    async def search(self, keyword: str):
        data = self.ytdl.extract_info(keyword, download=False)
        songList = []
        if 'playlist?list' in keyword:
            for entry in data['entries']:
                # print("title: " + entry['title'] + ' ' + entry['webpage_url'])
                songList.append({
                    'title': entry['title'],
                    'id': entry['id'],
                    'ext': entry['ext'],
                    'url': entry['webpage_url']
                })
        elif 'entries' in data:
            #mySongUrl=str(data['entries'][0]['webpage_url'])
            #print(mySongUrl)
            #print("find " + str(len(data['entries'])) + " results")
            #entryEle = data['entries'][0]
            #for k in entryEle.keys():
            #    print(k)
            print("Found search result")
            for entry in data['entries']:
                songList.append({
                    'title': entry['title'],
                    'id': entry['id'],
                    'ext': entry['ext'],
                    'url': entry['webpage_url']
                })
        else: 
            songList.append({
                'title': data['title'],
                'id': data['id'],
                'ext': data['ext'],
                'url': data['webpage_url']
            })
        return songList
            
            
        #return mySongUrl

#mp = MusicPlayer(None)
#songlist = mp.search("https://www.youtube.com/playlist?list=PL-dZyk71ncOuewuSQB92WTM5aF7KnBh6j")
#mp.addToPlaylistEnd(songlist)
#print(mp.playlist)