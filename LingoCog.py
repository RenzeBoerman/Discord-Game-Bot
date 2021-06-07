import discord
from discord.ext import commands

from lingo import Lingo


class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Krijg uitleg over DCLingo
    @commands.command()
    async def uitleg(self, ctx):
        embed = discord.Embed(title="LINGO uitleg", color=discord.Colour.gold())
        embed.add_field(name="Regel 1:", value="1. Ieder woord is 5 letters!", inline=True)
        embed.add_field(name="Regel 2:", value="2. Je hebt 2 minuten na ieder gok om een nieuwe gok te doen!", inline=True)
        embed.add_field(name="Regel 3:", value="3. Je hebt 5 beurten daarna ben je af!")
        embed.add_field(name="Documentatie GOED:", value="Een letter op de GOEDE plek is DIKGEDRUKT en een HOOFDLETTEE!", inline=True)
        embed.add_field(name="Documentatie BIJNA:", value="Een letter die IN het WOORD zit maar niet op de goede plek is een HOOFDLETTER", inline=True)
        embed.add_field(name="Documentatie FOUT", value="Een letter die NIET in het woord voorkomt is DOORGESTREEPT en een KLEINE LETTER", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def lingo(self, ctx):

        mijn_lingo = Lingo()
        turns = 5

        # Functie die kijkt naar de volgende messages en of het van de orginele user is!
        def check(message):
            return ctx.author == message.author

        await ctx.send("Je spel is begonnen! Je hebt 5 beurten en als je 2 min niet typt stopt het spel ook!")

        while turns >= 0:
            msg = await self.bot.wait_for("message", timeout=120.0, check=check)
            gok = msg.content.lower()
            uitvoer = mijn_lingo.validate_input(gok)

            embed = discord.Embed(title="LINGO", color=discord.Colour.blue())
            embed.add_field(name="Geraden", value=gok, inline=False)
            embed.add_field(name="Resultaat", value=uitvoer, inline=False)
            embed.add_field(name="Beurten", value=turns, inline=False)
            embed.add_field(name="Gebruiker", value=ctx.author, inline=False)
            await ctx.send(embed=embed)
            if uitvoer == "Gewonnen":
                await ctx.send("GOEDZO! Je hebt gewonnen.")
                break
            turns = turns - 1
            if turns < 0:
                await ctx.send("Je hebt geen beurten meer. Het woord was: " + mijn_lingo.woord + ".")


def setup(bot):
    bot.add_cog(Ping(bot))
