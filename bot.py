from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.webhook import SendMessage
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Главное меню — без "Правила"
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(KeyboardButton("🔗 Discord"), KeyboardButton("🛒 Магазин"))
main_kb.add(KeyboardButton("🧠 О нас"), KeyboardButton("📢 Апдейты"))
main_kb.add(KeyboardButton("💬 Обратная связь"))

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    return SendMessage(message.chat.id, "Добро пожаловать в 43 Squad!", reply_markup=main_kb)

@dp.message_handler(lambda msg: msg.text == "🔗 Discord")
async def discord_link(message: types.Message):
    return SendMessage(message.chat.id, "Ссылка: https://dsc.gg/43sq")

@dp.message_handler(lambda msg: msg.text == "🛒 Магазин")
async def shop(message: types.Message):
    return SendMessage(message.chat.id, "Магазин: https://shop.43sq.dev")

@dp.message_handler(lambda msg: msg.text == "🧠 О нас")
async def about(message: types.Message):
    return SendMessage(message.chat.id, "43 Squad — комьюнити для своих. Игры, движ, чат.")

@dp.message_handler(lambda msg: msg.text == "📢 Апдейты")
async def updates(message: types.Message):
    return SendMessage(message.chat.id, "Скоро апдейты 🔥")

@dp.message_handler(lambda msg: msg.text == "💬 Обратная связь")
async def feedback(message: types.Message):
    return SendMessage(message.chat.id, "Пиши в Telegram: @твой_ник или в Discord")
