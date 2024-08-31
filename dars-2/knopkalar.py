from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup

def asosiyknopka():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text='Telefon raqam jonatish', request_contact=True),
        KeyboardButton(text="Lokatsiya jonataish", request_location=True)
    )

    return markup