import discord


client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as " + str(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("What's up")


secret = open("token.txt")
token = secret.read()
secret.close()
print(token)
print(type(token))
client.run(token)