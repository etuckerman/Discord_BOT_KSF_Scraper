# Discord BOT KSF Scraper

This Discord bot, created using discord.py, is designed to scrape messages from a specified channel and store them in a CSV file. It offers the flexibility to customize the rate at which messages are stored and includes features to filter out unwanted messages.

## Features

- **Message Scraping**: The bot can scrape messages from a specified channel in a Discord server.
- **Customizable Rate Limiting**: You can customize the rate at which messages are stored, allowing for efficient scraping while respecting Discord API rate limits.
- **Filtering**: Unwanted messages, such as bot commands or messages containing only data between '<>', can be filtered out to ensure that only relevant messages are stored.
- **Exclude Specific Users**: Messages from specific users, such as bots, can be excluded from the scraping process.

## Usage

1. Clone this repository to your local machine.
2. Set up your environment variables, including the Discord bot token and any other configurations.
3. Customize the bot's behavior, such as specifying the channel to scrape and setting the rate at which messages are stored.
4. Run the bot using `python main.py` and monitor the console output for any errors or messages.
5. The bot will scrape messages from the specified channel and store them in a CSV file named `surf_messages.csv`.

## Environment Variables

- `TOKEN`: Your Discord bot token. This is required for the bot to authenticate with the Discord API.

## Dependencies

- Python 3.7+
- discord.py

## Contributors

- [Elliot Tuckerman](https://github.com/etuckerman)

## License

This project is licensed under the MIT License.
