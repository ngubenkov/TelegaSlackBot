import telebot
import requests
import time
import json

TOKEN = "814710549:AAE-0S2cxpURt8ZP8IWes2SqOlgOaWeCyhA"
channelId = 't.me/telegaJokesTes'

bot = telebot.TeleBot(TOKEN)


def botStart():
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Howdy, how are you doing?")
    while(True):
        time.sleep(10)

        response = requests.get('https://official-joke-api.appspot.com/jokes/programming/random').json()
        print(response[0]["setup"] + response[0]["punchline"])

        bot.send_message(chat_id="@telegaJokesTes", text=response[0]["setup"] + response[0]["punchline"])
    #bot.polling()
    #bot.send_message(channelId,response.content.strip())


def jokesAPI():
    response = requests.get("https://webknox-jokes.p.rapidapi.com/jokes/search?category=Chuck+Norris&minRating=5&numJokes=5&keywords=kick%2C+hard",
      headers={
        "X-RapidAPI-Host": "webknox-jokes.p.rapidapi.com",
        "X-RapidAPI-Key": "e5f3bc84bcmsh4ead144aded4d81p1585ccjsnd9e58d1a0d20"
      }
    )
    print(response)

jokesAPI()