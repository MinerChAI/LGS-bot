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
    
    if message.content.lower().startswith('lgs.zdku'):
        await client.send_message(message.channel, message.mentions[0].server_permissions.administrator)
    
    if message.content.lower().startswith('lgs.addroles') and message.author.server_permissions.manage_roles:
        roles = [i for i in message.role_mentions if message.author.top_role >= i]
        for i in message.mentions:
            await client.add_roles(i, *roles)
        await client.send_message(message.channel, 'Роли ' + ', '.join([i.mention for i in message.role_mentions]) + ' добавлены к участникам ' + ', '.join([i.mention for i in message.mentions]))
    
    if message.content.lower().startswith('lgs.removeroles') and message.author.server_permissions.manage_roles:
        roles = [i for i in message.role_mentions if message.author.top_role >= i]
        for i in message.mentions:
            await client.remove_roles(i, *roles)
        await client.send_message(message.channel, 'Роли ' + ', '.join([i.mention for i in message.role_mentions]) + ' сняты с участников ' + ', '.join([i.mention for i in message.mentions]))

client.run(token)