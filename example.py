import discord
import asyncio
import stats
import argparse
import sys

# Pass the token as a commandline argument"
client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!osrsStats'):
        player = message.content.split(" ")[1]
        ms = stats.osrs_request(player)
        await client.send_message(message.channel, ms)
#print(sys.argv[1])
client.run(sys.argv[1])
