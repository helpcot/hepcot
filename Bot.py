import os
import configuration as config
from discord.ext import commands

Bot = commands.Bot(command_prefix = config.PREFIX) # Назначаем основную переменную Bot
Bot.remove_command("help")

for cogs in os.listdir("./cogs"): # Подключаем папку для когов с названием cogs
	if cogs.endswith(".py"): # Если файлы заканчиваются на .py, то выполняется следущее
		cogs = f"cogs.{cogs.replace('.py', '')}"
		Bot.load_extension(cogs) # Загрузка когов

Bot.run(config.TOKEN) # Запуск бота