from telebot import *
from alerts_in_ua import Client as AlertsClient
from datetime import datetime
import pytz
import sqlite3
import time

# Connect to local SQLite database (to store alarm status)
db = sqlite3.connect("Local.db", check_same_thread=False)
sql = db.cursor()

# Create table if it doesn't exist
sql.execute("""CREATE TABLE IF NOT EXISTS Alarms (
    Sended TEXT
    )""")
db.commit()

# Initialize the table with default value if empty
sql.execute("SELECT Sended FROM Alarms")
if sql.fetchone() is None:
    sql.execute("INSERT INTO Alarms VALUES(?)", ("T",))
    db.commit()

# Initialize Telegram bot
bot = TeleBot("write your token")  # ⚠️ replace with your token from https://t.me/BotFather

# Initialize alerts client for alerts.in.ua
alerts_client = AlertsClient(token="write your token")  # ⚠️ get token from https://alerts.in.ua/api-request?

def main(message):
    # Chat or channel ID where the bot will send alerts
    chat_id = "write here the id of the channel or chat in which you want to write about the air alarm"  
    # Use https://t.me/getmyid_bot to find the ID (forward a message from the channel to get its ID)

    while True:
        # Get current time in Kyiv timezone
        kyiv_timezone = pytz.timezone('Europe/Kiev')
        current_time_in_kyiv = datetime.now(kyiv_timezone)
        current_time = current_time_in_kyiv.strftime("%H:%M")

        # Get all active alerts in Ukraine
        active_alerts = alerts_client.get_active_alerts()

        # Filter alerts for specific region (22 = Kharkiv region)
        location_uid_alerts = active_alerts.get_alerts_by_location_uid('22')

        # Check current status in the database
        sql.execute("SELECT Sended FROM Alarms")
        check = sql.fetchone()

        # If an alert is active but hasn't been sent yet — send alert message
        if location_uid_alerts != [] and check[0] != "T":
            bot.send_message(chat_id, f"🔴ATTENTION! Air raid alert declared, EVERYONE go to shelter‼️ {current_time}")
            sql.execute("UPDATE Alarms SET Sended = 'T'")
            db.commit()

        # If alert is cleared but hasn't been sent yet — send 'all clear' message
        elif location_uid_alerts == [] and check[0] != "F":
            bot.send_message(chat_id, f"🟢ALL CLEAR‼️ {current_time}")
            sql.execute("UPDATE Alarms SET Sended = 'F'")
            db.commit()

        # Check status every 60 seconds
        time.sleep(60)

# Command /start — starts the main checking loop
@bot.message_handler(commands=["start"])
def start(message):
    print("Bot started by user")
    print("User chat ID:", message.chat.id)
    main(message)

print("Bot started")
bot.infinity_polling()  # infinite polling to keep the bot running
