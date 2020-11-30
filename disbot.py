import discord
from discord.ext import commands
from discord.utils import get
bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    print("bot is ready")
    await bot.change_presence(activity=discord.Game(".help1"))

@bot.event
async def on_message(message):
    general = bot.get_channel(message.channel.id)
    if message.content == "אבי פרטי":
        await message.author.send("בנצ'וק די אני לא גנבתי")
    elif message.content == "בנצ'וק":
            await general.send("זה לא היה אבי")
    await bot.process_commands(message)
            
@bot.command("ban")
async def ban(ctx, member : discord.Member, *, reason=None):

    await member.ban(reason=reason)
    await ctx.send(str(member.mention) + " banned")

@bot.command("members1")
async def members1(ctx):
    mem = ctx.guild.members
    general = bot.get_channel(ctx.channel.id)
    s = 0
    for a in mem:
        s = s + 1
        user = a.name
        await general.send(user)
    await general.send(s)

@bot.event
async def on_member_join(member):
    coni = member.guild
    channelq = get(coni.channels, name="member-count")

    await channelq.edit(name="members: " + str(coni.member_count))
    print(coni.member_count)



@bot.event
async def on_member_remove(member):
    coni = member.guild
    channelq = get(coni.channels, name="member-count")

    await channelq.edit(name="members: " + str(coni.member_count))
    print(coni.member_count)

@bot.command("join")
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
@bot.command("leave")
async def leave(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()

bot.run(TOKEN")
