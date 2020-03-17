import discord
import configuration as config
from discord.ext import commands
from datetime import datetime

class Discord(commands.Cog):

	def __init__(self, Bot):
		self.Bot = Bot

	@commands.Cog.listener()
	async def on_ready(self):
		time = datetime.now().strftime("%H:%M:%S")
		print(f"Бот бы запущен в {time}")

	@commands.command(name = "kick", aliases = ["k"])
	async def kick_member(self, ctx, member: discord.Member = None, *, reason: str or int = "Не указана"):
		time = datetime.now().strftime("%H:%M:%S")
		embed = discord.Embed(description = f"Пользователь **{member.name}** был кикнут **{ctx.author.name}**. \nПричина: {reason}")
		embed.set_author(name = "Пользователь был кикнут", icon_url = member.guild.icon_url)
		embed.set_footer(text = f"Время: {time}")
		await ctx.message.delete()
		await member.kick(reason = reason)
		await ctx.send(embed = embed)

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			embed = discord.Embed(description = "Укажите правильные аргументы!")
			await ctx.message.delete()
			await ctx.send(embed = embed, delete_after = 10)

	@commands.Cog.listener()
	async def on_raw_reaction_add(self, payload):
		if payload.message_id == config.MESSAGE_ID:
			channel = self.Bot.get_channel(payload.channel_id)
			member = discord.utils.get(channel.guild.members, id = payload.user_id)
 
			try:
				emoji = str(payload.emoji)
				role = discord.utils.get(channel.guild.roles, id = config.ROLES[emoji])
				await member.add_roles(role)

			except KeyError as e:
				print(f"Ошибка, нету такого эмодзив базе: {emoji}")
			except Exception as e:
				print(repr(e))

	@commands.Cog.listener()
	async def on_raw_reaction_remove(self, payload):
		channel = self.Bot.get_channel(payload.channel_id)
		member = discord.utils.get(channel.guild.members, id = payload.user_id)
 
		try:
			emoji = str(payload.emoji)
			role = discord.utils.get(channel.guild.roles, id = config.ROLES[emoji])
			await member.remove_roles(role)

		except KeyError as e:
			print(f"Ошибка, нету такого эмодзив базе: {emoji}")
		except Exception as e:
			print(repr(e))

def setup(Bot):
	Bot.add_cog(Discord(Bot))
	print("Коги были загружены.")