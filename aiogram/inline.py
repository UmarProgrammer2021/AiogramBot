from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

uzb=InlineKeyboardButton('Ozbek tili',callback_data='uz')
rus=InlineKeyboardButton('Rus tili',callback_data='ru')
kanal=InlineKeyboardButton('Kanal',url='https://t.me/hajime_miyagi2022')
chat=InlineKeyboardButton('yuborish',switch_inline_query_current_chat='https://t.me/python_2group')

natija3=InlineKeyboardMarkup().add(uzb,rus,chat).insert(kanal)