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


@client.event
async def on_message(message):
    await client.process_commands(message)
    ctx = message.content
    author = message.author
    channel = message.channel.name
    print("{0},{1},{2}".format(ctx,author,channel))


@client.event
async def on_message(message):
    await client.process_commands(message)
    ctx = message.content
    author = message.author
    channel = message.channel.name
    print("{0},{1},{2}".format(ctx,author,channel))


@client.command(aliases = ['count', 'calc', 'вычисли', 'math'])
async def __count(ctx, *, args = None):
    text = ctx.message.content

    if args == None:
        await ctx.send(embed = discord.Embed(description = 'Please, specify expression to evaluate.', color = 0x800080))
    else:
        result = eval(args)
        await ctx.send(embed = discord.Embed(description = f'Evaluation result of `{args}`: \n`{result}`', color = 0x800080))
	
	
@client.command()
async def roles(ctx, role: discord.Role):
    await ctx.send(embed = discord.Embed(description = f'**Участников с этой ролью:** {len(role.members)}', color = 0x800000))


@client.command(aliases=['мост2'])
async def bridge(ctx):
    #jo = [ 'плохим' , 'ветхим' , 'прочным' , 'каменным' , 'деревянным' , 'на соплях' ]
    vir = ['прочным','каменным','ударооустойчивым','деревянным']
    vir2 = ['плохим','ветхим','на соплях','из веток']
    var = r.choice(vir)
    var2 = r.choice(vir2)
    ###############
    si1 = ['умный','внимательный','опытный','ловкий']
    si2 = ['пьяный','кантуженный','слепой','тупой','сорвиголова','уставший']
    st1 = r.choice(si1)
    st2 = r.choice(si2)
    ###############
    di1 = ['аккуратно пошёл','пополз','осторожно шагал']
    di2 = ['полетел','мысленно пошёл','быстро побежал','неуклюже пошёл','неосторожно шагал']
    de1 = r.choice(di1)
    de2 = r.choice(di2)
    ###############
    sl1 = ['У моста был самолёт','Около моста была лошадь','Было солнечно']
    sl2 = ['На мост напали крокодилы','Германские войска начали бомбить мост','Мост начал разваливаться','У моста ходили волки','У подножия обедал медведь','Кто-то начал орать','Дул сильный ветер']
    se1 = r.choice(sl1)
    se2 = r.choice(sl2)
    member = ctx.author.mention
    luck = 0
    emb = discord.Embed(title='__Переправа через речку__',description=f'Переправляется {member}')
    message = await ctx.send(embed = emb)
    await asyncio.sleep(1)
    a = 'удача'
    b = 'провал'
    e = [a,b]
    ds = r.choice(e)
    ################
    a1 = 'удача'
    b1 = 'провал'
    e1 = [a1,b1]
    r1 = r.choice(e1)
    ################
    a2 = 'удача'
    b2 = 'провал'
    e2 = [a2,b2]
    r2 = r.choice(e2)
    ################
    a3 = 'удача'
    b3 = 'провал'
    e3 = [a3,b3]
    r3 = r.choice(e3)
    if ds == a:
        luck += 1
        emb.add_field(name='1 шаг\nПостройка моста', value=f'Мост оказался {var}\n`Итог:` **УДАЧА**')
    if ds == b:
        luck -= 1
        emb.add_field(name='1 шаг\nПостройка моста', value=f'Мост оказался {var2}\n`Итог:` **НЕУДАЧА**')
    await message.edit(embed = emb)
    await asyncio.sleep(2)
    #########################
    if r1 == a1:
        luck += 1
        emb.add_field(name=f'2 шаг\nСостояние {ctx.author.name}', value=f'{member} был {st1}\n`Итог:` **УДАЧА**')
    if r1 == b1:
        luck -= 1
        emb.add_field(name=f'2 шаг\nCостояние {ctx.author.name}', value=f'{member} был {st2}\n`Итог:` **НЕУДАЧА**')
    await message.edit(embed = emb)
    await asyncio.sleep(2)
    #########################
    if r2 == a2:
        luck += 1
        emb.add_field(name=f'3 шаг\nПереход {ctx.author.name}', value=f'{member} {de1}\n`Итог:` **УДАЧА**')
    if r2 == b2:
        luck -= 1
        emb.add_field(name=f'3 шаг\nПереход {ctx.author.name}', value=f'{member} {de2}\n`Итог:` **НЕУДАЧА**')
    await message.edit(embed = emb)
    await asyncio.sleep(2)
    ########################
    if r3 == a3:
        luck += 1
        emb.add_field(name=f'4 шаг\nПриключение {ctx.author.name}', value=f'{se1}\n`Итог:` **УДАЧА**')
    if r3 == b3:
        luck -= 1
        emb.add_field(name=f'4 шаг\nПриключение {ctx.author.name}', value=f'{se2}\n`Итог:` **НЕУДАЧА**')
    await message.edit(embed = emb)
    await asyncio.sleep(2)
    ########################
    ran = ['Успех\n{member} успешно перебрался','Провал\n{member} так и не смог перебраться']
    rin = r.choice(ran)
    if luck > 0:
        emb.add_field(name='Успех', value=f'{member} успешно перебрался')
    if luck < 0:
        emb.add_field(name='Провал', value=f'{member} так и не смог перебраться')
    if luck == 0:
        emb.add_field(name=..., value ={rin})
    await message.edit(embed = emb)

	
token = os.environ.get('BOT_TOKEN') # Получаем токен с heroku который ты указывал в настройках
client.run(str(token)) # запускаем бота

