import discord,json,requests
import os 
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands


load_dotenv(".\Python Env\env\.env")
GIFHY_API=os.getenv("GIPHY_APIKEY")

intents = discord.Intents.default()
intents.message_content = True
bot=commands.Bot(command_prefix="/",intents=intents)
@bot.event
async def on_message(message):
    if message.content.startswith('BOT'):
        await message.channel.send('Yes! Check out "/commands" to know more!')
        # print(f'Message from {message.author}: {message.content}')


@bot.tree.command(name="welcome",description="Settle in")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message(f"Hi {interaction.user.mention}! Welcome to the server!👋🤗",ephemeral=True)

@bot.tree.command(name="avatar", description="Get user avatar")
async def avatar(interaction:discord.Interaction, member:discord.Member):
    await interaction.response.send_message(member.display_avatar)

@bot.tree.command(name="commands", description="The Commands which can be used")
async def command(interaction:discord.Interaction):
    await interaction.response.send_message("You can use these commands \n•/welcome\n•/avatar\n•/random-gif")

@bot.tree.command(name="say",description="I will convey your messages")
@app_commands.describe(your_message="What would you like me to say?")
async def say(interaction:discord.Interaction,your_message:str):
    await interaction.response.send_message(f"{interaction.user.mention} said `{your_message}`")

@bot.tree.command(name="random-gifs", description="Random gifs")
async def gif(interaction:discord.Interaction):
    response_url=requests.get(f"https://api.giphy.com/v1/gifs/random?api_key={GIFHY_API}&tag=&rating=r").json()["data"]["images"]["downsized"]["url"]
    embed = discord.Embed(title="Random GIF", color=0x4797ff)
    embed.set_image(url=response_url)
    await interaction.response.send_message(embed=embed)
    # print(response)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await bot.tree.sync()
bot.run(os.getenv("DISCORD_BOT_KEY"))