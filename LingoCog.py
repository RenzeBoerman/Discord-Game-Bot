import discord
from discord.ext import commands

from lingo import Lingo


class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Krijg uitleg over DCLingo
    @commands.command()
    async def uitleg(self, ctx):
        await ctx.send(format("Lingo is een heel simpel spel! De regels: \n"
                              "1. Het is altijd een 5 letter woord \n"
                              "2. Je hebt 5 pogingen om het goeie woord te raden \n"
                              "3. Een woord is speler gebonden(Als jij met een woord bezig bent kan alleen jij die "
                              "raden) \n "
                              "4. Je hebt 2 minuten de tijd om een woord te raden. \n"
                              
                              "\n"
                              "Als een letter op de goede plek staat is het een hoofdletter. \n"
                              "Als een letter in het woord zit maar niet op de goeie plek staat is het een kleine "
                              "letter. \n"
                              "Als een letter fout is is het een _."))

    @commands.command()
    async def lingo(self, ctx):

        mijn_lingo = Lingo()
        turns = 6

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
