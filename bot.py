import telebot
from config import token
from telebot import util

bot = telebot.TeleBot(token)


class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
    
    def info(self):
        return f"Машина {self.brand} цвета {self.color}"


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправь мне фото, и я его обработаю.")


@bot.message_handler(commands=['start_car'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Используй команду /car цвет марка, чтобы создать машину.")

@bot.message_handler(commands=['car'])
def handle_car(message):

    args = util.extract_arguments(message.text).split()
    
    if len(args) < 2:
        bot.reply_to(message, "Пожалуйста, укажите цвет и марку машины. Пример: /car красный BMW")
        return

    color = args[0]
    brand = args[1]

    
    car = Car(color, brand)

    
    bot.reply_to(message, car.info())

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    
    photo = message.photo[-1]  
    file_id = photo.file_id

    
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    
    file_name = f"{file_id}.jpg"
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    
    bot.reply_to(message, f"Фото получено и сохранено как {file_name}")




bot.infinity_polling()
