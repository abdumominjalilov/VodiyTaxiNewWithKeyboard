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


async def HaydovchiQayerTuman(callback: CallbackQuery, category, **kwargs):
    for Driver in inDriver:
        if Driver["tg_id"] == callback["from"]["id"]:
            for vd in vodiy:
                if vd['val'] == category:
                    Driver["QayerViloyat"] = category
                    cat = category
            if category == 'tashkent':
                Driver["QayerViloyat"] = category
                cat = category
            else:
                cat = Driver["QayerViloyat"]
        else:
            pass

    for customer in inCustomer:
        if customer["tg_id"] == callback["from"]["id"]:
            for vd in vodiy:
                if vd['val'] == category:
                    customer["QayerViloyat"] = category
                    cat = category
            if category == 'tashkent':
                customer["QayerViloyat"] = category
                cat = category
            else:
                cat = customer["QayerViloyat"]
    if cat == "andijon":
        markup = await Haydovchiqayertuman(115)
        await callback.message.edit_text(text='Andijonning Qayeriga Bormoqchisiz ?', reply_markup=markup)

    elif cat == "frmg":
        markup = await Haydovchiqayertuman(116)
        await callback.message.edit_text(text='Farg\'onaning Qayeriga Bormoqchisiz ?', reply_markup=markup)

    elif cat == "namangan":
        markup = await Haydovchiqayertuman(117)
        await callback.message.edit_text(text='Namanganning Qayeriga Bormoqchisiz ?', reply_markup=markup)
    elif cat == "tashkent":
        for Driver in inDriver:
            if Driver["tg_id"] == callback["from"]["id"]:
                Driver["QayerViloyat"] = "tashkent"
        for customer in inCustomer:
            if customer["tg_id"] == callback["from"]["id"]:
                customer["QayerViloyat"] = "tashkent"
        markup = await Haydovchiqayertuman(5)
        txt = f'Toshkentning Qayeriga Bormoqchisiz ?'
        await callback.message.edit_text(text=txt, reply_markup=markup)

    else:
        print('5 da hatolik')
    # Xabar matnini o'zgartiramiz va keyboardni yuboramiz
