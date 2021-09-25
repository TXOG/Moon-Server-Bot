#main.py
#important ids have been hidden
import os
import random
from dotenv import load_dotenv
import keep_alive
import discord
from discord.ext.commands import Bot
import shlex
import requests
from datetime import datetime


load_dotenv()

client = discord.Client()




muneebsquotes = [
        "Yo Muneeb, someone is missing you",
         "He is probably Busy I guess",
          "Uhmm, if he might be studying lol", 
          "Follow him on instagraam @muneeb_ahmed_official"
  ]





@client.event
async def on_ready():
  print("bot is ready")


@client.event
async def on_message(message): 
  #commands
  async def on_message(message):
    if message.author == client.user:
     return

  if message.content.startswith("mo.hello"):
    number = random.randint(0, 3)
    if number == 0:
      await message.channel.send("Hi!")
    elif number == 1:
      await message.channel.send("Hello...")
    elif number == 2:
      await message.channel.send("Go away")
    elif number == 3:
      await message.channel.send("F**k off you gae cant")


  if message.content.startswith("mo.help"):   
    embed=discord.Embed(title="Help")
    embed=discord.Embed(description="I see you are trying to use Muneeb's bot. If you insist, here are the commands:")
    embed.set_author(name="daTXOGllama", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQd_2nCMS88xEZeFGy2ARJJjg9QDyfi9tKW1g&usqp=CAU")
    embed.set_thumbnail(url="https://contenthub-static.grammarly.com/blog/wp-content/uploads/2018/05/how-to-ask-for-help.jpg")
    embed.add_field(name="hello", value="Say hi to the bot...", inline=True)
    embed.add_field(name="triggers", value="Gives a list of the server's triggers", inline=True)
    embed.add_field(name="ban", value="100% works", inline=True)
    embed.add_field(name="test", value="You won't be trolled ... probably ", inline=True)
    embed.add_field(name="random", value="Gives random number between -100 and 100", inline=True)
    embed.add_field(name="changelog", value="Shows bot changelog", inline=True)
    embed.add_field(name="echo", value = "Repeats what you say", inline=True)
    embed.add_field(name="kc", value="kek chat entry - if you don't know what that means then you can't use it", inline=True)
    embed.set_footer(text="Prefix is mo.   • bot created by daTXOGllama#1234",
    icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
    await message.channel.send(embed=embed)

  if message.content.startswith("mo.triggers"):
    embed=discord.Embed(title="Triggers", description="You want triggers? I got that grub my driller:")
    embed.set_author(name="daTXOGllama", url="https://www.youtube.com/watch?v=m_d5PBsuME0", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQd_2nCMS88xEZeFGy2ARJJjg9QDyfi9tKW1g&usqp=CAU")
    embed.set_thumbnail(url="https://media1.tenor.com/images/a20ddd95ed33c6937246c1f37232e519/tenor.gif?itemid=10111909")
    embed.add_field(name="muneeb", value="Every great man should have a list of quotes that one can randomly get from a basic discord bot", inline=True)
    embed.add_field(name="moon", value="Thanks for being part of moon ... every time", inline=True)
    embed.set_footer(text="TRIGGERS ARE CAPS SENSITIVE • bot created by daTXOGllama#1234",
    icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
    await message.channel.send(embed=embed)

  if message.content.startswith("mo.ban"):
    await message.channel.send(f":white_check_mark: Banned {message.author.mention}")

  if message.content.startswith("mo.test"):
    await message.channel.send("<:troll:864486158997913600> <:troll:864486158997913600>")

  if message.content.startswith("mo.echo"):
    if message.author == client.user:
      return
    elif "everyone" in message.content:
      await message.delete()
      await message.channel.send(f"{message.author.mention} you can't use the word `everyone` in your echo")
    elif "here" in message.content:
      await message.delete()
      await message.channel.send(f"{message.author.mention} you can't use the word `here` in your echo")
    elif "@" in message.content:
      await message.delete()
      await message.channel.send(f"{message.author.mention} it's not nice to ping people through this command <:(")
    else:
      arguments = message.content.lstrip('mo.echo')
      arguments = message.content.split(' ', 1)
      arguments = shlex.split(message.content)[1:]
      arguments = message.content[len('mo.echo'):]
      msg = arguments
      await message.delete()
      await message.channel.send(msg)

  if message.content.startswith("mo.kc"):
    message_channel = message.channel.id
    if message_channel == achannelid:
      channel = client.get_channel(achannelid)
      arguments = message.content.lstrip('mo.kc')
      arguments = message.content.split(' ', 1)
      arguments = shlex.split(message.content)[1:]
      arguments = message.content[len('mo.kc'):]
      msg = arguments
      await message.delete()
      await channel.send(msg)

    else:
      await message.delete()
      await message.channel.send("Oop, the command didn't work. Maybe it's because you don't have permission to use it kek ||Actually it's because you are using the wrong channel||")


  if message.content.startswith("mo.random"):
    number = random.randint(-100, 100)
    await message.channel.send("`" + str(number) + "`")

  if message.content.startswith("mo.changelog"):
    embed=discord.Embed(title="Change Log V1.3", url="https://github.com/TXOG", description="eep, who will read this?")
    embed.set_author(name=" daTXOGllama", url="https://www.youtube.com/watch?v=m_d5PBsuME0", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQd_2nCMS88xEZeFGy2ARJJjg9QDyfi9tKW1g&usqp=CAU")
    embed.set_thumbnail(url="https://www.files.construction/wp-content/uploads/sites/14/2020/10/Photo_Jun_30_19-09-42-47-PM.png")
    embed.add_field(name="Ace", value="Removed all references to Ace from commands and triggers", inline=False)
    embed.add_field(name="Embeds", value="Certain commands contain embeds", inline=False)
    embed.add_field(name="Triggers", value="Emojis no longer trigger a responce", inline=False)
    embed.add_field(name="Random", value="Random commands added", inline=False)
    embed.add_field(name="Pings", value="Pinging the bot provokes a reaction", inline=False)
    embed.set_footer(text="Oh look, a footer! • bot created by daTXOGllama#1234",
    icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
    await message.channel.send(embed=embed)

  if str(client.user.id) in message.content:
    embed = discord.Embed(title="Hi there!", description=":D", colour=0x87CEEB, timestamp = datetime.utcnow())
    embed.set_author(name=" daTXOGllama", url="https://www.youtube.com/watch?v=m_d5PBsuME0", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQd_2nCMS88xEZeFGy2ARJJjg9QDyfi9tKW1g&usqp=CAU")
    embed.add_field(name="Why'd you ping me?", value="You need to use the prefix mo. to use the bot", inline=False)
    embed.add_field(name="Help?", value="Use mo.help for a list of commands", inline=True)
    embed.set_footer(text="Bot made by daTXOGllama#1234", icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
    await message.channel.send(embed=embed)





  #triggers
  if "muneeb" in message.content:
    if ":" in message.content:
      return
    else:
      response = random.choice(muneebsquotes)
      await message.channel.send(response)


  if "moon" in message.content:
    if ":" in message.content:
      return
    else:
      await message.channel.send("Thank you Very much for being a part of Moon")











keep_alive.keep_alive()

token = os.environ.get("secret_bot_token")
client.run(token)
