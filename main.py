import os
import discord
from discord.ext import commands
import random

fate = discord.Client()

cunny_words = ["kawaii Fate", "u r cute Fate"]

starter_encouragements = [">-<","///>_<///", "BAKA!!"]

@fate.event
async def on_ready():
  print('Ready to Login')

@fate.event
async def on_message(msg):
  if msg.author == fate.user:
    return
  if msg.content.startswith('!hello'):
    await msg.channel.send('Nyahallo')
  if any(word in msg.content for word in cunny_words):
    await msg.channel.send(random.choice(starter_encouragements))
  if msg.content.startswith('!owner'):
    await msg.channel.send('Ferunando is my Creator + my Papa Xp')

fate.run(os.getenv("token3"))