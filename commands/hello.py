from discord.ext import commands

def setup(bot):

    @bot.command() 
    async def hello(ctx: commands.Context): # contextualizção do comando: user, chat, canal
        name = ctx.author.display_name
        await ctx.reply(f"👋 Hello, {name}! How r u? 👀")