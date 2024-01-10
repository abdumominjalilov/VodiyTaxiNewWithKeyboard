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


async def HaydovchiQayerga(callback: CallbackQuery, category, **kwargs):
    for Driver in inDriver:
        if Driver["tg_id"] == callback["from"]["id"]:
            for msh in mashina:
                if msh['val'] == category:
                    Driver["mashina"] = category
            markup = await Haydovchiqayerga(3)
            await callback.message.edit_text(text='Qayerga Bormoqchisiz ?', reply_markup=markup)

    for cs in inCustomer:
        if cs["tg_id"] == callback["from"]["id"]:
            markup = await Haydovchiqayerga(13)
            txt = f'Qayerga Bormoqchisiz ?'
            await callback.message.edit_text(text=txt, reply_markup=markup)
