import os
import telebot
import requests
from io import BytesIO
from generator import generate_image
from utils import resize_image

BOT_TOKEN = ''

# Telegram bot setup
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['photo'], func=lambda message: True)
def handle_photo(message):
    # Check if the message has a caption (text)
    if message.caption:

        # Get the messgae id of the "Generating promotional image..." message
        tooltip_id = bot.send_message(message.chat.id, "Generating image...").message_id

        # Get the file ID of the largest photo
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file_url = f'https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}'

        # Download the image
        response = requests.get(file_url)
        image = BytesIO(response.content)

        # Save the image temporarily
        with open('temp_image.jpg', 'wb') as f:
            f.write(image.getbuffer())

        # Generate the promotional image
        generate_image(message.caption, 'temp_image.jpg', 'output.png')

        # Resize the image if necessary
        resized_image = resize_image('output.png')

        # Delete the "Generating image..." message
        bot.delete_message(message.chat.id, tooltip_id)

        # Send the resized image back to the user
        bot.send_photo(message.chat.id, resized_image)

        # Clean up temporary files
        os.remove('temp_image.jpg')
        os.remove('output.png')
    else:
        bot.reply_to(message, "Please provide a caption with the image.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Please send an image with a caption.")

if __name__ == "__main__":
    print("Bot is running...")
    bot.polling()
