import telebot

# Replace with your bot token
API_TOKEN = '7677020842:AAH2EJrJRZPFTzniasiHScSePrk4xOgNYUQ'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send a number and I'll tell if it's Big (5-9) or Small (0-4).")

@bot.message_handler(func=lambda message: message.text.isdigit())
def handle_number(message):
    num = int(message.text)
    if 0 <= num <= 9:
        result = "Big" if num >= 5 else "Small"
        bot.reply_to(message, f"Number: {num} → {result}")
    else:
        bot.reply_to(message, "Please send a single digit number (0-9).")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    bot.reply_to(message, "Please send a number between 0 and 9.")

bot.infinity_polling()
