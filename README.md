# Discord Message Scraper

This Python script allows you to scrape and store message data from a specific Discord channel using the `discord.py` library. The script fetches the entire message history of the designated channel and stores it in a CSV file, making it convenient for later analysis or processing, including Natural Language Processing (NLP) tasks.

## Features

- Fetches and stores message data from a specified Discord channel.
- Captures message timestamps, authors, and message content.
- Saves the data in a CSV file for easy access and manipulation.
- Simple and easy-to-use, with customizable options for different channels.

## Usage

1. **Set up a Discord Bot**: Create a new bot account on the Discord Developer Portal and obtain its token.
2. **Install Dependencies**: Install the required Python libraries (`discord.py`) using pip.
3. **Configure the Script**: Update the script with your bot token and specify the channel you want to scrape.
4. **Run the Script**: Execute the script to start scraping message data from the designated channel.
5. **Access the Data**: Once the script completes, you'll find the scraped data stored in a CSV file (`surf_messages.csv` by default).

## Requirements

- Python 3.x
- `discord.py` library

## License

This project is licensed under the MIT License
