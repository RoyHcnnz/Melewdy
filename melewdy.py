import discord
import secret

TOKEN = secret.BOT_TOKEN

intents=discord.Intents.all()
client = discord.Client(intents=intents)

tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await tree.sync(guild=discord.Object(id=secret.TESTING_SERVER_ID))


#Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
@tree.command(name = "search", description = "Search for songs", guild=discord.Object(id=secret.TESTING_SERVER_ID)) 
async def searchSong(interaction, keyword: str):
    await interaction.response.send_message("Searching for " + keyword + " ...")

client.run(TOKEN)