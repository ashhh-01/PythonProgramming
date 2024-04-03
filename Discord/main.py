import discord,urllib.request
import os 
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv(".\Python Env\env\.env")
intents = discord.Intents.default()
intents.message_content = True
bot=commands.Bot(command_prefix="/",intents=intents)
@bot.event
async def on_message(message):
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        print(f'Message from {message.author}: {message.content}')


@bot.tree.command(name="welcome",description="Settle in")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("Hi! Welcome to the server!👋🤗")

@bot.tree.command(name="avatar", description="Get user avatar")
async def avatar(interaction:discord.Interaction, member:discord.Member):
    await interaction.response.send_message(member.display_avatar)

@bot.tree.command(name="commands", description="The Commands which can be used")
async def command(interaction:discord.Interaction):
    await interaction.response.send_message("You can use these commands \n•/welcome\n•/avatar")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await bot.tree.sync()
bot.run(os.getenv("DISCORD_BOT_KEY"))