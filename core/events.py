import discord
from config import WELCOME_CHANNEL_ID

def setup_events(bot):
    
    @bot.event # decorar uma função
    async def on_ready():
        print(f"Bot initialized as {bot.user}")

    @bot.event
    async def on_member_join(member: discord.Member):
        channel = bot.get_channel(WELCOME_CHANNEL_ID)
        if channel:
            await channel.send(f"{member.mention} has joined the server!")