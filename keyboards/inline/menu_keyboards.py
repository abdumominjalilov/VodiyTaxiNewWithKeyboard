import logging

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from utils.db_api.DataBase import get_categories, count_products, get_subcategories, get_products
from keyboards.inline.keyboard_info import andijon, haydovchiMijoz, vodiyTashkent, vodiy, fargona, namangan, toshkent, mashina, kishisoni, qayerQatnov



# Turli tugmalar uchun CallbackData-obyektlarni yaratib olamiz
menu_cd = CallbackData("show_menu", "level", "category",
                       "subcategory", "item_id")
buy_item = CallbackData("buy", "item_id")


# Quyidagi funksiya yordamida menyudagi har bir element uchun calbback data yaratib olinadi
# Agar mahsulot kategoriyasi, ost-kategoriyasi va id raqami berilmagan bo'lsa 0 ga teng bo'ladi
def make_callback_data(level, category="0", subcategory="0", item_id="0"):
    return menu_cd.new(
        level=level, category=category, subcategory=subcategory, item_id=item_id
    )
## 0 Haydovchimijoz
## 1 Haydovchiqayerqatnov \\\
## 2 Haydovchi             \\\
## 3 Haydovchimashina       \\\
## 4 Haydovchiqayerga
## 5 Haydovchivodiy
## 6 Haydovchiqayertuman
## 7 Haydovchikishisoni

async def Haydovchimijoz(val):
    lev = val
    markup = InlineKeyboardMarkup(row_width=2)

    hymj = haydovchiMijoz

    for HM in hymj:
        callback_data = make_callback_data(
            level=lev + 1, category=HM['val'])
        markup.insert(
            InlineKeyboardButton(text=HM['text'],
                                 callback_data=callback_data)
        )
    return markup


async def Haydovchiqayerqatnov(val):
    lev = val
    markup = InlineKeyboardMarkup(row_width=1)

    for qq in qayerQatnov:
        callback_data = make_callback_data(
            level=lev + 1, category=qq['val'])
        markup.insert(
            InlineKeyboardButton(text=qq['text'],
                                 callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(
            text="⬅️Ortga", callback_data=make_callback_data(level=lev - 1)
        )
    )
    return markup
    # return markup


async def Haydovchi(val):
    lev = val
    markup = InlineKeyboardMarkup(row_width=1)
    callback_data = make_callback_data(
        level=lev + 1)
    markup.insert(
        InlineKeyboardButton(text="Haydovchiqayerqatnov",
                             callback_data=callback_data)
    )
    markup.row(
        InlineKeyboardButton(
            text="⬅️Ortga", callback_data=make_callback_data(level=val - 1)
        )
    )

    return markup
# Kategoriyalar uchun keyboardyasab olamiz


async def Haydovchimashina(val):
    markup = InlineKeyboardMarkup(row_width=3)
    lev = val
    for msh in mashina:
        callback_data = make_callback_data(
            level=lev + 1, category=msh['val'])
        markup.insert(
            InlineKeyboardButton(text=msh['text'],
                                 callback_data=callback_data)
        )
    markup.row(
        InlineKeyboardButton(
            text="⬅️Ortga", callback_data=make_callback_data(level=val - 1)
        )
    )
    return markup


async def Haydovchiqayerga(val):
    lev = val
    markup = InlineKeyboardMarkup(row_width=1)

    if val == 3:
        for vt in vodiyTashkent:
            callback_data = make_callback_data(
                level=lev + 1, category=vt['val'])
            markup.insert(
                InlineKeyboardButton(text=vt['text'],
                                     callback_data=callback_data)
            )
        markup.row(
            InlineKeyboardButton(
                text="⬅️Ortga", callback_data=make_callback_data(level=lev - 1)
            )
        )
        return markup
    elif val == 13:
        for vt in vodiyTashkent:
            callback_data = make_callback_data(
                level=lev - 9, category=vt['val'])
            markup.insert(
                InlineKeyboardButton(text=vt['text'],
                                     callback_data=callback_data)
            )
        markup.row(
            InlineKeyboardButton(
                text="⬅️Ortga", callback_data=make_callback_data(level=lev - 13)
            )
        )
        return markup


async def Haydovchivodiy(val):
    lev = val

    markup = InlineKeyboardMarkup(row_width=1)
    if val == 4:
        for vd in vodiy:
            callback_data = make_callback_data(
                level=lev + 1, category=vd['val'])
            markup.insert(
                InlineKeyboardButton(text=vd['text'],
                                     callback_data=callback_data)
            )
        markup.row(
            InlineKeyboardButton(
                text="⬅️Ortga", callback_data=make_callback_data(level=lev - 1)
            )
        )
    # elif val == 15:
    #     for vd in vodiy:
    #         callback_data = make_callback_data(
    #             level=lev + 5, category=vd['val'])
    #         markup.insert(
    #             InlineKeyboardButton(text=vd['text'],
    #                                  callback_data=callback_data)
    #         )
    #     markup.row(
    #         InlineKeyboardButton(
    #             text="⬅️Ortga", callback_data=make_callback_data(level=lev - 5)
    #         )
    #     )

    return markup


async def Haydovchiqayertuman(val):
    lev = val
    markup = InlineKeyboardMarkup(row_width=3)

    if val == 115:
        for an in andijon:
            callback_data = make_callback_data(
                level=lev - 109, category=an['val'])
            markup.insert(
                InlineKeyboardButton(text=an['text'],
                                     callback_data=callback_data)
            )
        markup.row(
            InlineKeyboardButton(
                text="⬅️Ortga", callback_data=make_callback_data(level=lev - 111)
            )
        )
    elif val == 116:
        for fr in fargona:
            callback_data = make_callback_data(
                level=lev - 110, category=fr['val'])
            markup.insert(
                InlineKeyboardButton(text=fr['text'],
                                     callback_data=callback_data)
            )
        markup.row(
            InlineKeyboardButton(
                text="⬅️Ortga", callback_data=make_callback_data(level=lev - 112)
            )
        )
    elif val == 117:
        for nm in namangan:
            callback_data = make_callback_data(
                level=lev - 111, category=nm['val'])
            markup.insert(
                InlineKeyboardButton(text=nm['text'],
                                     callback_data=callback_data)
            )
        markup.row(
            InlineKeyboardButton(
                text="⬅️Ortga", callback_data=make_callback_data(level=lev - 113)
            )
        )
    elif val == 5:
        for tsh in toshkent:
            callback_data = make_callback_data(
                level=lev + 1, category=tsh['val'])
            markup.insert(
                InlineKeyboardButton(text=tsh['val'],
                                     callback_data=callback_data)
            )
        markup.row(
            InlineKeyboardButton(
                text="⬅️Ortga", callback_data=make_callback_data(level=lev - 2)
            )
        )
    # elif val == 1115:
    #     for an in andijon:
    #         callback_data = make_callback_data(
    #             level=lev - 1085, category=an['val'])
    #         markup.insert(
    #             InlineKeyboardButton(text=an['text'],
    #                                  callback_data=callback_data)
    #         )
    #     markup.row(
    #         InlineKeyboardButton(
    #             text="⬅️Ortga", callback_data=make_callback_data(level=lev - 1095)
    #         )
    #     )
    # elif val == 1116:
    #     for fr in fargona:
    #         callback_data = make_callback_data(
    #             level=lev - 1086, category=fr['val'])
    #         markup.insert(
    #             InlineKeyboardButton(text=fr['text'],
    #                                  callback_data=callback_data)
    #         )
    #     markup.row(
    #         InlineKeyboardButton(
    #             text="⬅️Ortga", callback_data=make_callback_data(level=lev - 1096)
    #         )
    #     )
    # elif val == 1117:
    #     for nm in namangan:
    #         callback_data = make_callback_data(
    #             level=lev - 1087, category=nm['val'])
    #         markup.insert(
    #             InlineKeyboardButton(text=nm['text'],
    #                                  callback_data=callback_data)
    #         )
    #     markup.row(
    #         InlineKeyboardButton(
    #             text="⬅️Ortga", callback_data=make_callback_data(level=lev - 1097)
    #         )
    #     )
    # elif val == 20:
    #     for tsh in toshkent:
    #         callback_data = make_callback_data(
    #             level=lev + 10, category=tsh['val'])
    #         markup.insert(
    #             InlineKeyboardButton(text=tsh['val'],
    #                                  callback_data=callback_data)
    #         )
    #     markup.row(
    #         InlineKeyboardButton(
    #             text="⬅️Ortga", callback_data=make_callback_data(level=lev - 5, category="u")
    #         )
    #     )
    return markup


async def Haydovchikishisoni(val):
    lev = val
    markup = InlineKeyboardMarkup(row_width=1)
    for ksh in kishisoni:
        callback_data = make_callback_data(
            level=lev + 1, category=ksh['val'])
        markup.insert(
            InlineKeyboardButton(text=ksh['text'],
                                 callback_data=callback_data)
        )
    markup.row(
        InlineKeyboardButton(
            text="⬅️Ortga", callback_data=make_callback_data(level=lev - 1)
        )
    )
    return markup
