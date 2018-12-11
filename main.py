import discord
from const import *

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message: discord.Message):
    print(message.server, '/',  message.channel, '/', message.author, 'написал', message.content)    
    if message.content.lower().startswith('lgs.say'):
        text = message.content.split('|', 1)[1]
        if message.channel_mentions:
            for i in message.channel_mentions:
                await client.send_message(i, text)
        await client.send_message(message.channel, text)

client.run(token)