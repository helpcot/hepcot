import os
import discord
from discord.ext import commands
import datetime
from discord.utils import get
import asyncio
import random as r
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
	
	emb.add_field( name = '{}av'.format( PREFIX ), value = 'Посмотреть аватарку пользователя' )
	emb.add_field( name = '{}clear'.format( PREFIX ), value = 'Очистка чата' )
	emb.add_field( name = '{}kick'.format( PREFIX ), value = 'Кик Участника' )
	emb.add_field( name = '{}ban'.format( PREFIX ), value = 'Бан Участника' )
	emb.add_field( name = '{}unban'.format( PREFIX ), value = 'Разбан Участника' )
	emb.add_field( name = '{}members'.format( PREFIX ), value = 'Посмотреть Участников Сервера' )

	await ctx.send( embed = emb )
	

@client.command()
async def members(ctx):
    server_members = ctx.guild.members
    data = "\n".join([i.name for i in server_members])
    
    await ctx.send(data)
	
	
@client.command()
async def av(ctx, member : discord.Member = None):
	
    user = ctx.message.author if (member == None) else member

    embed = discord.Embed(title=f'Аватар пользователя {user}', color= 0x00FF00)

    embed.set_image(url=user.avatar_url)

    await ctx.channel.purge( limit = 1 )
    await ctx.send(embed=embed)


@client.command()
async def password(ctx, lenght: int = None, number: int = None):

    if not lenght or not number:
        await ctx.send(embed = discord.Embed(description = f'Пожалуйста, укажите длину пароля и количество символов в нем.', color=0x0c0c0c)) 

    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for x in range(number):
        password = ''

        for i in range( lenght ):
            password += random.choice(chars)

        await ctx.send(embed = discord.Embed(description = f'Сгенерированный пароль:\n{password}', color=0x00FFFF)) 
        return


# создаем таблицу если её нету
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                id TEXT,
                nickname TEXT,
                mention TEXT,
                lvl INT,
                xp INT)""")


@client.event
async def on_message(message):
    cursor.execute(f"SELECT id FROM users where id={message.author.id}") # загружаем БД игрока
    if cursor.fetchone() == None: # Если игрока нету в БД, но он на сервере, то..
        cursor.execute(f"INSERT INTO users VALUES ({message.author.id}, '{message.author.name}', '<@{message.author.id}>', 1, 0)") # вводим данные игрока согласно созданной таблице
    else: # если игрок есть в БД
        pass
    conn.commit() # сохранение БД
    if len(message.content) > 5: # будем начислять опыт за сообщение больше 5ти символов
        for row in cursor.execute(f"SELECT xp,lvl FROM users where id={message.author.id}"):
            expi = row[0]+r.randint(1, 3) # вводим новую переменную, в которую будем добавлять опыт от 1 до 3 единиц
            cursor.execute(f'UPDATE users SET xp={expi} where id={message.author.id}') # обновляем опыт игрока в БД
            lvch = expi/(row[1]*100) # при каком количестве будет повышение LVL
            lv = int(lvch)
            if row[1] < lv: #если текущий уровень меньше уровня, который был рассчитан формулой выше, то...
                await message.channel.send(f'Поздравляю! Вы достигли нового уровня!')
                bal=1000*lv
                cursor.execute(f'UPDATE users SET lvl={lv} where id={message.author.id}') # обновляем уровень игрока
    await client.process_commands(message) # данная фича нужна чтобы узать потом команды
    conn.commit() # опять сохраняем БД


@client.event
async def on_member_join(member):
    cursor.execute(f"SELECT id FROM users where id={member.id}") # все также, существует ли участник в БД
    if cursor.fetchone() == None:
        cursor.execute(f"INSERT INTO users VALUES ({member.id}, '{member.name}', '<@{member.id}>', 1, 0)")
    else:
        pass
    conn.commit()


@client.command()
async def lvl(ctx):
    for row in cursor.execute(f"SELECT lvl,xp FROM users where id={ctx.author.id}"): # задаем цикл где row[0] - уровень, а row[1] - опыт
        await ctx.send(f'Ваш уровень {row[0]}. Опыт: {row[1]}.')

	
token = os.environ.get('BOT_TOKEN') # Получаем токен с heroku который ты указывал в настройках

client.run(str(token)) # запускаем бота

