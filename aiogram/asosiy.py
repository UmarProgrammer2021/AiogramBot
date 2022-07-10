from config import *
from aiogram import Bot,Dispatcher,executor,types
from button import *
from inline import *

bot=Bot(token=API_TOKEN)
ab=Dispatcher(bot)

@ab.message_handler(commands=['start','help'])
async def start(message: types.Message):
    ism=message.from_user.first_name

    await message.answer("assalomu aleykum {}".format(ism),reply_markup=natija3)

@ab.message_handler()
async def buttons(message: types.Message):
    if message.text == "Kurslar":
        await message.answer('Bizda quydagi kurslar mavjud',reply_markup=natija2)
    elif message.text=='Manzil':
        await message.answer("Bizning manzil")
        await message.answer_location(41.33477691773244, 69.21545644019866)


@ab.callback_query_handler(lambda a: a.data=='uz')
async def uzbtili(callback_query: types.CallbackQuery):
    bot.asnwer_callback_query=(callback_query.id)
    await bot.send_message(callback_query.from_user.id,'Siz Ozbek tilini tanladingiz ',reply_markup=natija)


if __name__ =="__main__":
    executor.start_polling(ab)