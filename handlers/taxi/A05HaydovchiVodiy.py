from aiogram.types import CallbackQuery, Message
from utils.massiv.allCustomer import inCustomer
from utils.massiv.allCustomer import inDriver
from handlers.taxi.A06HaydovchiQayerTuman import HaydovchiQayerTuman
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


async def HaydovchiVodiy(callback: CallbackQuery, category, **kwargs):

    for Driver in inDriver:
        if Driver["tg_id"] == callback["from"]["id"]:
            for vdtsh in vodiyTashkent:
                if vdtsh['val'] == category:
                    Driver["vodiyTashkent"] = category
                    cat = category
                else:
                    cat = Driver["vodiyTashkent"]

            if cat == "vodiy":
                markup = await Haydovchivodiy(4)
                await callback.message.edit_text(text='Qaysi Tumanga Bormoqchisiz ?', reply_markup=markup)

            elif cat == "tashkent":
                await HaydovchiQayerTuman(callback, category)
        else:
            # await MijozVodiy(callback, category)
            pass

    for cs in inCustomer:
        if cs["tg_id"] == callback["from"]["id"]:
            for vdtsh in vodiyTashkent:
                if vdtsh['val'] == category:
                    cs["vodiyTashkent"] = category
                    cat = category
                else:
                    cat = cs["vodiyTashkent"]

            if cat == "vodiy":
                markup = await Haydovchivodiy(4)
                await callback.message.edit_text(text='Qaysi Tumanga Bormoqchisiz ?', reply_markup=markup)

            elif cat == "tashkent":
                await HaydovchiQayerTuman(callback, category)
        else:
            # await MijozVodiy(callback, category)
            pass
