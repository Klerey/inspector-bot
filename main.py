import discord
from discord.ext import commands
import os
import random
import youtube_dl
import time
import asyncio

client = commands.Bot(command_prefix="=", intents = discord.Intents.all())
client.remove_command("help")

x = []
for i in range(1, 501):
  x.append(i)

winning_list = [69,420]



@client.event
async def on_ready():
    print("Mr.Inspector at your server!")
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="=help"
    ))

@client.group(invoke_without_command=True)
async def help(ctx):
  embed = discord.Embed(title='Help', description='Use =help <command> for more information about that specific command. ',color=0xFF5733)
  embed.add_field(name='Utility', value='addrole, removerole, move, ping', inline = False)
  embed.add_field(name='Fun', value='f, lootbox, play, stop, vote, yesno',inline = False)
  await ctx.send(embed=embed)

@help.command()
async def addrole(ctx):
  embed = discord.Embed(title='Add role', description="This command required manage channels permission. It can be use to give any role as long as the bot's role is higher than that role")
  embed.add_field(name='**Syntax**', value='=addrole <target> <role>', inline=False)
  embed.add_field(name='**Aliases**', value='add, add-role', inline=False)
  await ctx.send(embed=embed)

@help.command()
async def removerole(ctx):
  embed = discord.Embed(title='Remove role', description="This command required manage channels permission. It can be use to remove any role as long as the bot's role is higher than that role.")
  embed.add_field(name='**Syntax**', value='=removerole <target> <role>', inline=False)
  embed.add_field(name='**Aliases**', value='remove, remove-role', inline=False)
  await ctx.send(embed=embed)

@help.command()
async def move(ctx):
  embed = discord.Embed(title='Move', description="Move a user in a voice chat.")
  embed.add_field(name='**Syntax**', value='=move <target> "<voice channel name>"', inline=False)
  await ctx.send(embed=embed)

@help.command()
async def ping(ctx):
  embed = discord.Embed(title='Ping!', description="Pong!")
  embed.add_field(name='**Syntax**', value='=ping', inline=False)
  await ctx.send(embed=embed)

@help.command()
async def f(ctx):
  embed = discord.Embed(title='F', description="Press **F** to pay respect.")
  embed.add_field(name='**Syntax**', value='=f', inline=False)
  await ctx.send(embed=embed)

@help.command()
async def lootbox(ctx):
  embed = discord.Embed(title='Loot box', description="This command is a like a gacha machine. It will random a number between 1 to 500. If you got 69 or 420, you will get a special role!")
  embed.add_field(name='**Syntax**', value='=lootbox', inline=False)
  embed.add_field(name='**Aliases**', value='loot-box, loot_box, loot', inline=False)
  await ctx.send(embed=embed)

@help.command()
async def yesno(ctx):
  embed = discord.Embed(title='Yes or No?', description="Ask any yes or no question.")
  embed.add_field(name='**Syntax**', value='=yesno <the question>', inline=False)
  await ctx.send(embed=embed)

@help.command()
async def vote(ctx):
  embed = discord.Embed(title='Vote!', description="Let any memeber create a poll for anything. Any question or answer needs to be put in a quotation mark.")
  embed.add_field(name='**Syntax**', value='=vote "<the question>" "<Answer1>" "<Answer2>"', inline=False)
  embed.add_field(name='**Aliases**', value='poll', inline=False)
  await ctx.send(embed=embed)

@help.command()
async def play(ctx):
  embed = discord.Embed(title='Play', description="Play any music on Youtube! The command has a slight delay of 10 second to 1 minute. Please be patient. In addition, there is a bug right now with this function, if the bot are in a voice chat before you use this command it will not work. This issue will be fix soon. Solution for right now is to use command =leave every time before playing a new song")
  embed.add_field(name='**Syntax**', value='=play <url>', inline=False)
  await ctx.send(embed=embed)



@client.command(aliases = ['Yesno', 'YesNo', 'Yes-No'])
async def yesno(ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(title=message, url="https://youtu.be/wDgQdr8ZkTw", color=0xFF5733)
    embed.add_field(
        name="👍 Yes", value='.', inline=False)
    embed.add_field(
        name="👎 No", value='.', inline=False)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')


@client.command(aliases = ['Play'])
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    channel = ctx.author.voice.channel
    await channel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    await ctx.send("> The song has been played!")


@client.command()
async def stop(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if voice.is_playing():
    voice.pause()
  else:
    await ctx.send("No audio is playing right now.")

@client.command(aliases = ['F'])
async def f(ctx):
  await ctx.send("""
  FFFFFFFFFFFFFFFFFFFFF
F
F
F
F
FFFFFFFFFFFFF
F
F
F
F
F
  """)


@client.command()
async def leave(ctx):
    if ctx.author.voice is None:
        await ctx.send("> Im not in a channel ")
        return
    await ctx.voice_client.disconnect()
    await ctx.send("> I am disconnected!")


@client.command(aliases = ['loot-box, loot_box, loot'])
@commands.cooldown(1, 3600, commands.BucketType.user)
async def lootbox(ctx):
  output = random.choice(x)
  if output == 69:
    await ctx.send("> CONGRATS, YOU JUST GOT THE **Lucky_boi** ROLE! " + str(output))
    member = ctx.message.author
    role = discord.utils.get(member.guild.roles, name="Lucky_boi")
    await member.add_roles(role)

  elif output == 420:
    await ctx.send("> CONGRATS, YOU JUST GOT THE **Lucky_boi** ROLE! " + str(output))
    member = ctx.message.author
    role = discord.utils.get(member.guild.roles, name="Lucky_boi")
    await member.add_roles(role)

  else: 
    await ctx.send(f"> {str(output)}  Sadly, you did not won the jackpot (69 and 420 are the winning number)")


@client.command(aliases =['add', 'add-role', 'Add'])
@commands.has_permissions(manage_channels=True)
async def addrole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"> hey {ctx.message.author.mention}, {member.name} has been given a role called: {role.name}")


@client.command(aliases =['remove', 'remove-role', 'Remove'])
@commands.has_permissions(manage_channels=True)
async def removerole(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    await ctx.send(f"> hey {ctx.message.author.mention}, {member.name} has been removed from a role called: {role.name}")


@client.event
async def on_command_error(ctx, error):
  await ctx.send(f"> An error occured: {str(error)}")


@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def ping(ctx):
    await ctx.send("> Pong!")


@client.command(pass_context=True)
async def rroll(ctx):
  if (ctx.author.voice):
    channel = ctx.author.voice.channel
    await channel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("rick.m4a"))
    await ctx.send(f"> AHA, you've been rick roll'd by {ctx.message.author.mention}")
  else:
    await ctx.send("> I cannot rick roll you because you are not in a voice channel!")

  time.sleep(19)
  await ctx.voice_client.disconnect()

@client.command(aliases =['Vote', 'poll','Poll'])
async def vote(ctx, q, a1, a2):
  await ctx.message.delete()
  embed=discord.Embed(title=q, url="https://youtu.be/VBlFHuCzPgY", color=0x4FFAE1)
  embed.add_field(name=f"1️⃣ {a1}", value=".", inline=False)
  embed.add_field(name=f"2️⃣ {a2}", value=".", inline=False)
  msg = await ctx.send(embed=embed)
  await msg.add_reaction('1️⃣')
  await msg.add_reaction('2️⃣')


@client.command()
async def rolling(ctx, member: discord.Member):
  voice_state = member.voice
  if (voice_state):
    channel = member.voice.channel
    await channel.connect()
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    voice.play(discord.FFmpegPCMAudio("rick.m4a"))
    await ctx.send(f"> AHA, {member.mention} has been rick roll'd by {ctx.message.author.mention}")
  else:
    await ctx.send(f"> The user you mentioned is not in a voice channel!")

  time.sleep(19)
  await ctx.voice_client.disconnect()


@client.command(aliases =['Move'])
async def move(ctx, member: discord.Member, channel):
    vcchannel = discord.utils.get(ctx.guild.voice_channels, name = channel)
    await member.move_to(vcchannel)
    await ctx.send(f"{ctx.message.author.mention}, you have successfully moved {member.mention} to {channel}")


client.run(TOKEN)
