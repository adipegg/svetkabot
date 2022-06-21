from distutils.cmd import Command
from http import client
import os
import random
import telebot


bot = telebot.TeleBot('5353490647:AAGpW1u2Li4GIikWN1US0mW8EYlvy5Ttb24')

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет странник', parse_mode='html')

blank_line_regex = r"(?:\r?\n){2,}"

jokes = open('./Jokes.txt', 'r')
joke_mean = jokes.read().split('/')
jokes.close()


@bot.message_handler(commands = ['joke'])
def joke(message):
    bot.send_message(message.chat.id, random.choice(joke_mean), parse_mode='html')

bot.polling(none_stop = True)

