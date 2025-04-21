from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

TOKEN = "7973886164:AAGYp6TAAQ_WfES8FMUxl5AoIFDU53_v7a8"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Главное меню
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(KeyboardButton("🔗 Discord"), KeyboardButton("🛒 Магазин"))
main_kb.add(KeyboardButton("🧠 О нас"), KeyboardButton("🧾 Правила"))
main_kb.add(KeyboardButton("📢 Апдейты"), KeyboardButton("💬 Обратная связь"))

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Добро пожаловать в 43 Squad!", reply_markup=main_kb)

@dp.message_handler(lambda message: message.text == "🔗 Discord")
async def send_discord(message: types.Message):
    await message.answer("Вот ссылка на наш Discord: https://dsc.gg/43sq")

@dp.message_handler(lambda message: message.text == "🛒 Магазин")
async def send_shop(message: types.Message):
    await message.answer("Наш магазин: https://shop.43sq.dev (или твоя ссылка)")

@dp.message_handler(lambda message: message.text == "🧠 О нас")
async def about_us(message: types.Message):
    await message.answer("Мы — 43 Squad. Комьюнити для своих. Поддержка, ивенты, актив.")

@dp.message_handler(lambda message: message.text == "🧾 Правила")
async def rules(message: types.Message):
    await message.answer("1. Уважай других\n2. Не флуди\n3. Без токсичности\n(добавь свои пункты)")

@dp.message_handler(lambda message: message.text == "📢 Апдейты")
async def updates(message: types.Message):
    await message.answer("Пока апдейтов нет. Скоро будет 🔥")

@dp.message_handler(lambda message: message.text == "💬 Обратная связь")
async def feedback(message: types.Message):
    await message.answer("Напиши свои предложения сюда: @твой_ник или в Discord")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
