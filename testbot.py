import telegram
bot = telegram.Bot(token="2018116023:AAE4BTVAMSJd9sJ03hu6QpnRo-rwm9CdwO8")
updates = bot.get_updates()
print(updates[1])
bot.send_message(text='Hi Momo!', chat_id=675633880)