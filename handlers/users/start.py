import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_keyboard import menu
from utils.db_api.DataBase import add_product, delete_products, get_categories, get_products, get_product
from handlers.users.menu_handlers import HaydovchiMijoz
import sys
from loader import dp
from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    
    # try:
    #     user = await add_user(
    #         telegram_id=message.from_user.id,
    #         full_name=message.from_user.full_name,
    #         username=message.from_user.username,
    #     )
    # except asyncpg.exceptions.UniqueViolationError:
    #     user = await select_user(telegram_id=message.from_user.id)

    # product = await get_products("food")
    # print(product, "try")
    # print(sys.get_int_max_str_digits(message))/
    print(sys.getsizeof(message), 'msg')
    print(message['contact'], 'contact')
    await message.answer(
        "Xush kelibsiz! Do'konimizdagi mahsulotlarni ko'rish uchun quyidagi Menu tugmasini bosing",
        reply_markup=menu,
    )
    await HaydovchiMijoz(message)

    # ADMINGA xabar beramiz
    # count = await count_users()
    # msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    # await bot.send_message(chat_id=ADMINS[0], text=msg)
