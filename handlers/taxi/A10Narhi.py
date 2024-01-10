from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states.infoUser import PersonalData
from utils.massiv.allCustomer import inCustomer
from utils.massiv.allCustomer import inDriver
# from keyboards.inline.Customer_keyboard import HaydovchiKorishYl,HaydovchiTugatish
from handlers.tugatish.A00MijozTugatish import MijozTugatish
from handlers.tugatish.A00haydovchiTugatish import HaydovchiTugatish


@dp.message_handler(state=PersonalData.phoneNum)
async def answer_phone(message: types.Message, state: FSMContext):

    print(message.from_user.id)
    for Customer in inCustomer:
        if Customer["tg_id"] == message.from_user.id:
            phone = message.text

            await state.update_data(
                {"phone": phone}
            )
            # Ma`lumotlarni qayta o'qiymiz
            data = await state.get_data()
            name = data.get("name")
            yolNarxi = data.get("yolNarxi")
            phone = data.get("phone")
            await state.finish()
            # markup = await HaydovchiKorishYl(20)

            msg = "Malumotingiz Quyidagi Ko'rinishda Haydovchilarga Yuborildi:\n"
            msg += "\n"
            msg += f"🙎‍♂️ Ismi - \n"
            msg += f"🏚 Manzili - \n"
            msg += f"🔍 Qayeriga - \n"
            msg += f"📞 Telefon: - \n"
            msg += f"💰 Narxi: - \n"
            msg += "\n"
            msg += "Iltimos Haydovchilar Aloqaga CHiqishini Kuting....."
    # await message.answer.delete()

            await message.answer(msg)
            await MijozTugatish(message)
            # await message.answer("Kerakli Bo'lim Tanlang", reply_markup=markup)

    for Driver in inDriver:
        if Driver["tg_id"] == message.from_user.id:
            phone = message.text

            await state.update_data(
                {"phone": phone}
            )
            # Ma`lumotlarni qayta o'qiymiz
            data = await state.get_data()
            name = data.get("name")
            yolNarxi = data.get("yolNarxi")
            phone = data.get("phone")
            await state.finish()
            # markup = await HaydovchiTugatish(21)

            msg = "Quyidagi Mijozlar Bor:\n"
            msg += "\n"
            msg += f"🙎‍♂️ Ismi - \n"
            msg += f"🏚 Manzili - \n"
            msg += f"🔍 Qayeriga - \n"
            msg += f"📞 Telefon: - \n"
            msg += f"💰 Narxi: - \n"
            msg += "\n"
    # await message.answer.delete()

            await message.answer(msg)
            await HaydovchiTugatish(message)
            # await message.answer("Kerakli Bo'lim Tanlang", reply_markup=markup)
