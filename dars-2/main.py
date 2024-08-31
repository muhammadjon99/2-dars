from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from knopkalar import asosiyknopka
from geopy.distance import distance

bottoken = '7101094041:AAHefUTFkV9OOtEt9qPLXEM3DpiEgF_tAGs'
bot = Bot(bottoken)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    await message.reply('Xush kelibsiz', reply_markup=asosiyknopka())
    chatid = message.chat.id
    print(chatid)

@dp.message_handler(content_types='contact')
async def getcontact(message: Message):
    chatid = message.chat.id
    phone = message.contact.phone_number
    name = message.contact.first_name
    await bot.send_contact(chat_id=chatid, phone_number=phone, first_name=name)



@dp.message_handler(content_types='location')
async def getlocation(message: Message):
    chatid = message.chat.id
    lat = message.location.latitude
    long = message.location.longitude

    itcenterlat = 40.460604
    itcenterlong = 71.2122335
    masofa = distance((lat, long), (itcenterlat, itcenterlong)).km
    masofa = round(masofa, 3)
    await message.reply(f'Masofa: {masofa} km')


    await bot.send_location(chat_id=chatid, latitude=itcenterlat, longitude=itcenterlong)
    await bot.send_location(chat_id=6829390664, latitude=lat, longitude=long)



executor.start_polling(dp, skip_updates=True)