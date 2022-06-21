import telebot
from telebot import*

bot = telebot.TeleBot('5353490647:AAGpW1u2Li4GIikWN1US0mW8EYlvy5Ttb24')

#музыка
@bot.message_handler(commands = ['музыка'])
def start(message):   
    if message.text == 'Реп':
        audio = 'Сплин - Топай; Сплин - Танцуй; Nirvana - Smells Like Teen Spirit; Metallica - Entered Sandman; Rammsterin - Du hast; Rammstein - LOS; Metallica - The Unforgiven; Metallica - Sad But True'
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'Инструментальная':
        audio = 'Inside; MetaLove; Serenity; Nagotashi; Дыши'        
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'Рок':
        audio = 'ХАГИ ВАГИ; Малиновый закат; Валим; Кайфуй; Моя игра'
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'Електрон':
        audio = 'daft punk harder better faster stronger; coffin dance'
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'Фонк':
        audio = 'Tokyo Drift Phonk; BORN FOR SPACE; You'
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'Гачи':
        audio = open('Gachimuchi_-_KOZHANYJJ_TRAKTOR_66184053.mp3', 'fem.love - 1000-7 【RIGHT VERSION】♂ Gachi Remix.mp3', 'Slava Marlow - Slava Marlow - Camry 3.5 (prod. Rat TV).mp3', 'Razor_Shot_-_YUnost_v_sapogakh_Gachi_Version_Gachimuchi_remiks_67003631.mp3')
        bot.send_audio(message.chat.id, audio)



@bot.message_handler(commands = ['игры'])
def start(message):
    if message.text == 'FPS(Шутер)':
        game = 'CS:GO; Call of Duty; Doom; FarCry; Overwatch'
        bot.send_game(message.chat.id, game)
    elif message.text == 'Фэнтези':
        game = 'Ведьмак; Skyrim; Dark Souls; Game of Thrones'
        bot.send_game(message.chat.id, game)
    elif message.text == 'MOBA':
        game = 'Dota 2; League of legends; Smite'
        bot.send_game(message.chat.id, game)
    elif message.text == 'RPG':
        game = 'WoW; Red Dead Redemption 2; Dark Souls 3'
        bot.send_game(message.chat.id, game)
    elif message.text == 'Стратегия':
        game = 'Spore; Terraria; Fallout: New Vegas'
        bot.send_game(message.chat.id, game)
    elif message.text == 'Симулятор':
        game = 'Microsoft Flight Simulator (2020); World of Tanks; Jurassic World Evolution 2'
        bot.send_game(message.chat.id, game)


bot.polling(none_stop = True) 