from typing import Union
from aiogram.types import CallbackQuery, Message
from keyboards.inline.menu_keyboards import (
    menu_cd,
    Haydovchimijoz,
    Haydovchi,
    Haydovchikishisoni,
    Haydovchimashina,
    Haydovchiqayerqatnov,
    Haydovchiqayerga,
    Haydovchiqayertuman,
    Haydovchivodiy,
)
async def HaydovchiMijoz(message: Union[CallbackQuery, Message], **kwargs):
    markup = await Haydovchimijoz(0)

    # Xabar matnini o'zgartiramiz va keyboardni yuboramiz
    # Agar foydalanuvchidan Message kelsa Keyboardni yuboramiz
    if isinstance(message, Message):
        await message.answer("Kerakli Bo'lim Tanlang", reply_markup=markup)

    # Agar foydalanuvchidan Callback kelsa Callback natbibi o'zgartiramiz
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_text(text="Kerakli Bo'lim Tanlang", reply_markup=markup)

