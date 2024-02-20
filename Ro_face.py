import telebot
from deepface import DeepFace

token = '7192693333:AAH-xYJD7QcjJHUs4f0d-VSDthNPgg8w3L0'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """Hello stupid human I will recognize in your strange face your strange emotions. Try me bitch""")
    
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

@bot.message_handler(content_types=['photo'])
def photo(message):
    print ('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    print ('fileID =', fileID)
    file_info = bot.get_file(fileID)
    print ('file.file_path =', file_info.file_path)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    objs = DeepFace.analyze(img_path = "image.jpg", 
            actions = ['age', 'gender', 'race', 'emotion']
    )
    dominant_emotion = objs[0]['dominant_emotion']
    bot.reply_to(message, f'Your dominant emotion is {dominant_emotion}')

bot.infinity_polling()