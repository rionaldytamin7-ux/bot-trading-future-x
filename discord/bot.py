import discord

from discord.ext import commands

from config import Config

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)