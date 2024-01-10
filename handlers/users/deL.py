import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_keyboard import menu
from utils.db_api.DataBase import drop_products, delete_products


from loader import dp
from data.config import ADMINS


@dp.message_handler(text="/del")
async def bot_start(message: types.Message):
    await delete_products()
    print("Mahsulotlar Ochdi /set ishladi")
    await message.answer(
        "Mahsulotlar Ochdi"
    )

    # ADMINGA xabar beramiz
    # count = await count_users()
    # msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    # await bot.send_message(chat_id=ADMINS[0], text=msg)
