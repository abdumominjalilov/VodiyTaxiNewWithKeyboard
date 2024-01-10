import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_keyboard import menu
from utils.db_api.DataBase import add_product, delete_products, get_categories, get_products, get_product


from loader import dp
from data.config import ADMINS


@dp.message_handler(text="/set")
async def bot_start(message: types.Message):
    await add_product(
        1,
        "food",
        "🍒 Oziq-ovqat",
        "tea",
        "🍵 Choy",
        "Ahmad Tea. Earl Grey",
        "https://ahmadtea.my/wp-content/uploads/2020/08/AHMA-BlackTeas-Earl-Grey-100tb-GT.png",
        10,
        "Ahmad choy",
    )
    await add_product(
        2,
        "food",
        "🍒 Oziq-ovqat",
        "tea",
        "🍵 Choy",
        "Ahmad Tea. English Brekafast",
        "https://dibaonline.de/media/image/product/196/lg/ahmad-tea-english-breakfast-500g-loose-leaf-tea.png",
        20,
    )
    await add_product(
        3,
        "food",
        "🍒 Oziq-ovqat",
        "coffee",
        "☕ Kofe",
        "Nescafe Gold",
        "https://www.nescafe.com/mt/sites/default/files/2020-07/nescafe-gold-blend-jar-front-pitch.png",
        15,
        "Discover our signature smooth, rich instant coffee. Coffee connoisseurs will appreciate the well-rounded taste and rich aroma in every cup. Our expertly crafted blend is great for all coffee drinking occasions, whenever you want to make a moment special. So why not relax, enjoy the now and savour the distinctive taste of this premium blend.",
    )
    await add_product(
        4,
        "food",
        "🍒 Oziq-ovqat",
        "milk",
        "🥛 Sut",
        "Nestle Sut. 1L",
        "https://100comments.com/wp-content/uploads/2017/03/nestle-just-milk-low-fat.jpg",
        2,
    )
    await add_product(
        5,
        "electronics",
        "🖥️ Elektronika",
        "phone",
        "📱 Telefonlar",
        "iPhone 13",
        "https://9to5mac.com/wp-content/uploads/sites/6/2021/09/iphone-13-pro-max-tidbits-9to5mac.jpg",
        1000,
        "Yangi iPhone 13",
    )
    await add_product(
        6,
        "electronics",
        "🖥️ Elektronika",
        "laptop",
        "💻 Noutbuklar",
        "macBook Air",
        "https://checheelectronics.co.ke/wp-content/uploads/2021/06/NL244a1b_2.jpg",
        1600,
    )
    product = await get_categories()
    print(product, "Mahsulotlar Qoshildi /set ishladi")
    await message.answer(
        "Mahsulotlar Qoshildi"
    )

    # ADMINGA xabar beramiz
    # count = await count_users()
    # msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    # await bot.send_message(chat_id=ADMINS[0], text=msg)
