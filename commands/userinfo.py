from discord.ext import commands
import discord

def setup(bot):

    @bot.command()
    async def userinfo(ctx, member: discord.Member = None):
        member = member or ctx.author

        joined = (
            member.joined_at.strftime("%d/%m/%Y, %H:%M:%S")
            if member.joined_at
            else "Unknown"
        )

        channel = ctx.channel.name

        await ctx.reply(
            f"Your username is: @{member.name}\n"
            f"You have joined: {joined}\n"
            f"You are in: {channel}"
        )
