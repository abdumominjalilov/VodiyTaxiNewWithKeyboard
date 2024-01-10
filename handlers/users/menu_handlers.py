from aiogram import types
from aiogram.types import CallbackQuery
from keyboards.inline.menu_keyboards import menu_cd
from loader import dp
from handlers.taxi.A00HaydovchiMijoz import HaydovchiMijoz
from handlers.taxi.A01HaydovchiQayerQatnov import HaydovchiFun
from handlers.taxi.A03HaydovchiMashina import HaydovchiMashina
from handlers.taxi.A04HaydovchiQayerga import HaydovchiQayerga
from handlers.taxi.A05HaydovchiVodiy import HaydovchiVodiy
from handlers.taxi.A06HaydovchiQayerTuman import HaydovchiQayerTuman
from handlers.taxi.A07HaydovchiKishiSoni import HaydovchiNechaKishi
from handlers.taxi.A08TelRaqam import HaydovchiTelefonRaqam

# Bosh menyu matni uchun handler


@dp.message_handler(text="Bosh menyu")
async def show_menu(message: types.Message):
    # Foydalanuvchilarga barcha kategoriyalarni qaytaramiz
    await HaydovchiMijoz(message)


# Yuqoridagi barcha funksiyalar uchun yagona handler


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """
    :param call: Handlerga kelgan Callback query
    :param callback_data: Tugma bosilganda kelgan ma'lumotlar
    """

    # Foydalanuvchi so'ragan Level (qavat)
    current_level = callback_data.get("level")

    # Foydalanuvchi so'ragan Kategoriya
    category = callback_data.get("category")

    # Ost-kategoriya (har doim ham bo'lavermaydi)
    subcategory = callback_data.get("subcategory")

    # Mahsulot ID raqami (har doim ham bo'lavermaydi)
    item_id = int(callback_data.get("item_id"))

    # Har bir Level (qavatga) mos funksiyalarni yozib chiqamiz
    levels = {
        "0": HaydovchiMijoz,
        "1": HaydovchiFun,
        "2": HaydovchiMashina,
        "3": HaydovchiQayerga,
        "4": HaydovchiVodiy,
        "5": HaydovchiQayerTuman,
        "6": HaydovchiNechaKishi,
        "7": HaydovchiTelefonRaqam,
        # "8": HaydovchiIsmi,
        # "20": MijozTugatish,
        # "21": MijozHaydovchiKorish,
        # "22": HaydovchiTugatish,
    }

    # Foydalanuvchidan kelgan Level qiymatiga mos funksiyani chaqiramiz
    current_level_function = levels[current_level]

    # Tanlangan funksiyani chaqiramiz va kerakli parametrlarni uzatamiz
    await current_level_function(
        call, category=category, subcategory=subcategory, item_id=item_id
    )
