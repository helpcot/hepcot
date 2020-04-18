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
async def on_ready(*args):
    print ( 'Бот Подключён!Можно работать.' )
    type = discord.ActivityType.listening
    activity = discord.Activity(name = "легендарную пыль", type = type)
    status = discord.Status.dnd
    await client.change_presence(activity = activity, status = status)

#clear
@client.command()
@commands.has_permissions( administrator = True)
async def clear(ctx,amount : int):
    
    channel_log = client.get_channel(698638879271420017) #Айди канала логов

    await ctx.channel.purge( limit = amount )

# Работа с ошибками очистки чата

@clear.error 
async def clear_error(ctx, error):

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.name},у вас нет прав для использования данной команды.**', color=0x0c0c0c))

    if isinstance( error, commands.MissingRequiredArgument  ): 
        await ctx.send(embed = discord.Embed(description = f'**:grey_exclamation: {ctx.author.name},обязательно укажите количевство сообщений.**', color=0x0c0c0c))
	

#Kick
@client.command()
@commands.has_permissions( administrator = True) 
async def kick(ctx,member: discord.Member = None, reason = None): 

    if member is None:

        await ctx.send(embed = discord.Embed(description = '**:grey_exclamation: Обязательно укажите: пользователя!**'))

    elif reason is None:

        await ctx.send(embed = discord.Embed(description = '**:grey_exclamation: Обязательно укажите: причину!**'))

    else:

        channel_log = client.get_channel(1111111111) #Айди канала логов

        await member.kick( reason = reason )
        await ctx.send(embed = discord.Embed(description = f'**:shield: Пользователь {member.mention} был исключен.\n:book: По причине: {reason}**', color=0x0c0c0c))
        await channel_log.send(embed = discord.Embed(description = f'**:shield: Пользователь {member.mention} был исключен.\n:book: По причине: {reason}**', color=0x0c0c0c)) 

# Работа с ошибками кика

@kick.error 
async def kick_error(ctx, error):

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.name},у вас нет прав для использования данной команды.**', color=0x0c0c0c))
	

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


async def help( ctx ):
    emb = discord.Embed( title = 'help', colour = discord.Color.red() )
    emb = discord.Embed( title = 'Навигация по командам' )
	
    emb.add_field( name = '{}roles'.format( PREFIX ), value = 'Посмотерть всех участников заданной роли' )	
    emb.add_field( name = '{}bridge'.format( PREFIX ), value = 'Мини игра' )	
    emb.add_field( name = '{}password'.format( PREFIX ), value = 'Сгенерировать пароль' )	
    emb.add_field( name = '{}mute'.format( PREFIX ), value = 'Выдать мут' )
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
    emb = discord.Embed(title='Переправа через речку',description=f'Переправляется {member}')
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
    #################
    

    if ds == a:
        luck += 1
        emb.add_field(name='1 шаг\nПостройка моста', value=f'Мост оказался {var}\nИтог: УДАЧА')
    if ds == b:
        luck -= 1
        emb.add_field(name='1 шаг\nПостройка моста', value=f'Мост оказался {var2}\nИтог: НЕУДАЧА')
    await message.edit(embed = emb)
    await asyncio.sleep(2)
    #########################
    if r1 == a1:
        luck += 1
        emb.add_field(name=f'2 шаг\nСостояние {ctx.author.name}', value=f'{member} был {st1}\nИтог: УДАЧА')
    if r1 == b1:
        luck -= 1
        emb.add_field(name=f'2 шаг\nCостояние {ctx.author.name}', value=f'{member} был {st2}\nИтог: НЕУДАЧА')
    await message.edit(embed = emb)
    await asyncio.sleep(2)
    #########################
    if r2 == a2:
        luck += 1
        emb.add_field(name=f'3 шаг\nПереход {ctx.author.name}', value=f'{member} {de1}\nИтог: УДАЧА')
    if r2 == b2:
        luck -= 1
        emb.add_field(name=f'3 шаг\nПереход {ctx.author.name}', value=f'{member} {de2}\nИтог: НЕУДАЧА')
    await message.edit(embed = emb)
    await asyncio.sleep(2)
    ########################
    if r3 == a3:
        luck += 1
        emb.add_field(name=f'4 шаг\nПриключение {ctx.author.name}', value=f'{se1}\nИтог: УДАЧА')
    if r3 == b3:
        luck -= 1
        emb.add_field(name=f'4 шаг\nПриключение {ctx.author.name}', value=f'{se2}\nИтог: НЕУДАЧА')
    await message.edit(embed = emb)
    await asyncio.sleep(2)
    ########################
    ran = ['Ты успешно перебрался','Ты так и не смог перебраться']
    rin = r.choice(ran)
    if luck > 0:
        emb.add_field(name='Успех', value=f'{member} успешно перебрался')
    if luck < 0:
        emb.add_field(name='Провал', value=f'{member} так и не смог перебраться')
    if luck == 0:
        emb.add_field(name='Итог:', value =f'{rin}')
    await message.edit(embed = emb)


@client.command()
@commands.has_permissions(administrator = True)
async def mute(ctx, amount : int, member: discord.Member = None, role: discord.Role = None):
    await ctx.channel.purge( limit = 1 )

    mute_role = discord.utils.get( ctx.message.guild.roles, name = 'mute' )
    
    await member.add_roles( mute_role )
    await ctx.send(embed = discord.Embed(description = f'**:shield:Мут пользователю {member.mention} успешно выдан на {amount} секунд!:shield:**', color=0x0000FF))
    await asyncio.sleep(amount)
    await member.remove_roles( mute_role )
    await ctx.send(embed = discord.Embed(description = f'**:white_check_mark:Мут у пользователя {member.mention} успешно снят!:white_check_mark:**', color=0x800080))


@client.command()
@commands.has_permissions( administrator = True) 
async def clown(ctx,member: discord.Member = None):

    if member is None:

        await ctx.send(embed = discord.Embed(description = '**:grey_exclamation: Обязательно укажите: пользователя!**'))

    else:

        mute_role = discord.utils.get( ctx.message.guild.roles, name = 'clown' ) #Айди роли
        channel_log = client.get_channel(612921652199817224) #Айди канала логов

        await member.add_roles( mute_role )
       
        await channel_log.send(embed = discord.Embed(description = f'**:clown: Пользователю {member.mention} была дана роль клоуна :clown:**', color=0x0c0c0c))  

# Работа с ошибками мута

@clown.error 
async def clown_error(ctx, error):

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.name},у вас нет прав для использования данной команды.**', color=0x0c0c0c))

	
@client.command()
async def roles(ctx, role: discord.Role = None):

    await ctx.message.delete()
    
    if not role:
        description = f''
        guild = ctx.guild
        for i in guild.roles:
            description += f'{i.mention} \n\n'
        await ctx.send(embed = discord.Embed(description = description))
    else:
        await ctx.send(embed = discord.Embed(description = f'**Участников с этой ролью:** {len(role.members)}'))
	
	
@client.event
async def is_owner(ctx):
    return ctx.author.id == 583991031016456192 # Айди создателя бота


@client.command()
@commands.check(is_owner)
async def channel_create(ctx, *, arg):

    await ctx.message.delete()
     
    guild = ctx.guild
    channel = await guild.create_text_channel(f'{arg}')
    await ctx.send(embed = discord.Embed(description = f'**:strawberry: Текстовый канал "{arg}" успешно создан!:strawberry:**', color=0x0c0c0c))


@client.command(name = "ник", aliases = ["rename", "change"])
@commands.has_permissions(administrator = True)
async def ник(ctx, member: discord.Member = None, nickname: str = None):
    try:
        if member is None:
            await ctx.send(embed = discord.Embed(description = "Обязательно укажите **пользователя**!"))
        elif nickname is None:
            await ctx.send(embed = discord.Embed(description = "Обязательно укажите ник!"))
        else:
            await member.edit(nick = nickname)
            await ctx.send(embed = discord.Embed(description = f"У пользователя **{member.name}** был изменен ник на **{nickname}**"))
    except:
        await ctx.send(embed = discord.Embed(description = f"Я не могу изменить ник пользователя **{member.name}**!"))
	
	
@client.command()
@commands.has_permissions( administrator = True)
async def say(ctx, *, arg):

    await ctx.message.delete()

    await ctx.send(embed = discord.Embed(description = f'{arg}', color=0x0c0c0c))
	
	
@client.command()
@commands.has_permissions(administrator=True)
async def mutek(ctx, member: discord.Member,reason=None):
        try:#Даю роль mute
            mute_role = discord.utils.get(member.guild.roles,name='mute')
            await member.add_roles(mute_role)
        except: # Если такой нет то саздаю и сразу настраиваю
            role = await ctx.guild.create_role(name="mute")#создаю роль с названием mute
            #меняю права роли
            await role.edit(name='mute', send_messages=False, send_tts_messages=False, read_messages=True, hoist=True)
            mute_role = discord.utils.get(member.guild.roles,name='mute')
            await member.add_roles(mute_role)#Даю роль 
            #Настраиваю каналыы
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = False
            for chat in ctx.guild.channels:
                await chat.set_permissions(role, overwrite=overwrite)	

	
token = os.environ.get('BOT_TOKEN') # Получаем токен с heroku который ты указывал в настройках
client.run(str(token)) # запускаем бота

