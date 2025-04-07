from dotenv import load_dotenv
load_dotenv()
import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

@bot.command()
async def hola(ctx):
    await ctx.send("¡Hola desde el bot!")

@bot.command()
async def robux(ctx, neto: int):
    precio = neto / 0.7
    precio = round(precio)
    await ctx.send(f"💸 Para recibir **{neto} robux** después del 30% de comisión, debes poner el precio en: **{precio} robux**.")


bot.run(os.getenv("DISCORD_TOKEN"))
