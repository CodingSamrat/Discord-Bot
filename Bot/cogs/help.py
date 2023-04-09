#: Discord---
from discord.ext import commands
from discord.ext.commands.context import Context

from discord import Guild

#: Bot---
from Bot.utils import LOG


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    #: Bot Events
    #:
    @commands.Cog.listener()
    async def on_ready(self):
        LOG.Cog.success(self)

    #: write commands here
    #:
    @commands.command(name="help", help="Shows this message")
    async def help(self, ctx: Context):
        await ctx.send("Hii, From Help Command")


async def setup(client):
    await client.add_cog(Help(client))
