import discord
import asyncio

client = discord.Client('NzQxODgyNDYwODQ0ODUxMjUx.Xy-B4g.QgBS5Yi_DVv1J6OhymXs529PetM')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
       await client.send_message(message.channel, 'Pong!')

client.run('NzQxODgyNDYwODQ0ODUxMjUx.Xy-B4g.QgBS5Yi_DVv1J6OhymXs529PetM')
