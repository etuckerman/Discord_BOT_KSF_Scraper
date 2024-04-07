import os  # Importing the os module for accessing environment variables
import csv  # Importing the csv module for handling CSV files
import discord  # Importing the discord module for interacting with Discord API

# Setting up intents to specify what events the bot should listen to
intents = discord.Intents.default()
intents.message_content = True

# Creating a Discord client instance
client = discord.Client(intents=intents)

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))  # Printing bot's name upon successful login
    channel = discord.utils.get(client.get_all_channels(), name='surf')  # Getting the 'surf' channel
    await fetch_and_store_messages(channel)  # Calling function to fetch and store messages

# Function to fetch and store messages from a channel
async def fetch_and_store_messages(channel):
    # Opening a CSV file for writing
    with open('surf_messages.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)  # Creating a CSV writer object
        writer.writerow(['Author', 'Message'])  # Writing header row to the CSV file

        # Iterating through all messages in the channel's history
        async for message in channel.history(limit=None):
            # Writing author's name and message content to the CSV file
            writer.writerow([message.author.name, message.content])

try:
    token = os.getenv("TOKEN") or ""  # Getting bot token from environment variables
    if token == "":
        raise Exception("Please add your token to the Secrets pane.")  # Raising an exception if token is not provided
    client.run(token)  # Running the bot with the provided token
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e  # Raising any other HTTP exceptions encountered during bot execution
