# alarm-bot-ukraine
Telegram bot for air raid alerts (in my case, in the Kharkiv region)

Make sure Python is installed on your computer. Install the required libraries via CMD:

```bash
pip install pyTelegramBotAPI
pip install alerts_in_ua
pip install db-sqlite3
```

Create a bot in Telegram via [https://t.me/BotFather](https://t.me/BotFather).


Add the bot to your channel and make it an admin. Download the .py file and open it in an editor. Insert your IDs into the code in the places indicated. Run the file and go to the chat with the bot, then type /start. Your bot will post alerts in the channel whose ID you entered in the `chat_id` field. Do not close the .py file. After restarting, go back to the chat with the bot and type /start again — you will see 'started by user' in the console.
