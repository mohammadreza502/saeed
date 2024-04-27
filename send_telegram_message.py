import asyncio
from telegram import Bot

# توکن ربات تلگرام خود را وارد کنید
TOKEN = '6729905797:AAGcfb5YqJs1u6smfEvIbOJ3V68idMbccFI'

# آیدی کانال مورد نظر را وارد کنید (باید با @ شروع شود)
CHANNEL_ID = '@mamanesaeed'

# متن پیامی که می‌خواهید ارسال شود
MESSAGE = 'امروزم کس ننت سعید'

async def send_message_to_channel():
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHANNEL_ID, text=MESSAGE)

if __name__ == "__main__":
    asyncio.run(send_message_to_channel())
