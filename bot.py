import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('NTcwNjU3NDg0NjU4ODM1NDY2.XMeZ_w.VG9MoM9SXASp5E0NlV0JwnjLaac')
