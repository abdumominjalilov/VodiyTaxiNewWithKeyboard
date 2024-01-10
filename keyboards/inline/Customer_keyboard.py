
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.keyboard_info import hdkryl, qayerQatnov, haydovchiynl

# customer_key = CallbackData(
#     "daraja", "info", "category", "subcategory", "item_id")
menu_c = CallbackData("show_menu", "daraja", "category",
                       "subcategory", "item_id")

# def make_callback_data(daraja=0, info=0, category=0, subcategory=0, item_id=0):
#     return customer_key.new(daraja=daraja, info=info, category=category, subcategory=subcategory, item_id=item_id)
def make_callback_data(daraja=20, category="0", subcategory="0", item_id="0"):
    return menu_c.new(
        daraja=daraja, category=category, subcategory=subcategory, item_id=item_id
    )

async def HaydovchiKorishYlkey(val):
    lev = val
    markup = InlineKeyboardMarkup(row_width=2)

    hymj = hdkryl

    for HM in hymj:
        callback_data = make_callback_data(
            daraja=lev + 1, category=HM['val'])
        markup.insert(
            InlineKeyboardButton(text=HM['text'],
                                 callback_data=callback_data)
        )
    return markup


async def QaysiHdkey(val):
    lev = val
    markup = InlineKeyboardMarkup(row_width=2)

    hymj = qayerQatnov

    for HM in hymj:
        callback_data = make_callback_data(
            daraja=lev + 1, category=HM['val'])
        markup.insert(
            InlineKeyboardButton(text=HM['text'],
                                 callback_data=callback_data)
        )
    markup.row(
        InlineKeyboardButton(
            text="⬅️Ortga", callback_data=make_callback_data(daraja=lev - 1)
        )
    )
    return markup


async def HaydovchiTugatishkey(val):
    lev = val
    markup = InlineKeyboardMarkup(row_width=2)

    hymj = haydovchiynl

    for HM in hymj:
        callback_data = make_callback_data(
            daraja=lev + 1, category=HM['val'])
        markup.insert(
            InlineKeyboardButton(text=HM['text'],
                                 callback_data=callback_data)
        )
   
    return markup
