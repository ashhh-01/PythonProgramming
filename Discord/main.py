import discord
import os 
from dotenv import load_dotenv
load_dotenv(".env")

client = discord.Client(intents=discord.Intents.default())

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    @client.event
    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_BOT_KEY"))