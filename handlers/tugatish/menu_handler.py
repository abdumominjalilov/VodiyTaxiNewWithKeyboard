from aiogram import types
from aiogram.types import CallbackQuery
from keyboards.inline.Customer_keyboard import menu_c
from loader import dp
from handlers.tugatish.A00MijozTugatish import MijozTugatish
from handlers.tugatish.A00MijozTugatish import MijozHaydovchiKorish
from handlers.tugatish.A00haydovchiTugatish import HaydovchiTugatish



@dp.callback_query_handler(menu_c.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """
    :param call: Handlerga kelgan Callback query
    :param callback_data: Tugma bosilganda kelgan ma'lumotlar
    """

    # Foydalanuvchi so'ragan Level (qavat)
    darajasi = callback_data.get("daraja")

    # Foydalanuvchi so'ragan Kategoriya
    # info = callback_data.get("info")


    levels = {
        # "0": HaydovchiMijoz,
        # "1": HaydovchiFun,
        # "2": HaydovchiMashina,
        # "3": HaydovchiQayerga,
        # "4": HaydovchiVodiy,
        # "5": HaydovchiQayerTuman,
        # "6": HaydovchiNechaKishi,
        # "7": HaydovchiTelefonRaqam,
        # # "8": HaydovchiIsmi,
        "20": MijozTugatish,
        "21": MijozHaydovchiKorish,
        "22": HaydovchiTugatish,
    }

    # Foydalanuvchidan kelgan Level qiymatiga mos funksiyani chaqiramiz
    current_level_function = levels[darajasi]

    # Tanlangan funksiyani chaqiramiz va kerakli parametrlarni uzatamiz
    await current_level_function(
        call, category=0, subcategory=0, item_id=0
    )
