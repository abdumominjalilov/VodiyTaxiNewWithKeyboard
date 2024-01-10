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

async def HaydovchiNechaKishi(callback: CallbackQuery, category, **kwargs):
    for Driver in inDriver:
        if Driver["tg_id"] == callback["from"]["id"]:
            for ad in andijon:
                if ad['val'] == category:
                    Driver["QayerTuman"] = category
            for fm in fargona:
                if fm['val'] == category:
                    Driver["QayerTuman"] = category
            for nm in namangan:
                if nm['val'] == category:
                    Driver["QayerTuman"] = category
            for tsh in toshkent:
                if tsh['val'] == category:
                    Driver["QayerTuman"] = category
            else:
                pass

    for customer in inCustomer:
        if customer["tg_id"] == callback["from"]["id"]:
            for ad in andijon:
                if ad['val'] == category:
                    customer["QayerTuman"] = category
            for fm in fargona:
                if fm['val'] == category:
                    customer["QayerTuman"] = category
            for nm in namangan:
                if nm['val'] == category:
                    customer["QayerTuman"] = category
            for tsh in toshkent:
                if tsh['val'] == category:
                    customer["QayerTuman"] = category
            else:
                pass
    for x in inDriver:
        if Driver["tg_id"] == callback["from"]["id"]:
            print(Driver)
    markup = await Haydovchikishisoni(6)

    # Xabar matnini o'zgartiramiz va keyboardni yuboramiz
    await callback.message.edit_text(text='Necha Kishi ?', reply_markup=markup)

