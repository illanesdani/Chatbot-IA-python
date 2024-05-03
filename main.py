import chatbot

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN ="7027278237:AAE7dLU1QkjY85UCSI6jWJj_zyrVeGLliBk"

USUARIO="@DDaniChatBot"

#Repetir esto para los comandos en sí
async def comandos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tienes tres comandos: /start , /info y /comands. Selecciona uno de ellos para ver que hacer")

async def inicio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, bienvenidoo!")

#Repetir esto para los comandos en sí
async def informacion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Soy un chatbot programado con IA y python que sigue aprendiendo cosas. Podés ver mi código en [inserte link luego]"
                                    "Además soy super copado")


async def mensajes_entrantes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tipo = update.message.chat.type
    texto = update.message.text

    if not texto:
        return
    
    if tipo == "group":
        if USUARIO in texto:
            texto_nuevo = texto.replace(USUARIO, " ").strip()
            response = chatbot.respuestas(texto_nuevo)
        else:
            return
    else:
        response = chatbot.respuestas(texto)

    if response:
        await update.message.reply_text(response)
    else:
        await update.message.reply_text("ha ocurrido un problema")


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    #comandos
    app.add_handler(CommandHandler("start", inicio))
    app.add_handler(CommandHandler("info", informacion))
    app.add_handler(CommandHandler("comandos", comandos))

    #respuestas
    app.add_handler(MessageHandler(filters.TEXT, mensajes_entrantes))

    #actualizacion del bot
    app.run_polling(poll_interval=0)