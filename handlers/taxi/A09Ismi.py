from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states.infoUser import PersonalData


@dp.message_handler(state=PersonalData.fullName)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data({"name": fullname})

    await message.answer("1 Kishiga Necha Pul?\n 👇👇👇 Pastga Yozing 👇👇👇")

    # await PersonalData.email.set()
    await PersonalData.next()


@dp.message_handler(state=PersonalData.yolNarxi)
async def answer_fullname(message: types.Message, state: FSMContext):
    yolNarxi = message.text

    await state.update_data({"yolNarxi": yolNarxi})
    # await message.answer.delete_message()

    await message.answer("Telefon Raqamingizni kiriting\n 👇👇👇 Pastga Yozing 👇👇👇")

    # await PersonalData.email.set()
    await PersonalData.next()


