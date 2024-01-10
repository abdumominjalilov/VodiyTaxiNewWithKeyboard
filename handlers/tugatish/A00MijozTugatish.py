from typing import Union
from aiogram.types import CallbackQuery, Message
from keyboards.inline.Customer_keyboard import HaydovchiKorishYlkey,QaysiHdkey

async def MijozTugatish(message: Union[CallbackQuery, Message], **kwargs):
    markup = await HaydovchiKorishYlkey(20)

    # Xabar matnini o'zgartiramiz va keyboardni yuboramiz
    # Agar foydalanuvchidan Message kelsa Keyboardni yuboramiz
    if isinstance(message, Message):
        await message.answer("Kerakli Bo'lim Tanlang", reply_markup=markup)

    # Agar foydalanuvchidan Callback kelsa Callback natbibi o'zgartiramiz
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_text(text="Kerakli Bo'lim Tanlang", reply_markup=markup)

async def MijozHaydovchiKorish(message: Union[CallbackQuery, Message], **kwargs):
    markup = await QaysiHdkey(21)

    # Xabar matnini o'zgartiramiz va keyboardni yuboramiz
    # Agar foydalanuvchidan Message kelsa Keyboardni yuboramiz
    if isinstance(message, Message):
        await message.answer("Kerakli Bo'lim Tanlang", reply_markup=markup)

    # Agar foydalanuvchidan Callback kelsa Callback natbibi o'zgartiramiz
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_text(text="Kerakli Bo'lim Tanlang", reply_markup=markup)

