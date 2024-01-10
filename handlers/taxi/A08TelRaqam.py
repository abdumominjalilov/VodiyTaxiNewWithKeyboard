from aiogram.types import CallbackQuery, Message
from utils.massiv.allCustomer import inCustomer
from utils.massiv.allCustomer import inDriver
from keyboards.inline.keyboard_info import haydovchiMijoz, mashina, kishisoni, qayerQatnov, vodiyTashkent, vodiy, andijon, fargona, namangan, toshkent
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
from states.infoUser import PersonalData


async def HaydovchiTelefonRaqam(callback: CallbackQuery, category, **kwargs):
    for Driver in inDriver:
        if Driver["tg_id"] == callback["from"]["id"]:
            for ksh in kishisoni:
                if ksh['val'] == category:
                    Driver["kishisoni"] = category

    for customer in inCustomer:
        if customer["tg_id"] == callback["from"]["id"]:
            for ksh in kishisoni:
                if ksh['val'] == category:
                    customer["kishisoni"] = category
    # await callback.message.edit
    await callback.message.delete()
    await PersonalData.fullName.set()
    await callback.message.answer("Ismingiz?\n 👇👇👇 Pastga Yozing 👇👇👇")
