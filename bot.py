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
    
    channel_log = client.get_channel(705186463578456204) #Айди канала логов

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

        channel_log = client.get_channel(710950827786895454) #Айди канала логов

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
    channel = message.channel
    print("{0},{1},{2}".format(ctx,author,channel))


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


@client.command( pass_context = True, aliases=[ "Мут", "мут", "мьют", "Мьют", "mute" ] )
@commands.has_permissions( administrator = True)
async def tempmute(ctx, member : discord.Member, time:int, arg:str, *, reason=None):

    Переменная_размут = f'**Вы были размучены на сервере {ctx.guild.name}**'
    Переменная_мут = f'**Вы были замучены на сервере {ctx.guild.name} на {time}{arg} по причине: {reason}**'
    mute_role = discord.utils.get( ctx.message.guild.roles, id = 706584225591066747 )

    await member.add_roles(mute_role, reason=None, atomic=True)
    await ctx.send(embed = discord.Embed(description = f'**:shield:Мут пользователю {member.mention} успешно выдан на {time}{arg} по причине {reason} :shield:**', color=0x0000FF))
    await member.send(embed = discord.Embed(description = f'{Переменная_мут}', color=0x0c0c0c))

    if arg == "s":
        await asyncio.sleep(time)          
    elif arg == "m":
        await asyncio.sleep(time * 60)
    elif arg == "h":
        await asyncio.sleep(time * 60 * 60)
    elif arg == "d":
        await asyncio.sleep(time * 60 * 60 * 24)

    await member.remove_roles( mute_role )
    await ctx.send(embed = discord.Embed(description = f'**:white_check_mark:Мут у пользователя {member.mention} успешно снят!:white_check_mark:**', color=0x800080))
    await member.send(embed = discord.Embed(description = f'{Переменная_размут}', color=0x800080))


@tempmute.error 
async def tempmute_error(ctx, error):

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.mention},у вас нет прав для использования данной команды.**', color=0x0c0c0c))

    
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


@client.command()
@commands.has_permissions(administrator = True)
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


@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 719269317149196349: # ID Сообщения
        guild = client.get_guild(payload.guild_id)
        role = None

        if str(payload.emoji) == '🍓': # Emoji для реакций
            role = guild.get_role(719220991322226848) # ID Ролей для выдачи 【v】【e】【r】【i】【f】【i】【e】【d】
        elif str(payload.emoji) == '🪓':
            role = guild.get_role(711220628950220911)#【G】【T】【A】
        elif str(payload.emoji) == '✈️':
            role = guild.get_role(694512931546857512)#【D】【a】【y】【Z】
        elif str(payload.emoji) == '🔮':
            role = guild.get_role(692861094602997800)#【D】【O】【T】【A】【2】
        elif str(payload.emoji) == '🌐':
            role = guild.get_role(692870504935063602)#【C】【s】【G】【o】
        elif str(payload.emoji) == '❓':
            role = guild.get_role(683045145817776139)#【q】【u】【b】【e】

        if role:
            member = guild.get_member(payload.user_id)
            if member:
                await member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 719269317149196349: # ID Сообщения
        guild = client.get_guild(payload.guild_id)
        role = None

        if str(payload.emoji) == '🍓': # Emoji для реакций
            role = guild.get_role(719220991322226848) # ID Ролей для выдачи 【v】【e】【r】【i】【f】【i】【e】【d】
        elif str(payload.emoji) == '🪓':
            role = guild.get_role(711220628950220911)#【G】【T】【A】
        elif str(payload.emoji) == '✈️':
            role = guild.get_role(694512931546857512)#【D】【a】【y】【Z】
        elif str(payload.emoji) == '🔮':
            role = guild.get_role(692861094602997800)#【D】【O】【T】【A】【2】
        elif str(payload.emoji) == '🌐':
            role = guild.get_role(692870504935063602)#【C】【s】【G】【o】
        elif str(payload.emoji) == '❓':
            role = guild.get_role(683045145817776139)#【q】【u】【b】【e】

        if role:
            member = guild.get_member(payload.user_id)
            if member:
                await member.remove_roles(role)
		
		
@client.event
async def on_member_join( member ):
    emb = discord.Embed( description = f"**:strawberry:Пользователь **{member.mention}**, присоединился к серверу!:strawberry:**", color = 0x0c0c0c )
    

    channel = client.get_channel( 646440966026166282 ) # Айди канала куда будет писаться сообщение
    await channel.send( embed = emb )


@client.event
async def on_member_remove( member ):
    emb = discord.Embed( description = f"**:x:Пользователь **{member.mention}**, покинул сервер!:x:**", color = 0x0c0c0c )
    

    channel = client.get_channel( 646440966026166282 ) # Айди канала куда будет писаться сообщение
    await channel.send( embed = emb )


@client.command()
async def sayqwecccccc( ctx ):
	emb = discord.Embed( 
		title = 'Получение ролей',
		color = 0x7aa13d
	 )

	emb.add_field( name = '**Нажми на эмодзи для получения роли**', value = '''
		:strawberry:`---`【v】【e】【r】【i】【f】【i】【e】【d】
		:axe:`---`【G】【T】【A】
		:airplane:`---`【D】【a】【y】【Z】
		:crystal_ball:`---`【D】【O】【T】【A】【2】
		:globe_with_meridians:`---`【C】【s】【G】【o】
		:question:`---`【q】【u】【b】【e】

		''' )

	await ctx.send( embed = emb )
	
	
@client.command()
@commands.has_permissions(administrator = True)
async def statplay(ctx, *, arg):
    await ctx.channel.purge( limit = 1 )
    await client.change_presence(activity=discord.Game(name=arg))
    await ctx.send("Изменяем...")
    await ctx.send("Статус бота изменен!")


@client.command()
@commands.has_permissions(administrator = True)
async def statwatch(ctx, *, arg):
    await ctx.channel.purge( limit = 1 )
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(name=arg, type=discord.ActivityType.watching))
    await ctx.send("Изменяем...")
    await ctx.send("Статус бота изменен!")


@client.command()
@commands.has_permissions(administrator = True)
async def statlisten(ctx, *, arg):
    await ctx.channel.purge( limit = 1 )
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(name=arg, type=discord.ActivityType.listening))
    await ctx.send("Изменяем...")
    await ctx.send("Статус бота изменен!")
	
	
@client.command()
@commands.has_permissions(administrator = True)
async def statstream(ctx, *, arg):
    await ctx.channel.purge( limit = 1 )
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(name=arg, type=discord.ActivityType.streaming))
    await ctx.send("Изменяем...")
    await ctx.send("Статус бота изменен!")
	
	
@client.event
async def on_guild_role_create(role):
    chanel = client.get_channel(710950827786895454)
    async for entry in chanel.guild.audit_logs(limit = 1,action=discord.AuditLogAction.role_create):
        e = discord.Embed(colour=0x08dfab)
        e.set_author(name = 'Журнал аудита | создание роли', url = e.Empty, icon_url = 'https://media.discordapp.net/attachments/689879530542071952/711588305506140241/verdict.png?width=407&height=407')
        e.add_field(name = "Роль:", value = f"<@&{entry.target.id}>")
        e.add_field(name = "ID роли:", value = f"{entry.target.id}")
        e.add_field(name = "‎‎‎‎", value = "‎‎‎‎",)
        e.add_field(name = "Создал:", value = f"{entry.user.mention}")
        e.add_field(name = "ID создавшего:", value = f"{entry.user.id}")
        e.add_field(name = "‎‎‎‎", value = "‎‎‎‎")
        await chanel.send(embed=e)
        return
@client.event
async def on_guild_role_delete(role):
    chanel = client.get_channel(710950827786895454)
    async for entry in chanel.guild.audit_logs(action=discord.AuditLogAction.role_delete):
        e = discord.Embed(colour=0xe84444)
        e.set_author(name = 'Журнал аудита | удаление роли', url = e.Empty, icon_url = 'https://media.discordapp.net/attachments/689879530542071952/711588305506140241/verdict.png?width=407&height=407')
        e.add_field(name = "Роль:", value = f"{role.name}")
        e.add_field(name = "ID роли:", value = f"{entry.target.id}")
        e.add_field(name = "‎‎‎‎", value = "‎‎‎‎",inline=False)
        e.add_field(name = "Удалил:", value = f"{entry.user.mention}")
        e.add_field(name = "ID удалившего:", value = f"{entry.user.id}")
        await chanel.send(embed=e)
        return


@client.command(aliases = ["емодзи", "емоджи", "эмоджи", "эмоция"])
async def эмодзи(ctx, emoji: discord.Emoji):
    e = discord.Embed(description = f"[Эмодзи]({emoji.url}) сервера {emoji}")
    e.add_field(name = "Имя:", value = f"`{emoji.name}`")
    e.add_field(name = "Автор:", value = f"{(await ctx.guild.fetch_emoji(emoji.id)).user.mention}")
    e.add_field(name = "‎‎‎‎", value = "‎‎‎‎")
    e.add_field(name = "Время добавления:", value = f"`{emoji.created_at}`")
    e.add_field(name = "ID эмодзи:", value = f"`{emoji.id}`")
    e.add_field(name = "‎‎‎‎", value = "‎‎‎‎")
    e.set_thumbnail(url = f"{emoji.url}")
    await ctx.send(embed = e)


@client.event
async def on_guild_role_create(role):
    chanel = client.get_channel(710950827786895454)
    async for entry in chanel.guild.audit_logs(limit = 1,action=discord.AuditLogAction.role_create):
        e = discord.Embed(colour=0x08dfab)
        e.set_author(name = 'Журнал аудита | создание роли', url = e.Empty, icon_url = 'https://media.discordapp.net/attachments/689879530542071952/711588305506140241/verdict.png?width=407&height=407')
        e.add_field(name = "Роль:", value = f"<@&{entry.target.id}>")
        e.add_field(name = "ID роли:", value = f"{entry.target.id}")
        e.add_field(name = "‎‎‎‎", value = "‎‎‎‎",)
        e.add_field(name = "Создал:", value = f"{entry.user.mention}")
        e.add_field(name = "ID создавшего:", value = f"{entry.user.id}")
        e.add_field(name = "‎‎‎‎", value = "‎‎‎‎")
        await chanel.send(embed=e)
        return
@client.event
async def on_guild_role_delete(role):
    chanel = client.get_channel(710950827786895454)
    async for entry in chanel.guild.audit_logs(action=discord.AuditLogAction.role_delete):
        e = discord.Embed(colour=0xe84444)
        e.set_author(name = 'Журнал аудита | удаление роли', url = e.Empty, icon_url = 'https://media.discordapp.net/attachments/689879530542071952/711588305506140241/verdict.png?width=407&height=407')
        e.add_field(name = "Роль:", value = f"{role.name}")
        e.add_field(name = "ID роли:", value = f"{entry.target.id}")
        e.add_field(name = "‎‎‎‎", value = "‎‎‎‎",inline=False)
        e.add_field(name = "Удалил:", value = f"{entry.user.mention}")
        e.add_field(name = "ID удалившего:", value = f"{entry.user.id}")
        await chanel.send(embed=e)
        return


@client.event
async def on_message_delete(message):
    channel = client.get_channel(710950827786895454)
    if message.content is None:
        return
    emb = discord.Embed(colour=0xff0000,
				description=f"{message.author}"
    				f"\n Удалил сообщение: `{message.content}`"
    				f"\n В канале: `{message.channel}`",timestamp=message.created_at)


    emb.set_author(name = 'Журнал аудита | Удаление сообщений', url = emb.Empty, icon_url = 'https://media.discordapp.net/attachments/689879530542071952/711588305506140241/verdict.png?width=407&height=407')
    emb.set_footer(text=f'ID Пользователя: {message.author.id} | ID Сообщения: {message.id}')
    await channel.send(embed=emb)
    return


@client.event
async def on_message_edit(before, after):
    channel = client.get_channel(710950827786895454)
    if before.author == client.user:
        return
    if before.content is None:
        return
    elif after.content is None:
        return
    emb = discord.Embed(colour=0xFF8000,
                                 description=f"{before.author} Изменил сообщение в канале {before.channel} "
                                             f"\n`Старое сообщение`:{before.content}"
                                             f"\n`Новое сообщение`: {after.content}",timestamp=before.created_at)

    emb.set_author(name = 'Журнал аудита | Изменение сообщений', url = emb.Empty, icon_url = 'https://media.discordapp.net/attachments/689879530542071952/711588305506140241/verdict.png?width=407&height=407')
    emb.set_footer(text=f"ID Пользователя: {before.author.id} | ID Сообщения: {before.id}")
    await channel.send(embed=emb)
    return		
	
token = os.environ.get('BOT_TOKEN') # Получаем токен с heroku который ты указывал в настройках
client.run(str(token)) # запускаем бота

