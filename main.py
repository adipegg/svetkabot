from distutils.cmd import Command
import os
import random
import telebot #имопрт библиотеки для тг бота
from telebot import types


bot = telebot.TeleBot('5353490647:AAGpW1u2Li4GIikWN1US0mW8EYlvy5Ttb24') #добавление уникального токена бота

def f (message):
    return message.text.lower() == 'привет'

@bot.message_handler(func = f)
def start (message):
    bot.send_message(message.chat.id, 'Салам! Меня зовут Светалана и я замужем. Если хочешь написать мне, то напиши команды а не подкатывай яйцами.', parse_mode='html')

def da (message):
    return message.text.lower() == 'да'

@bot.message_handler(func = da)
def pussy (message):
    bot.send_message(message.chat.id, 'Пизда.', parse_mode='html')

def how (message):
    return message.text.lower() == 'как дела?'

@bot.message_handler(func = how)
def affairs (message):
    bot.send_message(message.chat.id, 'C точки зрения банальной эрудиции игнорирую критерии утопического субъекта, решаю проблему усовершенствования формирующих геотрансплантационных квазипузлистатов всех кинетически коррелирующих аспектов, а так нормально.', parse_mode='html')

#ответ бота на команду стикеры 
@bot.message_handler(commands=['stickers'])
def commands(message):
    sti = open('stickers/' + random.choice(os.listdir('stickers')), 'rb')
    bot.send_sticker(message.chat.id, sti)

#ответ бота на команду пасхалка
def pas (message):
    return message.text.lower() == 'пасхалка'
@bot.message_handler(func = pas)
def vlad (message):
    sti = open('vlad.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)

def leg (message):
    return message.text.lower() == 'скинь ножки'
@bot.message_handler(func = leg)
def gay (message):
    video = open('gay.mp4', 'rb')
    bot.send_video(message.chat.id, video)

#ответ бота на команду секрет
@bot.message_handler(commands=['secret'])
def commands(message):
    sti = open('secret.wav', 'rb')
    bot.send_audio(message.chat.id, sti)

#задаём переменную которая открывает txt файл с анекдотами
jokes = open('./Jokes.txt', 'r')
joke_mean = jokes.read().split('/')
jokes.close()

#ответ бота на команду joke
@bot.message_handler(commands = ['joke'])
def joke(message):
    bot.send_message(message.chat.id, random.choice(joke_mean), parse_mode='html')

music_rock = open('./Music_rock.txt', 'r')
music_rock_mean = music_rock.read().split('/')
music_rock.close()

music_electro = open('./Music_electro.txt', 'r')
music_electro_mean = music_electro.read().split('/')
music_electro.close()

music_rap = open('./Music_rap.txt', 'r')
music_rap_mean = music_rap.read().split('/')
music_rap.close()

music_phonk = open('./Music_phonk.txt', 'r')
music_phonk_mean = music_phonk.read().split('/')
music_phonk.close()

music_techno = open('./Music_techno.txt', 'r')
music_techno_mean = music_techno.read().split('/')
music_techno.close()

game_fps = open('./FPS.txt', 'r')
game_fps_mean = game_fps.read().split('/')
game_fps.close()

games_fanta = open('./fanta.txt', 'r')
games_fanta_mean = games_fanta.read().split('/')
games_fanta.close()

games_MOBA = open('./MOBA.txt', 'r')
games_MOBA_mean = games_MOBA.read().split('/')
games_MOBA.close()

games_RPG = open('./RPG.txt', 'r')
games_RPG_mean = games_RPG.read().split('/')
games_RPG.close()

games_strat = open('./strat.txt', 'r')
games_strat_mean = games_strat.read().split('/')
games_strat.close()

games_sands = open('./sands.txt', 'r')
games_sands_mean = games_sands.read().split('/')
games_sands.close()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🎵Music")
    btn2 = types.KeyboardButton("🕹Games")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот Светка, создана чтобы ты написал мне команду, а я оптравлю тебе что ты захочешь:)".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "🎵Music"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Техно🎉")
        btn2 = types.KeyboardButton("Рок🤟")
        btn3 = types.KeyboardButton("Електронная⚡")
        btn4 = types.KeyboardButton("Фонк🚗")
        btn5 = types.KeyboardButton("Рэп🎧")
        back = types.KeyboardButton("Вернуться в главное меню🔙")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="Выберите один из предлагаемых жанров музыки:", reply_markup=markup)
    elif(message.text == "🕹Games"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Шутер🔫")
        btn2 = types.KeyboardButton("Фэнтези🪄")
        btn3 = types.KeyboardButton("MOBA🗺")
        btn4 = types.KeyboardButton("RPG⚒")
        btn5 = types.KeyboardButton("Стратегия🧠")
        btn6 = types.KeyboardButton("Песочница🤪")
        back = types.KeyboardButton("Вернуться в главное меню🔙")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text="Выберите один из предлагаемых жанров игры:", reply_markup=markup)
    
    elif message.text.lower() == 'техно🎉':
            bot.send_message(message.chat.id, random.choice(music_techno_mean), parse_mode='html')
    elif message.text.lower() == 'рок🤟':
            bot.send_message(message.chat.id, random.choice(music_rock_mean), parse_mode='html')
    elif message.text.lower() == 'електронная⚡':
            bot.send_message(message.chat.id, random.choice(music_electro_mean), parse_mode='html')
    elif message.text.lower() == 'фонк🚗':
            bot.send_message(message.chat.id, random.choice(music_phonk_mean), parse_mode='html')
    elif message.text.lower() == 'рэп🎧':
            bot.send_message(message.chat.id, random.choice(music_rap_mean), parse_mode='html')
    elif message.text.lower() == 'шутер🔫':
            bot.send_message(message.chat.id, random.choice(game_fps_mean), parse_mode='html')
    elif message.text.lower() == 'фэнтези🪄':
            bot.send_message(message.chat.id, random.choice(games_fanta_mean), parse_mode='html')
    elif message.text.lower() == 'moba🗺':
            bot.send_message(message.chat.id, random.choice(games_MOBA_mean), parse_mode='html')
    elif message.text.lower() == 'rpg⚒':
            bot.send_message(message.chat.id, random.choice(games_RPG_mean), parse_mode='html') 
    elif message.text.lower() == 'стратегия🧠':
            bot.send_message(message.chat.id, random.choice(games_strat_mean), parse_mode='html')
    elif message.text.lower() == 'песочница🤪':
            bot.send_message(message.chat.id, random.choice(games_sands_mean), parse_mode='html') 
    
    elif (message.text == "Вернуться в главное меню🔙"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("🎵Music")
        button2 = types.KeyboardButton("🕹Games")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Я не знаю как ответить на это...")    
        
bot.polling(none_stop=True) #грубо говоря запуск бота