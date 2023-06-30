import discord
import secret

TOKEN = secret.BOT_TOKEN

intents=discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)