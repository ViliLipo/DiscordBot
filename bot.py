import discord
import asyncio
import stats
import argparse
import sys
import tools
import GrandExhange

# Pass the token as a commandline argument"
client = discord.Client()
waitTime = 15
ge = GrandExhange.GrandExhangeService()
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
    elif message.content.startswith('!cleanup'):
        def isMe(m):
            return m.author == client.user
        deleted = await client.purge_from(message.channel, limit=100, check=isMe )
        await client.send_message(message.channel, 'Deleted {} message(s)'.format(len(deleted)))
    elif message.content.startswith('!removeMyMessages'):
        author = message.author
        def isAuthor(m):
            return m.author == author
        deleted = await client.purge_from(message.channel, limit=100, check=isAuthor)
        await client.send_message(message.channel, 'Deleted {} message(s)'.format(len(deleted)))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.lower().startswith('!osrsstats'):
        tmp = await client.send_message(message.channel, "Processing request...")
        l = False
        content = message.content
        player, l = tools.parse_osrs_request(content)
        try:
            playerObject = stats.Player(player)
            playerObject = stats.osrs_request_player(player)
        except:
            await client.edit_message(tmp, ("Can't find data for " + player))
            await asyncio.sleep(waitTime)
            client.delete_message(tmp)
            client.delete_message(message)
            return
        if (l):
            reply = "```" + playerObject.longMessage() + "```"
        else:
            reply = "```"  + playerObject.shortMessage() + "```"
        await client.edit_message(tmp, reply)
        await asyncio.sleep(waitTime)
        await client.delete_message(tmp)
        await client.delete_message(message)
    elif message.content.lower().startswith('!osrsge'):
        tmp = await client.send_message(message.channel, "Processing request...")
        #ge = GrandExhange.GrandExhangeService()
        try:
            ms = ge.message(message.content)
        except:
            ms = "No such item or too many hits"
        ms = '```' + ms + '```'
        await client.edit_message(tmp, ms)
        await asyncio.sleep(waitTime)
        await client.delete_message(tmp)
        await client.delete_message(message)
    elif message.content.startswith('!help'):
        reply = "```Commands : \n" \
        + "!help \nDisplays this message \n" \
        + "--------\n" \
        + "!osrsStats [-l] [playername] \n" \
        + "Shows HiScores for given playername \n" \
        + "if -l parameter is passed statistics, for all skills are shown \n" \
        + "---------\n" \
        + "!osrsGE [item] \n" \
        + "Finds GE information for objects that match item \n" \
        + "----------\n" \
        + "All requests and responses are displayed for {} seconds```".format(waitTime)
        reply = await client.send_message(message.channel, reply)
        await asyncio.sleep(waitTime)
        await client.delete_message(message)
        await client.delete_message(reply)

#print(sys.argv[1])
import os
client.run(os.environ['TOKEN'])
