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


async def HaydovchiFun(callback: CallbackQuery, category, **kwargs):

    cat = category
    for Driver in inDriver:
        if Driver["tg_id"] == callback["from"]["id"]:
            for hm in haydovchiMijoz:
                if hm["val"] == category:
                    Driver["nameCustomer"] = category
                    cat = category
                else:
                    cat = Driver["nameCustomer"]

    for Customer in inCustomer:
        if Customer["tg_id"] == callback["from"]["id"]:
            for hm in haydovchiMijoz:
                if hm["val"] == category:
                    Customer["nameCustomer"] = category
                    cat = category
                else:
                    cat = Customer["nameCustomer"]
    if cat == "driver":
        for Driver in inDriver:
            if Driver["tg_id"] == callback["from"]["id"]:
                pass
            else:
                inDriver.append({
                    "tg_id": callback["from"]["id"],
                    "nameCustomer": "driver",
                    "username": callback["from"]["username"],
                    "firstname": callback["from"]["first_name"],
                    "lastname": callback["from"]["last_name"]
                })

        for Customer in inCustomer:
            if Customer["tg_id"] == callback["from"]["id"]:
                inCustomer.remove(Customer)

        else:
            pass

        markup = await Haydovchiqayerqatnov(1)
        await callback.message.edit_text(text='Qaysi Viloyatga Qatnaysiz ?', reply_markup=markup)


# Customer
    elif cat == "customer":
        for Customer in inCustomer:
            if Customer["tg_id"] == callback["from"]["id"]:
                pass
            else:
                inCustomer.append({
                    "tg_id": callback["from"]["id"],
                    "nameCustomer": "customer",
                    "username": callback["from"]["username"],
                    "firstname": callback["from"]["first_name"],
                    "lastname": callback["from"]["last_name"]
                })

        for Driver in inDriver:
            if Driver["tg_id"] == callback["from"]["id"]:
                print(Driver)
                inDriver.remove(Driver)
            else:
                pass

        markup = await Haydovchiqayerga(13)
        txt = f'Qayerga Bormoqchisiz ?'
        await callback.message.edit_text(text=txt, reply_markup=markup)
    else:
        print("HaydovchiFun da hatolik", inCustomer, inDriver)
