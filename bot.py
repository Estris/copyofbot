orc = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'azyxewvtisrlpnomqkjhugfdcb')
print("Hello, world!".translate(orc))

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello, my sweet prince'):
        await message.channel.send('Hello!')

    if message.content.startswith('Botty boy, come here!'):
        await message.channel.send('Yes?')

    if message.content.startswith('I love you'):
        await message.channel.send('Hohooo~ I love you too~')

    if message.content.startswith('Hello, my knife in shining butter'):
        await message.channel.send('The waffle knight arrives!')
    
    if message.content.startswith('$translate'):
        textToTranslate = message.content[11:]
        print(message.channel)
        await message.channel.send(translate(textToTranslate))

def translate(text):
    #this is where you would do the actual translating. for example, text.maketrans(args)

    #this is an example:
    translated = ""
    for char in text:
        if (char == "a"):
            translated = translated + "3"
        elif (char == "l"):
            translated = translated + "1"
        elif (char == "o"):
            translated = translated + "0"
        elif (char != " "):
            translated = translated + "X"
        else:
            translated = translated + " "
    return translated

client.run('NTcwNjU3NDg0NjU4ODM1NDY2.XMeZ_w.VG9MoM9SXASp5E0NlV0JwnjLaac')


