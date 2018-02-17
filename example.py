import discord
import asyncio
import stats
import argparse
import sys
import tools
import GrandExhange

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
        l = False
        content = message.content
        player, l = tools.parse_osrs_request(content)
        try:
            playerObject = stats.Player(player)
            playerObject = stats.osrs_request_player(player)
        except:
            await client.send_message(message.channel, ("Can't find data for " + player))
            return
        if (l):
            reply = "```" + playerObject.longMessage() + "```"
        else:
            reply = "```"  + playerObject.shortMessage() + "```"
        await client.send_message(message.channel, reply)
    elif message.content.startswith('!osrsGE'):
        ge = GrandExhange.GrandExhangeService()
        try:
            ms = ge.message(message.content)
        except:
            ms = "No such item or too many hits"
        ms = '```' + ms + '```'
        await client.send_message(message.channel, ms)
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
        + "----------\n```"
        await client.send_message(message.channel, reply)

#print(sys.argv[1])
client.run(sys.argv[1])
