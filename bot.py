from contextvars import Context
from unicodedata import name
from xmlrpc.client import Boolean
import discord

from os import getenv
from dotenv import load_dotenv
from random import randint

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}({bot.user.id}).")

@bot.slash_command(name="ping", description="Ping!")
async def neko(ctx: discord.ApplicationContext):
    await ctx.respond("pong!")

load_dotenv()
bot.run(getenv("DISCORD_BOT_TOKEN"))