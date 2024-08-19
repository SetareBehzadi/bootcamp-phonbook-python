from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    job = context.job
    await context.bot.send_message(job.chat_id, text=f"Beep! {job.data} seconds are over!")

async def set_timer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_message.chat_id
    due = float(context.args[0])
    context.job_queue.run_once(alarm, due, chat_id=chat_id, name=str(chat_id), data=due)


if __name__ == "__main__":
    token = "7381061596:AAH-TXqJh-qxeRHohNa13eN2y1X5w-jncd0"
    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler("set", set_timer))
    application.run_polling()