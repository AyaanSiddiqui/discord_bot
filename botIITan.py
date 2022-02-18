import discord
from keep_running import keep_running

client = discord.Client()

slangs = [] #Enter slangs that you want bot to reply to
responding = True
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

    elif user_message.lower() == "bye":
        await message.channel.send(f"See you later {username}")
        
    elif any(word in user_message for word in slangs):
        await message.channel.send(f"01000110 01010101 01000011 01001011 01011001 01001111 01010101 00100001 {username}")

keep_running()
client.run('TOKEN') #Enter you token here
