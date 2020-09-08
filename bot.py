import discord
import asyncio

client = discord.Client('NzUyNzM4MDA2ODI1MzA0MTE2.X1b_5g.p-kWeZ5QAQgKAgYXHZ7XnF9om4M')

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

client.run('NzUyNzM4MDA2ODI1MzA0MTE2.X1b_5g.p-kWeZ5QAQgKAgYXHZ7XnF9om4M')
