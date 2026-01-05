import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = os.getenv('TOKEN')

if TOKEN is None:
    raise ValueError("Error: Token is not configured!")

permisions = discord.Intents.all() # permissões que o bot precisa para funcionar -> all -> todas elas
permisions.members = True # para pegar membros
permisions.voice_states = True # para saber o canal
bot = commands.Bot(".", intents=permisions)

@bot.event # decorar uma função
async def on_ready():
    print(f"Bot inicialized as {bot.user}!")

@bot.event
async def on_member_join(member: discord.Member):
    channel = bot.get_channel(1146522478357778573)
    await channel.send(f"{member.mention} entrou no servidor!")

@bot.command()
async def ola(ctx:commands.Context): # contextualizção do comando: user, chat, canal
    nome = ctx.author.display_name
    await ctx.reply(f"👋 Olá, {nome}! Tudo bem?")

@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    username = ctx.author.name
    entrou = member.joined_at.strftime("%d/%m/%Y, %H:%M:%S")
    canal = ctx.channel.name
    await ctx.reply(f"""Seu user é: @{username}
Você entrou em: {entrou}
Você está no canal: {canal}""")
    
@bot.command()
async def falar(ctx:commands.Context, *, texto): # '*' faz com que o discord capture todo o texto
    await ctx.send(texto)




bot.run(TOKEN)

