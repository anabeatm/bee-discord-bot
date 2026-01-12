import discord
import os

from discord.ext import commands
from dotenv import load_dotenv

from config import PREFIX
from core.events import setup_events
from commands import setup_commands

def main():
    load_dotenv()
    token = os.getenv('TOKEN')

    if not token:
        raise ValueError("Error: TOKEN is not configured")

    intents = discord.Intents.default() # permissões que o bot precisa para funcionar -> all -> todas elas
    intents.members = True # para pegar membros
    intents.voice_states = True # para saber o canal
    intents.message_content = True # aparentemente essencial
    
    bot = commands.Bot(PREFIX, intents=intents)

    setup_events(bot)
    setup_commands(bot)

    bot.run(token)

        
    # @bot.command()
    # async def falar(ctx:commands.Context, *, texto): # '*' faz com que o discord capture todo o texto
    #     await ctx.send(texto)



if __name__ == "__main__":
    main()
