import discord
from discord.ext import commands
from discord.utils import get
#\u05D1\u05E0\u05E6\u05D5\u05E7 \u05D0\u05E0\u05D9 \u05D0\u05D5\u05E0\u05DC\u05D9\u05D9\u05DF

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("bot is ready")

@client.command(name="join")
async def join(ctx):
    cahnnel = ctx.message.author.voice.channel
    await cahnnel.connect()
@client.event
async def on_message(message):
    Author = "yohaygaming#0108"
    if message.content == Author:
        print(message.author)
        await message.author.send("שקי שתוק יא זונה")
    await client.process_commands(message)

client.run("NzE5MDY1NDgxNTE2MDIzODI4.Xtx_6g.SKTflJrjt6SZ_lTtmBMsTmY_TY8")