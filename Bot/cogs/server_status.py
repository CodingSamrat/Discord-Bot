#: Discord---
from discord.ext import commands
from discord.ext.commands.context import Context

from discord import Guild

#: Bot---
from Bot.utils import LOG


class ServerStatus(commands.Cog):  # <- Change ->
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    #: Bot Events
    #:
    @commands.Cog.listener()
    async def on_ready(self):
        LOG.Cog.success(self)

    #: write commands here
    #:
    @commands.command(name="ping", help="Shows the latency of Bot")
    async def ping(self, ctx: Context):
        latency = self.bot.latency * 1000
        await ctx.send(f"Bot latency: `{latency}`")


async def setup(client):
    await client.add_cog(ServerStatus(client))
