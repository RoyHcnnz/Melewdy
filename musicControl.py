from asyncio import sleep
import os
import discord
from discord.ext import commands
import musicPlayer
# all discord side funtionality

class musicControl(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.vc = None
        self.player: musicPlayer.MusicPlayer = None

    @discord.app_commands.command(name = "join", description = "Join the voice channel")
    async def join(self, interaction: discord.Interaction):
        if interaction.user.voice == None:
            await interaction.response.send_message(str(interaction.user.name) + " is not in a voice channel.")
            return
        
        voice_channel = interaction.user.voice.channel
        self.vc = await voice_channel.connect()
        self.player = musicPlayer.MusicPlayer(self.vc)
        await interaction.response.send_message("Joined voice channel")
        
    @discord.app_commands.command(name = "search", description="search a keyword/youtube url for a song or a playlist")
    @discord.app_commands.describe(keyword="keyword to search/youtube url for a song or a playlist")
    async def search(self, interaction: discord.Interaction, keyword: str):
        if self.vc is None:
            await interaction.response.send_message("Please use /join first")
            return
        await interaction.response.send_message("Searching ... ")
        songs = await self.player.search(keyword)
        if len(songs) == 0:
            await interaction.followup.send("Nothing is found. Please try again with another keyword.")
        resultStr = "Here is what I found: \n"
        for song in songs:
            resultStr += song['title'] + "\n"
        await interaction.followup.send(resultStr)

        


    #  returned from extract url
    #{
    #    "id": "y3lP_gPjlUo",
    #    "title": "孫燕姿 Sun Yan-Zi - 第一天 First Day (official 官方完整版MV)",
    #    "thumbnail": "https://i.ytimg.com/vi_webp/y3lP_gPjlUo/sddefault.webp",
    #    "description": "孫燕姿 Sun Yan-Zi – 完美的一天 A Perfect Day\n[ ♬ 數位音樂平台]\nhttps://TWBC.lnk.to/SunPERFECTLY\n孫燕姿精選歌單\nhttps://TopsifyTW.lnk.to/nQtIzLY\n[ ♬ 實體專輯購買]\n華納購物網 https://goo.gl/3NfLQK\n博客來 https://goo.gl/mHtgcT\n五大唱片 https://goo.gl/w0O0bQ\n佳佳唱片 https://goo.gl/Ej0COu\n山海山音樂 https://goo.gl/nOXAbN\n----------------------------------------------------------------------------------------------\n● 第12屆金曲獎「最佳新人」、第16屆金曲獎「最佳女演唱人」\n● 全亞洲超過3000萬張銷量、華語樂壇最具影響力和指標性女歌手\n\nA perfect world , A perfect day！\n孫燕姿 完美的一天，超乎你的想像。\n「一望無際的海邊沙灘，一間灑滿陽光的房子，一個一起生活的人，2隻小狗，總不完的音樂，自由自在著……。」\n完美的一天，孫燕姿音樂旅途，新的一頁…\n\n★ 從音樂製作發想開始，如何透過新的製作人從零開始是主要的關鍵\n賈敏恕「完美的一天」，FIR+五月天+孫燕姿聯合創作與製作的「第一天」\n我們可以從新的合作上，聽到新的音樂性。\n\n完美的一天 是孫燕姿的第9張作品，於2005年10月07日發行。\n\n跟著 #藍色點唱機 一起聽音樂吧！\nFacebook http://smarturl.it/BJBFB\nKKBOX http://smarturl.it/BJBKK\nSpotify http://smarturl.it/BJBSP",
    #    "duration": 254,
    #    "webpage_url": "https://www.youtube.com/watch?v=y3lP_gPjlUo"
    #}
    @discord.app_commands.command(name = "play", description = "Start/continue playing current playlist")
    async def play(self, interaction):
        
        await interaction.response.send_message("Preparing ...")
        
        await interaction.followup.send("Playing ...")
            
        # Delete command after the audio is done playing.
        # await ctx.message.delete()

    @discord.app_commands.command(name = "pause", description = "Pause current song")
    async def pause(self, interaction):
        if self.vc is None:
            await interaction.response.send_message("Please use /join first")
            return
        else:
            self.vc.pause()
            await interaction.response.send_message("Paused")

    @discord.app_commands.command(name = "skip", description = "Skip to the next song")
    async def skip(self, interaction):
        await interaction.response.send_message("skip")

    @discord.app_commands.command(name = "stop", description = "Stop playing and reset the progress for the current playlist")
    async def stop(self, interaction):
        await interaction.response.send_message("stop")

    @discord.app_commands.command(name = "playlist", description = "Display current playlist")
    async def playlist(self, interaction):
        await interaction.response.send_message("stop")


async def setup(bot: commands.Bot):
    await bot.add_cog(musicControl(bot))
