import discord
import os
from quoteApi import get_quote
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Hello")


@client.event
async def on_message(message):

    processed_msg = message.content.upper()
    if message.author == client.user:
        return
    if processed_msg.startswith('HELLO'):

        await message.channel.send('Hi from bot')
    if message.content.startswith('inspire'):
        gQuote = get_quote()
        await message.channel.send(gQuote)
    if message.content.startswith('file'):
        file = discord.File('f.txt')
        await message.channel.send(file=file, content='your file')
client.run(os.getenv('TOKEN'))
