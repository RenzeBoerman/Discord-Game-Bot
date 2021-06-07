import discord
from discord.ext import commands

import os

TOKEN = "ODQ3NDYwNzgxMTIxMDc3MjU4.YK-ZWw.eHaAFXl6i9D07COwAuluwEoDr5I"

bot = commands.Bot(command_prefix="*")


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(TOKEN)
