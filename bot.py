import os
import discord
from discord.ext import commands
import datetime
from discord.utils import get
import asyncio
import random as r



PREFIX = '/'


client = commands.Bot( command_prefix = PREFIX )
client.remove_command( 'help' )

@client.event

async def on_ready():
	print ( 'Бот Подключён!Можно работать.' )

	await client.change_presence( status = discord.Status.online, activity = discord.Game( 'Эммм' ) )

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
	
	emb.add_field( name = '{}clear'.format( PREFIX ), value = 'Очистка чата' )
	emb.add_field( name = '{}kick'.format( PREFIX ), value = 'Кик Участника' )
	emb.add_field( name = '{}ban'.format( PREFIX ), value = 'Бан Участника' )
	emb.add_field( name = '{}unban'.format( PREFIX ), value = 'Разбан Участника' )

	await ctx.send( embed = emb )
	

ev_player = [''] #игроки в розыгрыше
start_ev = 0 #перемычка

@client.command()
async def event_roles(stx, role: discord.Role = None, member: discord.Member = None):
    global ev_player
    global start_ev
    general = client.get_channel(698603287032758404)
    if role is None:
        await stx.send('**Упомяните роль для розыгрыша.**' '\n' '`/event_roles [role]`')
        return
    ev_role = role
    start_ev = 1
    await general.send(f'Технический администратор запустил розыгрыш роли {role.mention}. Для участия пропишите `/mp`.' '\n' f'**Розыгрыш состоится через 2 минуты.**')
    await asyncio.sleep(120)
    ev_win = r.choice(ev_player)
    member = ev_win
    await general.send(f'**Поздравляем {ev_win.mention}! Он выигрывает в розыгрыше и получает роль {role.mention}.**')
    await ev_win.add_roles(role)
    ev_player = ['']
    start_ev = 0

@client.command()
async def mp(stx):
    global ev_player
    global start_ev
    author = stx.message.author
    if start_ev == 0:
        await stx.send('**Сейчас нету розыгрыша ролей!**')
        return
    if author in ev_player:
        await stx.send('Вы уже приняли участие в этом розыгрыше!')
        return
    else:
        ev_player.append(author)
        print(f'Игрок {author} принял участие в розыгрыши роли.')
        await stx.send(embed = discord.Embed(description = f'**{author.mention}, Вы успешно приняли участие в розыгрыши роли!**', color = 0xee3131))
        print('Розыгрыш роли завершен.')
		
	
token = os.environ.get('BOT_TOKEN') # Получаем токен с heroku который ты указывал в настройках

client.run(str(token)) # запускаем бота

