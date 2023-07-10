import discord
from discord.ext.commands import Bot
import secret
import musicControl

TOKEN = secret.BOT_TOKEN

intents = discord.Intents.all()
melewdyBot = Bot(".", intents=intents)

tree = melewdyBot.tree

class MyGroup(discord.app_commands.Group):
    @discord.app_commands.command(name="greet", description="Say hello")
    async def greet(self, interaction, member: discord.Member):
        await interaction.response.send_message("Hello, " + member.name)

sub1 = MyGroup(name="group", description="A test for cmd group")


@melewdyBot.event
async def on_ready():
    print(f'{melewdyBot.user} has connected to Discord!')
    # sync slash commands
    tree.add_command(sub1)
    await musicControl.setup(melewdyBot)
    await tree.sync()
    # await sub1.sync(guild=discord.Object(id=secret.TESTING_SERVER_ID)) 

melewdyBot.run(TOKEN)