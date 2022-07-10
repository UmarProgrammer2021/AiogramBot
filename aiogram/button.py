from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton

tugma1=KeyboardButton('Kurslar')
tugma2=KeyboardButton('Manzil')
tugma3=KeyboardButton('Aloqa')
tugma4=KeyboardButton('Bepul darsga yozilish')

natija=ReplyKeyboardMarkup(resize_keyboard=True).row(tugma1,tugma2,tugma4).insert(tugma3)


kurs1=KeyboardButton('Begginer')
kurs2=KeyboardButton('Elementry')
kurs3=KeyboardButton('Intermedit')
kurs4=KeyboardButton('uper-intermedit')
kurs5=KeyboardButton('IELTS')

natija2=ReplyKeyboardMarkup(resize_keyboard=True).add(kurs1,kurs2,kurs3).add(kurs4,kurs5)