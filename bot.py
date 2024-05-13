from pyrogram import Client, Filters

# Инициализация бота
app = Client("токен?")

# Обработка входящих сообщений
@app.on_message(Filters.private)
async def handle_message(client, message):
    # Обработка сообщения и отправка новых сообщений
    pass

app.run()
