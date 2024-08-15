from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}')
    print(message)


@router.message(F.text == "1")
async def test(message=Message):
    await message.answer(message.from_user.last_name)
    print(message)
