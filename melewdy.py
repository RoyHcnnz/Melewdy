import discord
import secret

TOKEN = secret.BOT_TOKEN

intents = discord.Intents.all()
client = discord.Client(intents=intents)

tree = discord.app_commands.CommandTree(client)

class MyGroup(discord.app_commands.Group):
    @discord.app_commands.command(name="greet", description="Say hello")
    async def greet(self, interaction, member: discord.Member):
        await interaction.response.send_message("Hello, " + member.name)

sub1 = MyGroup(name="group", description="A test for cmd group")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # sync slash commands
    tree.add_command(sub1)
    await tree.sync()
    # await sub1.sync(guild=discord.Object(id=secret.TESTING_SERVER_ID))


#Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
@tree.command(name = "search", description = "Search for songs") 
@discord.app_commands.describe(keyword="keyword to search, can be name of the song or artist or any related keyword")
async def searchSong(interaction, keyword: str):
    await interaction.response.send_message("Searching for " + keyword + " ...")

@tree.command(name = "ping", description = "Ping") 
async def searchSong(interaction):
    await interaction.response.send_message("Pong")

client.run(TOKEN)