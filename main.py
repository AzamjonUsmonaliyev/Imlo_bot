import logging

from aiogram import Bot, Dispatcher, executor, types
from checkWord import checkWords
from transliterate import  to_cyrillic, to_latin

API_TOKEN = '5750065386:AAHsHH5OtFgir61ou300qIcW3vGspKJ1-Lg'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Assalamu alaykum! Uzbekcha , Kirilcha Imlo botimizga xush kelibsiz! ")



@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalamu alaykum! Botdan foydalanish uchun so'z yuboring ! ")


@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text
    word_tr = word
    if word.isascii()!= True:
        word = to_latin(word)

    if len(message.text.split())<2:
        result = checkWords(word)
        if result['available']:
            response = f"✅ {word.capitalize()}"
        else:
            response = f"❌ {word.capitalize()}\n"
            for text in result['matches']:
                response += f"✅ {text.capitalize()} \n"
        if word_tr.isascii()!= True:
            await message.reply(to_cyrillic(response))
        else:
            await message.reply(response)
    else:
        for words in word.split():
            result = checkWords(words)
            if result['available']:
                response = f"✅ {words.capitalize()}"
            else:
                response = f"❌ {words.capitalize()}\n"
                for text in result['matches']:
                    response += f"✅ {text.capitalize()} \n"
            if word_tr.isascii() != True:
                await message.reply(to_cyrillic(response))
            else:
                await message.reply(response)


    # old style:
    # await bot.send_message(message.chat.id, message.text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)