import os
import discord
from discord.ext import commands
import datetime
from discord.utils import get


PREFIX = '/'


client = commands.Bot( command_prefix = PREFIX )
client.remove_command( 'help' )

@client.event

async def on_ready():
	print ( 'Бот Подключён!Можно работать.' )

	await client.change_presence( status = discord.Status.online, activity = discord.Game( 'Дрочит Пиписорку' ) )

#clear
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def clear( ctx, amount = 100 ):
	await ctx.channel.purge( limit = amount )


#clear commands
@client.command( pass_context = True)
@commands.has_permissions( administrator = True )
	
async def hello( ctx, amount = 1):
	emb = discord.Embed( title = 'Kick', colour = discord.Color.green() )
	await ctx.channel.purge( limit = amount )

	author = ctx.message.author
	await ctx.send( f'Иди нахуй бомж ебаный { author.mention }')

#Kick
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def kick( ctx, member: discord.Member, *, reason = None ):
	emb = discord.Embed( title = 'Kick', colour = discord.Color.red() )
	await ctx.channel.purge( limit = 1 )

	await member.kick( reason = reason )

	emb.set_author( name = member.name, icon_url = member.avatar_url )
	emb.add_field(name = 'Kick user', value = 'Kicked_Users : {}'.format( member.mention )  )

	await ctx.send( embed = emb )

	

#ban
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def ban( ctx, member: discord.Member, *, reason = None ):
	emb = discord.Embed( title = 'Ban', colour = discord.Color.red() )
	await ctx.channel.purge( limit = 1 )

	await member.ban( reason = reason )

	emb.set_author( name = member.name, icon_url = member.avatar_url )
	emb.add_field(name = 'Ban user', value = 'Banned_Users : {}'.format( member.mention )  )

	await ctx.send( embed = emb )


#unban
@client.command( pass_context = True)
@commands.has_permissions( administrator = True )
async def unban( ctx, *, member ):
	await ctx.channel.purge( limit = 1 )

	banned_users = await ctx.guild.bans()

	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban( user )
		await ctx.send( f'Unbannded user { user.mention }' )

		return

#command help
@client.command( pass_context = True)
@commands.has_permissions( administrator = True )

async def help( ctx ):
	emb = discord.Embed( title = 'help', colour = discord.Color.red() )
	emb = discord.Embed( title = 'Навигация по командам' )
	
	emb.add_field( name = '{}pizda'.format( PREFIX ), value = 'Ещё один привет от бота' )
	emb.add_field( name = '{}hello'.format( PREFIX ), value = 'Привет от бота' )
	emb.add_field( name = '{}clear'.format( PREFIX ), value = 'Очистка чата' )
	emb.add_field( name = '{}kick'.format( PREFIX ), value = 'Кик Участника' )
	emb.add_field( name = '{}ban'.format( PREFIX ), value = 'Бан Участника' )
	emb.add_field( name = '{}unban'.format( PREFIX ), value = 'Разбан Участника' )

	await ctx.send( embed = emb )

@client.command( pass_context = True)
@commands.has_permissions( administrator = True )

async def time( ctx ):
	emb = discord.Embed( title = 'Your title', colour = discord.Color.green(), url = 'https://time100.ru/Russkoye' )

	emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
	emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
	emb.set_image( url = 'https://sun9-26.userapi.com/c856120/v856120014/202e42/WwtXVGFE9DE.jpg' )
	emb.set_thumbnail( url = 'https://sun9-26.userapi.com/c856120/v856120014/202e42/WwtXVGFE9DE.jpg' )

	now_date = datetime.datetime.now()

	emb.add_field( name = 'Time', value = 'Time : {}'.format( now_date ) )

	await ctx.send( embed = emb )

@client.command()
@commands.has_permissions( administrator = True )

async def users_mute( ctx, member: discord.Member ):
	await ctx.channel.purge( limit = 1 )

	mute_role = discord.utils.get( ctx.message.guild.roles, name = 'mute' )

	await member.add_roles( mute_role )
	await ctx.send( f'У { member.mention }, ограничение чата, за нарушение правил!' )

@client.command()
async def  join(ctx):
	global voice
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild = ctx.guild)

	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()
		await ctx.send(f'Бот залетает в канал: {channel}')

@client.command()
async def  leave(ctx):
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild = ctx.guild)

	if voice and voice.is_connected():
		await voice.disconnect()
	else:
		voice = await channel.connect()
		await ctx.send(f'Бот вылетает с канала: {channel}')

@client.command()
@commands.has_permissions( administrator = True )

async def sex( ctx, member: discord.Member ):
	await ctx.channel.purge( limit = 1 )

	sex_role = discord.utils.get( ctx.message.guild.roles, name = 'sex' )

	await member.add_roles( sex_role )
	await ctx.send( f'У { member.mention }, появилась топ роль!' )

@client.command( pass_context = True)
@commands.has_permissions( administrator = True )	
async def pizda( ctx, amount = 1):
	await ctx.channel.purge( limit = amount )

	author = ctx.message.author
	await ctx.send( f'хуй на { author.mention }')
	
token = os.environ.get('BOT_TOKEN') # Получаем токен с heroku который ты указывал в настройках

client.run(str(token)) # запускаем бота

