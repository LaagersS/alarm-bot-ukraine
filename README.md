# alarm-bot-ukraine
Telegram bot for air raid alerts (in my case, in the Kharkiv region)

Make sure Python is installed on your computer. Install the required libraries via CMD:

```bash
pip install pyTelegramBotAPI
pip install alerts_in_ua
pip install db-sqlite3
```

Create a bot in Telegram via [https://t.me/BotFather](https://t.me/BotFather). <br>
<img width="491" height="264" alt="Знімок екрана 2025-10-06 о 15 15 51" src="https://github.com/user-attachments/assets/d5d0fb3a-09a0-4cd0-89e7-5b42fb572834" />


Add the bot to your channel and make it an admin. Download the .py file and open it in an editor. Insert your IDs into the code in the places indicated. Run the file and go to the chat with the bot, then type /start. Your bot will post alerts in the channel whose ID you entered in the `chat_id` field. Do not close the .py file. After restarting, go back to the chat with the bot and type /start again — you will see 'started by user' in the console. <br>
<img width="720" height="174" alt="Знімок екрана 2025-10-06 о 15 22 12" src="https://github.com/user-attachments/assets/228e70bd-1c03-411e-a668-908aeac2941d" />
