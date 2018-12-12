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
    if message.content.lower().startswith('lgs.'):
        cmd = ' '.join(message.content[4:])    
        if message.content.lower().startswith('say'):
            text = message.content.split('|', 1)[1]
            if message.channel_mentions:
                for i in message.channel_mentions:
                    await client.send_message(i, text)
            await client.send_message(message.channel, text)
    
        if message.content.lower().startswith('zdku'):
            await client.send_message(message.channel, message.mentions[0].server_permissions.administrator)
    
        if message.content.lower().startswith('addroles') and message.author.server_permissions.manage_roles:
            roles = [i for i in message.role_mentions if message.author.top_role >= i]
            for i in message.mentions:
                await client.add_roles(i, *roles)
            await client.send_message(message.channel, 'Роли ' + ', '.join([i.mention for i in message.role_mentions]) + ' добавлены к участникам ' + ', '.join([i.mention for i in message.mentions]))
    
        if message.content.lower().startswith('removeroles') and message.author.server_permissions.manage_roles:
            roles = [i for i in message.role_mentions if message.author.top_role >= i]
            for i in message.mentions:  
                await client.remove_roles(i, *roles)
            await client.send_message(message.channel, 'Роли ' + ', '.join([i.mention for i in message.role_mentions]) + ' сняты с участников ' + ', '.join([i.mention for i in message.mentions]))
    
        if cmd.lower().startswith('help'):
            embed=discord.Embed(title='Помощь по боту', color=0x008800)
            embed.set_author(name="LGS бот")
            embed.add_field(name='`lgs.help`', value='Увидеть этот список', inline=True)
            embed.add_field(name='`lgs.say [каналы...] | <текст>`', value='Написать сообщение в `каналы...`', inline=True)
            embed.add_field(name='`lgs.addroles` <роли> <участники>', value='Добавить `роли` к `участники`', inline=True)
            embed.add_field(name='`lgs.removeroles` <роли> <участники>', value='Убрать `роли` с `участники`', inline=True)
            embed.set_footer(text='Помоги создателю!\nWMR: R725794253675\nQiwi:+79166758407')
            await client.send_message(message.channel, embed=embed)

client.run(token)