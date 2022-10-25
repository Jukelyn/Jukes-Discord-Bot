import os
import discord
from discord.ext import commands
from webserver import keep_alive

client = commands.Bot(command_prefix='>')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Genshin Impact'))
    print("We're online!")


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong, ur mom. Latency: {round((client.latency) * 1000)}ms'
                   )


@client.command()
async def pong(ctx):
    await ctx.send("Wrong command dumbass")


@client.command()
async def say(ctx, *, arg):
    await ctx.send(arg)


############################# Troll Commands
@client.command()
async def inv(ctx):
    await ctx.send("INVITE!!! INVITE ME! LEMME JOINNNN!")


@client.command()
async def pro(ctx):
    await ctx.send("pro")


@client.command()
async def pasa(ctx, user: discord.Member = None):
    await ctx.send(":peach:")


@client.command()
async def hug(ctx, user: discord.Member = None):
    await ctx.send(f"<@{ctx.author.id}> gives <@{user.id}> a hug :heart:")


@client.command(aliases=[
    'hugMe', 'needhug', 'needHug', 'hugPlease', 'plzHug', 'plsHug', 'plzhug',
    'plshug'
])
async def hugme(ctx):
    await ctx.send(f"Aww, here's a hug <@{ctx.author.id}> :heart:")


@client.command()
async def kiss(ctx, user: discord.Member = None):
    await ctx.send(f"<@{ctx.author.id}> gives <@{user.id}> a kiss uwu:heart:")


@client.command()
async def owo(ctx):
    await ctx.send("owo")


@client.command()
async def uwu(ctx):
    await ctx.send("uwu")


############################# Troll Commands


@client.command()
async def ban(ctx, *arg):
    out = ''
    for shit in arg:
        out += shit + ' '
    await ctx.send(f'No, you do it. Ban {out} yourself!')


@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def toDo(ctx, amount=99):  # P
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
        messages.append(message)
    await channel.delete_messages(messages)
    await ctx.send(
        f'{amount} messages have been purged by {ctx.message.author.mention}')


@client.command()
async def tell(ctx, *, arg: str) -> str:
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=1):
        messages.append(message)
    await channel.delete_messages(messages)
    await ctx.send(arg)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Genshin Impact'))
    print("We're online!")


@client.command(aliases=['Add', 'addition', 'Addition', '+'])
async def mathadd(ctx, *numbers: float):
    try:
        result = sum(numbers)
        await ctx.send(result)

    except:
        pass


@client.command(aliases=['Sub', 'subtract', 'Subtract', '-'])
async def mathsub(ctx, x: float, y: float):
    try:
        result = x - y
        await ctx.send(result)

    except:
        pass


@client.command(aliases=['Rand', 'random', 'Random'])
async def mathrando(ctx, x: int, y: int):
    x, y = min(x, y), max(x, y)
    try:
        result = random.randint(x, y)
        await ctx.send(result)

    except:
        pass


@client.command(aliases=['Div', 'divide', 'Divide', '/'])
async def mathdiv(ctx, x: float, y: float):
    try:
        result = x / y
        await ctx.send(result)

    except:
        pass


@client.command(aliases=['multi', 'Multi', 'multiply', 'Multiply', '*'])
async def mathmult(ctx, x: float, y: float):
    try:
        result = x * y
        await ctx.send(result)

    except:
        pass


@client.command(aliases=['Sqrt', 'root', 'Root'])
async def mathsqrt(ctx, x: float):
    try:
        result = math.sqrt(x)
        await ctx.send(result)

    except:
        pass
@client.command(aliases=['Power', 'power', 'pow'])
async def mathpow(ctx, x: int, y: int):
    try:
        result = math.pow(x,y)
        await ctx.send(result)
    except:
        pass
@client.command(aliases=['Power', 'power', 'pow'])
async def mathpow(ctx, x: int, y: int):
    try:
        result = math.pow(x,y)
        await ctx.send(result)
    except:
        pass
@client.command(aliases=['log10', 'Log10', 'logx'])
async def log10(ctx, x: float)
    try:
        if x < 0:
            return
        else:
            result = math.log10(x)
            await ctx.send(result)
    except:
        pass
@client.command(aliases=['exp', 'Exp', 'exponent', 'Exponent'])
async def exp(ctx, x: float)
    try:
        result = math.exp(x)
        await ctx.send(result)
    except:
        pass



########################################################### Genshin Commands Below here ###########################################################
@client.command(aliases=['dilluc', 'Dilluc', 'diluc', 'dil', 'Dil'])
async def Diluc(ctx):
    embed = discord.Embed(
        title='Diluc Farming List',
        description=
        'This is for Diluc specific talent and character materials only. Refer to corresponding commands for the specific weapons that this character uses. Additionally, the old banner can be found [here](https://media.discordapp.net/attachments/831885537811234886/833689508330602546/Diluc.png?width=1039&height=702)',
        colour=discord.Colour.red())

    embed.set_footer(text='Banner by: discord.gg/Keqing')  #Bottom Text
    embed.set_image(
        url=
        "https://media.discordapp.net/attachments/953505473125052456/953505605073637376/Diluc_New.png?width=1818&height=1228"
    )  #Banner
    embed.set_thumbnail(
        url='https://rerollcdn.com/GENSHIN/Characters/Diluc.png'
    )  #Small Icon top right
    embed.set_author(
        name='Jukelyn',
        icon_url=
        'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
    )
    embed.add_field(
        name='Everyday',
        value=
        'Small Lamp Grass \n Pyro Regisvines \n Skirmishers \n Agents \n Electro Cicin Mages',
        inline=False)
    embed.add_field(name='Mondays', value='None', inline=False)
    embed.add_field(name='Tuesdays',
                    value='Teachings of Resistance',
                    inline=False)
    embed.add_field(name='Wednesdays', value='None', inline=False)
    embed.add_field(name='Thursdays', value='None', inline=False)
    embed.add_field(name='Fridays',
                    value='Teachings of Resistance',
                    inline=False)
    embed.add_field(name='Saturdays', value='None', inline=False)
    embed.add_field(name='Sundays',
                    value='Teachings of Resistance',
                    inline=False)
    await ctx.send(embed=embed)


@client.command(aliases=['benett', 'bennett', 'ben', 'benny', 'Ben', 'Benny'])
async def Bennett(ctx):
    embed = discord.Embed(
        title='Bennett Farming List',
        description=
        'This is for Bennett specific talent and character materials only. Refer to corresponding commands for the specific weapons that this character uses.',
        colour=discord.Colour.red())

    embed.set_footer(text='Banner by: discord.gg/Keqing')  #Bottom Text
    embed.set_image(url='https://i.imgur.com/nhBVUWn.png')  #Banner
    embed.set_thumbnail(
        url='https://rerollcdn.com/GENSHIN/Characters/Bennett.png'
    )  #Small Icon top right
    embed.set_author(
        name='Jukelyn',
        icon_url=
        'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
    )
    embed.add_field(
        name='Everyday',
        value='Windwheel Asters \n Pyro Regisvines \n Treasure Hoarders',
        inline=False)
    embed.add_field(name='Mondays', value='None', inline=False)
    embed.add_field(name='Tuesdays',
                    value='Teachings of Resistance',
                    inline=False)
    embed.add_field(name='Wednesdays', value='None', inline=False)
    embed.add_field(name='Thursdays', value='None', inline=False)
    embed.add_field(name='Fridays',
                    value='Teachings of Resistance',
                    inline=False)
    embed.add_field(name='Saturdays', value='None', inline=False)
    embed.add_field(name='Sundays',
                    value='Teachings of Resistance',
                    inline=False)
    await ctx.send(embed=embed)


@client.command(aliases=['sucrose', 'suc', 'sucroce', 'Suc'])
async def Sucrose(ctx):
    embed = discord.Embed(
        title='Sucrose Farming List',
        description=
        'This is for Sucrose specific talent and character materials only. Refer to corresponding commands for the specific weapons that this character uses.',
        colour=discord.Colour.red())

    embed.set_footer(text='Banner by: discord.gg/Keqing')  #Bottom Text
    embed.set_image(url='')  #Banner
    embed.set_thumbnail(
        url='https://rerollcdn.com/GENSHIN/Characters/Sucrose.png'
    )  #Small Icon top right
    embed.set_author(
        name='Jukelyn',
        icon_url=
        'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
    )
    embed.add_field(
        name='Everyday',
        value='Windwheel Asters \n Anemo Hypostatis \n Whopperflowers',
        inline=False)
    embed.add_field(name='Mondays', value='Teachings of Freedom', inline=False)
    embed.add_field(name='Tuesdays', value='None', inline=False)
    embed.add_field(name='Wednesdays', value='None', inline=False)
    embed.add_field(name='Thursdays',
                    value='Teachings of Freedom',
                    inline=False)
    embed.add_field(name='Fridays', value='None', inline=False)
    embed.add_field(name='Saturdays', value='None', inline=False)
    embed.add_field(name='Sundays', value='Teachings of Freedom', inline=False)
    await ctx.send(embed=embed)


@client.command(
    aliases=['XQ', 'xq', 'Xq', 'xQ', 'xingqiu', 'xqc', 'xQc', 'XQC', 'xQcL'])
async def Xingqiu(ctx):
    embed = discord.Embed(
        title='Xingqiu Farming List',
        description=
        'This is for Xingqiu specific talent and character materials only. Refer to corresponding commands for the specific weapons that this character uses.',
        colour=discord.Colour.red())

    embed.set_footer(text='Banner by: discord.gg/Keqing')  #Bottom Text
    embed.set_image(
        url=
        'https://media.discordapp.net/attachments/824481856862158849/830641405667835904/Xingqiu.png?width=1039&height=702'
    )  #Banner
    embed.set_thumbnail(
        url='https://rerollcdn.com/GENSHIN/Characters/Xingqiu.png'
    )  #Small Icon top right
    embed.set_author(
        name='Jukelyn',
        icon_url=
        'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
    )
    embed.add_field(
        name='Everyday',
        value='Silk Flowers \n Oceanids \n Hilichurls and Samachurls (Masks)',
        inline=False)
    embed.add_field(name='Mondays', value='None', inline=False)
    embed.add_field(name='Tuesdays', value='None', inline=False)
    embed.add_field(name='Wednesdays', value='Teachings of Gold', inline=False)
    embed.add_field(name='Thursdays', value='None', inline=False)
    embed.add_field(name='Fridays', value='None', inline=False)
    embed.add_field(name='Saturdays', value='Teachings of Gold', inline=False)
    embed.add_field(name='Sundays', value='Teachings of Gold', inline=False)
    await ctx.send(embed=embed)


@client.command(aliases=[
    'sch', 'sc', 'sd', 'give', 'wut', 'what', 'Sch', 'Schedule', 'shcedule',
    'Shcedule', 'Scedule', 'scedule'
])
async def schedule(ctx):
    embed = discord.Embed(title='Weekly Farming List',
                          description="Jukelyn's weekly farming list!",
                          colour=discord.Colour.red())

    embed.set_footer(text='GLHF.')  #Bottom Text
    embed.set_thumbnail(
        url=
        'https://cdn.discordapp.com/avatars/347216701055565827/dd8d8fea4dd82a780589bc98c8854201.webp?size=256'
    )  #Small Icon top right
    embed.set_author(
        name='Jukelyn',
        icon_url=
        'https://cdn.discordapp.com/avatars/347216701055565827/dd8d8fea4dd82a780589bc98c8854201.webp?size=160'
    )
    embed.add_field(name='Monday', value='Weekly Bosses', inline=False)
    embed.add_field(name='Tuesday', value='Diluc Talent Books', inline=False)
    embed.add_field(name='Wednesday',
                    value='Raiden Shogun Talent Scrolls',
                    inline=False)
    embed.add_field(name='Thursday',
                    value='Anything or just condense for tomorrow',
                    inline=False)
    embed.add_field(name='Friday', value='Diluc Talent Books', inline=False)
    embed.add_field(name='Saturday',
                    value='Raiden Shogun Talent Scrolls',
                    inline=False)
    embed.add_field(name='Sunday', value='Diluc Talent Books', inline=False)
    await ctx.send(embed=embed)


########################################################### Genshin Commands Above here ###########################################################

keep_alive()
botToken = os.environ['TOKEN']
client.run(botToken)
