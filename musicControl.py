from asyncio import sleep
import os
import discord
import musicPlayer
# all discord side funtionality

ydl = musicPlayer.getDownloader()

@discord.app_commands.command(name = "play", description = "Start/continue playing current playlist")
@discord.app_commands.describe(url="A youtube URL to play")
async def play(interaction, url: str):
    data = ydl.extract_info(url)
    if interaction.user.voice == None:
        await interaction.response.send(str(interaction.author.name) + "is not in a voice channel.")

    else:
        
        voice_channel = interaction.user.voice.channel
        vc = await voice_channel.connect()
        musicPath = os.getcwd() + '/downloads/' + data["extractor"] + "-" + data["id"] + "-" + data["title"]+ "." + data["ext"] 
        print(musicPath)
        vc.play(discord.FFmpegPCMAudio(source=musicPath))
        # Sleep while audio is playing.
        while vc.is_playing():
            await sleep(.1)
        await vc.disconnect()
    # Delete command after the audio is done playing.
    # await ctx.message.delete()

@discord.app_commands.command(name = "pause", description = "Pause current song")
async def pause(interaction):
    await interaction.response.send_message("pause")

@discord.app_commands.command(name = "skip", description = "Skip to the next song")
async def skip(interaction):
    await interaction.response.send_message("skip")

@discord.app_commands.command(name = "stop", description = "Stop playing and reset the progress for the current playlist")
async def stop(interaction):
    await interaction.response.send_message("stop")

@discord.app_commands.command(name = "playlist", description = "Display current playlist")
async def playlist(interaction):
    await interaction.response.send_message("stop")

#Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
@discord.app_commands.command(name = "search", description = "Search for songs") 
@discord.app_commands.describe(keyword="keyword to search, can be name of the song or artist or any related keyword")
async def searchSong(interaction, keyword: str):
    await interaction.response.send_message("Searching for " + keyword + " ...")

async def setup(cmdTree):
    cmdTree.add_command(play)
    cmdTree.add_command(pause)
    cmdTree.add_command(skip)
    cmdTree.add_command(stop)
    cmdTree.add_command(playlist)
    cmdTree.add_command(searchSong)
