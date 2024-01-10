from aiogram.types import CallbackQuery, Message
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
async def HaydovchiMashina(callback: CallbackQuery, category, **kwargs):

    for Driver in inDriver:
        if Driver["tg_id"] == callback["from"]["id"]:
            for qq in qayerQatnov:
                if qq['val'] == category:
                    Driver["qayerQatnov"] = category

    markup = await Haydovchimashina(2)
    await callback.message.edit_text(text='Mashinangiz Qanaqa ?', reply_markup=markup)
