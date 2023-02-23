# ###
from aiogram import Bot, Dispatcher, types, executor
from auth.config import API_TOKEN

bot = Bot(API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, text=f"Hello! {message.from_user.first_name}!")
    await message.delete()
    


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
