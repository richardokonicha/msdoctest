from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import telebot
# from config import (wcapi, token, debug, webhook_url, bot, telebot)
# from dotenv import load_dotenv
import os

# importdir.do("features", globals())
webhook_url = ""
token = "5410666315:AAEjKnX7OxCEvaJOZ8k5Bq17j8mIsR0vW1Y"
debug = False

# load_dotenv()

app = Flask(__name__)

bot = telebot.TeleBot(
    token,
    threaded=True
)


@bot.message_handler(commands=["start", "Start"])
def start(message):
    userid = message.from_user.id
    bot.send_chat_action(userid, action='typing')
    return bot.send_message(userid,  text="answer")



@app.route('/')
def index():
   print('Request for index page received')
   return ('This is a website.', 200, None)



# @server.route('/', methods=['GET'])
# def index():
#     return ('This is a website.', 200, None)


# @server.route('/monitor/order', methods=['POST'])
# def new_order_hook():
#     request_object = request.stream.read().decode("utf-8")
#     return (request_object, 200, None)


@app.route('/' + token, methods=['POST'])
def getMessage():
    request_object = request.stream.read().decode("utf-8")
    update_to_json = [telebot.types.Update.de_json(request_object)]
    bot.process_new_updates(update_to_json)
    return "got Message bro"

@app.route('/hook')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(webhook_url + token)
    return f"Webhook set to {webhook_url}"


if debug == True:
    bot.remove_webhook()
    bot.polling()
else:
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))