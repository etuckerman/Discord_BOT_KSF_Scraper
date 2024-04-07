import os
import csv
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

async def fetch_and_store_messages(channel):
    with open('surf_messages.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Author', 'Message'])

        async for message in channel.history(limit=None):
            # Check if the message is not blank and does not contain only emotes
            if message.content.strip() and not message.mentions:
                # Write author's name and message content to the CSV file
                writer.writerow([message.author.name, message.content])

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = discord.utils.get(client.get_all_channels(), name='surf')
    await fetch_and_store_messages(channel)

try:
    token = os.getenv("TOKEN") or ""
    if token == "":
        raise Exception("Please add your token to the Secrets pane.")
    client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e
