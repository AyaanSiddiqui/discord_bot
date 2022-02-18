import discord

client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message  = str(message.content)
    print(f"{username}: text on channel {channel}")

    if user_message.lower() == "hello" or user_message.lower() == "hi" or user_message.lower() == "hi bot" or user_message.lower() == "hello bot":
        await message.channel.send(f"Hello {username}. Great to see you again.")
        
    if user_message.lower() == "bye":
        await message.channel.send(f"See you later {username}")
        

client.run('OTQ0MDk2MDcxMzc2ODYzMjQy.Yg8n-w.UARHySjvPsRVBODQw16ZBbiK8Yc')
