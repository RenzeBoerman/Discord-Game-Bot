from discord.ext import commands


class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Event
    @commands.command()
    async def on_ready(self):
        print('Bot is online!')

    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")


def setup(bot):
    bot.add_cog(Ping(bot))
