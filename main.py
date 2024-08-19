from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # print("sss")
    # print(update.effective_chat)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hellloooo! {update.effective_chat.first_name}")

if __name__ == '__main__':

    application = ApplicationBuilder().token('7381061596:AAH-TXqJh-qxeRHohNa13eN2y1X5w-jncd0').build()
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.run_polling(allowed_updates='sala salam')
