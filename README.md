
## Overview
The Greeceficator Bot is a Telegram bot designed to transliterate text messages from English and Russian into Greek characters. It uses the python-telegram-bot library to interact with the Telegram API.

## Commands:


`/start` Starts the conversation.

`/help` Provides help information.

`/caps` Converts the message to uppercase after transliteration.

`/lower` Converts the message to lowercase after transliteration.

## Limitations

English has a complex phonetic system that does not easily map to Greek characters. In future versions, we may aim to use International Phonetic Alphabet as a bridge between any language and Greek.

Russian is much more phonetic, but there are still some sounds that does not present in Greek. Some letters would not be transliterated for the sake of readability (this bot aimed to help you learn, not to transpile 100% of the text).

## Installation
Use docker compose and dotenv example
