from typing import Union
from utils.massiv.allCustomer import inCustomer
from utils.massiv.allCustomer import inDriver
from aiogram import types
from aiogram.types import CallbackQuery, Message
from utils.db_api.DataBase import get_product
from states.infoUser import PersonalData
from keyboards.inline.keyboard_info import mashina, kishisoni, qayerQatnov, vodiyTashkent, vodiy, andijon, fargona, namangan, toshkent
from loader import dp

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


async def MijozQayerga(callback: CallbackQuery, category, **kwargs):
    print("Mijozismi")


async def MijozVodiy(callback, category, **kwargs):

    for cs in inCustomer:
        if cs["tg_id"] == callback["from"]["id"]:
            for vdtsh in vodiyTashkent:
                if vdtsh['val'] == category:
                    cs["vodiyTashkent"] = category
                    cat = category
                    print("teng")
            else:
                cat = cs["vodiyTashkent"]
                print("hato")

    if cat == "vodiy":
        markup = await Haydovchivodiy(15)
        await callback.message.edit_text(text='Qaysi Tumanga Bormoqchisiz ?', reply_markup=markup)

    elif cat == "tashkent":
        for Driver in inCustomer:
            if Driver["tg_id"] == callback["from"]["id"]:
                Driver["QayerViloyat"] = "tashkent"
        markup = await Haydovchiqayertuman(20)
        await callback.message.edit_text(text='Toshkentning Qayeriga Bormoqchisiz ?', reply_markup=markup)


async def MijozTuman(callback, category, **kwargs):

    for cs in inCustomer:
        if cs["tg_id"] == callback["from"]["id"]:
            for vd in vodiy:
                if vd['val'] == category:
                    cs["QayerViloyat"] = category
                    cat = category
            else:
                cat = cs["QayerViloyat"]

    if cat == "andijon":
        markup = await Haydovchiqayertuman(1115)
        await callback.message.edit_text(text='Andijonning Qayeriga Bormoqchisiz ?', reply_markup=markup)

    elif cat == "frmg":
        markup = await Haydovchiqayertuman(1116)
        await callback.message.edit_text(text='Farg\'onaning Qayeriga Bormoqchisiz ?', reply_markup=markup)

    elif cat == "namangan":
        markup = await Haydovchiqayertuman(1117)
        await callback.message.edit_text(text='Namanganning Qayeriga Bormoqchisiz ?', reply_markup=markup)
    elif cat == "tashkent":
        for Driver in inDriver:
            if Driver["tg_id"] == callback["from"]["id"]:
                Driver["QayerViloyat"] = "tashkent"
        markup = await Haydovchiqayertuman(20)
        await callback.message.edit_text(text='Toshkentning Qayeriga Bormoqchisiz ?', reply_markup=markup)

    else:
        print('5 da hatolik')

    markup = await Haydovchiqayertuman(20, category)
    await callback.message.edit_text(text='Qayerga Bormoqchisiz ?', reply_markup=markup)


async def MijozNechaKishi(callback: CallbackQuery, category, **kwargs):
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
    # for x in inDriver:
    #     if Driver["tg_id"] == callback["from"]["id"]:
    #         print(Driver)
    markup = await Haydovchikishisoni(6)

    # Xabar matnini o'zgartiramiz va keyboardni yuboramiz
    await callback.message.edit_text(text='Necha Kishi ?', reply_markup=markup)


async def MijozTelefonRaqam(callback: CallbackQuery, **kwargs):
    print("Mijozismi")


async def Mijozismi(callback: CallbackQuery, **kwargs):
    print("Mijozismi")


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
        "10": MijozQayerga,
        "15": MijozVodiy,
        "20": MijozTuman,
        "30": MijozNechaKishi,
        "40": MijozTelefonRaqam,
        "50": Mijozismi,

    }

    # Foydalanuvchidan kelgan Level qiymatiga mos funksiyani chaqiramiz
    current_level_function = levels[current_level]

    # Tanlangan funksiyani chaqiramiz va kerakli parametrlarni uzatamiz
    await current_level_function(
        call, category=category, subcategory=subcategory, item_id=item_id
    )
