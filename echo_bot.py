import telebot
import requests
import time
#from slackclient import SlackClient
import json


TOKEN = "814710549:AAE-0S2cxpURt8ZP8IWes2SqOlgOaWeCyhA" # telegram token
channelId = 't.me/telegaJokesTes'

slackToken = "xoxp-621302789795-621302789987-632728149556-2bd6e95dfbc936f6f09b23e1be321fa9"
workspace = "testing bot"


bot = telebot.TeleBot(TOKEN)


def botStart(): #send to telegram
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Howdy, how are you doing?")

    while(True):
        response = requests.get('https://official-joke-api.appspot.com/jokes/programming/random').json()
        print(response[0]["setup"] + response[0]["punchline"])

        bot.send_message(chat_id="@telegaJokesTes", text=response[0]["setup"] + " " + response[0]["punchline"])
        time.sleep(600)
    #bot.polling()
    #bot.send_message(channelId,response.content.strip())

# def sendToSlack():
#     sc = SlackClient(slackToken)
#     sc.rtm_send_message(workspace, "test", "1482960137.003543", True)


botStart()