import os
import discord
from discord.ext import commands
import datetime
from discord.utils import get
import asyncio
import random



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
	
	
serverid = 698603287032758404
rainbowrolename = "ПИДАРАС"
delay = 5


client = discord.Client()
colours = [discord.Color.dark_orange(),discord.Color.orange(),discord.Color.dark_gold(),discord.Color.gold(),discord.Color.dark_magenta(),discord.Color.magenta(),discord.Color.red(),discord.Color.dark_red(),discord.Color.blue(),discord.Color.dark_blue(),discord.Color.teal(),discord.Color.dark_teal(),discord.Color.green(),discord.Color.dark_green(),discord.Color.purple(),discord.Color.dark_purple()]

async def rainbowrole(role):
    for role in client.get_guild(serverid).roles:
        if str(role) == str(rainbowrolename):
            print("detected role")
            while not client.is_closed():
                try:
                    await role.edit(color=random.choice(colours))
                except Exception:
                    print("can't edit role, make sure the bot role is above the rainbow role and that is have the perms to edit roles")
                    pass
                await asyncio.sleep(delay)
    print('role with the name "' + rainbowrolename +'" not found')
    print("creating the role...")
    try:
        await client.get_guild(serverid).create_role(reason="Created rainbow role", name=rainbowrolename)
        print("role created!")
        await asyncio.sleep(2)
        client.loop.create_task(rainbowrole(rainbowrolename))
    except Exception as e:
        print("couldn't create the role. Make sure the bot have the perms to edit roles")
        print(e)
        pass
        await asyncio.sleep(10)
        client.loop.create_task(rainbowrole(rainbowrolename))

@client.event
async def on_ready():
    client.loop.create_task(rainbowrole(rainbowrolename))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Ready.')
    print('------------')
	
	
token = os.environ.get('BOT_TOKEN') # Получаем токен с heroku который ты указывал в настройках

client.run(str(token)) # запускаем бота

