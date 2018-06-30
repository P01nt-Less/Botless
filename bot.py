import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import time
import math

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), description='The one, and only: Botless, created by Pointless#1278.', self_bot=False)
bot.remove_command('help')

def pointcheck(ctx):
    return ctx.message.author.id == '276043503514025984' #checks if @Pointless#1278 is the author of the command

@bot.event
async def on_ready():
    print('Bot online!')
    print('Name: {}'.format(str(bot.user)))
    print('ID: {}'.format(str(bot.user.id)))
    print('Invite Link: https://discordapp.com/oauth2/authorize?client_id=462562571229200384&scope=bot&permissions=2146958591')

'''
'##::::'##:'########:'##:::::::'########::                                                                                      
 ##:::: ##: ##.....:: ##::::::: ##.... ##:                                                                                      
 ##:::: ##: ##::::::: ##::::::: ##:::: ##:                                                                                      
 #########: ######::: ##::::::: ########::                                                                                      
 ##.... ##: ##...:::: ##::::::: ##.....:::                                                                                      
 ##:::: ##: ##::::::: ##::::::: ##::::::::                                                                                      
 ##:::: ##: ########: ########: ##::::::::                                                                                      
..:::::..::........::........::..:::::::::     '''

@bot.command(pass_context=True,brief='Shows a list of commands.')
async def help(ctx, helpc: str = None):
    '''!help [command]'''
    if helpc == None:
        hhelp=discord.Embed(title='Help', color=0x0000FF)
        hhelp.add_field(name='General', value='`help` `ping`')
        hhelp.add_field(name='Informational', value='')
        hhelp.add_field(name='Fun', value='')
        hhelp.add_field(name='Managing', value='`giverole` `takerole`,')
        hhelp.add_field(name='Moderation', value='`kick` `ban` `unban` `softban`')
        hhelp.add_field(name='Owner', value='`say`, `restart`')
        hhelp.set_footer(text='Do !help <command> to find out what it does.\nI\'m a bot that has commands that are yet to come!')
        await bot.say(embed=hhelp)
    if helpc:
        helpget = bot.get_command(helpc)
        shelp=discord.Embed(title='Help', color=0x0000FF)
        shelp.add_field(name=f'Command: !{helpc}',value=f'Help: {helpget.brief}\nUsage: {helpget.help}')
        return await bot.say(embed=shelp)
    else:
        return

'''
:'#######::'##:::::'##:'##::: ##:'########:'########::                                                                          
'##.... ##: ##:'##: ##: ###:: ##: ##.....:: ##.... ##:                                                                          
 ##:::: ##: ##: ##: ##: ####: ##: ##::::::: ##:::: ##:                                                                          
 ##:::: ##: ##: ##: ##: ## ## ##: ######::: ########::                                                                          
 ##:::: ##: ##: ##: ##: ##. ####: ##...:::: ##.. ##:::                                                                          
 ##:::: ##: ##: ##: ##: ##:. ###: ##::::::: ##::. ##::                                                                          
. #######::. ###. ###:: ##::. ##: ########: ##:::. ##:                                                                          
:.......::::...::...:::..::::..::........::..:::::..::  '''
@bot.command(pass_context=True,brief='Says something as the bot.')
@commands.check(pointcheck)
async def say(ctx, *, text: str = None):
    '''!say <text>'''
    await bot.delete_message(ctx.message)
    await bot.say(text)

@bot.command(pass_context=True,brief='Restart the bot.')
@commands.check(pointcheck)
async def restart(ctx):
    '''!restart'''
    embed = discord.Embed(title='Restart',description=f'Sorry, but {ctx.message.author.mention} has forced me to restart. It\'ll only take a moment!',color=0xFF0000)
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=embed)
    await bot.logout()

'''
:'######:::'########:'##::: ##:'########:'########:::::'###::::'##:::::::                                                       
'##... ##:: ##.....:: ###:: ##: ##.....:: ##.... ##:::'## ##::: ##:::::::                                                       
 ##:::..::: ##::::::: ####: ##: ##::::::: ##:::: ##::'##:. ##:: ##:::::::                                                       
 ##::'####: ######::: ## ## ##: ######::: ########::'##:::. ##: ##:::::::                                                       
 ##::: ##:: ##...:::: ##. ####: ##...:::: ##.. ##::: #########: ##:::::::                                                       
 ##::: ##:: ##::::::: ##:. ###: ##::::::: ##::. ##:: ##.... ##: ##:::::::                                                       
. ######::: ########: ##::. ##: ########: ##:::. ##: ##:::: ##: ########:                                                       
:......::::........::..::::..::........::..:::::..::..:::::..::........::        '''

@bot.command(pass_context=True,aliases=['latency','pong'],brief='Shows the response time in milliseconds.')
async def ping(ctx):
    '''!ping'''
    ptime = time.time()
    embed=discord.Embed(Title = 'Ping', color = 0x00FF00)
    embed.add_field(name = 'Pong!', value = 'Calculating...')
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    ping3=await bot.say(embed=embed)
    ping2=time.time() - ptime 
    ping1=discord.Embed(Title = 'Ping', color = 0x00FF00)
    ping1.add_field(name='Pong!', value='{} milliseconds.'.format(int((round(ping2 * 1000)))))
    ping1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.edit_message(ping3,embed=ping1)


'''
'##::::'##::::'###::::'##::: ##::::'###:::::'######:::'####:'##::: ##::'######:::                                               
 ###::'###:::'## ##::: ###:: ##:::'## ##:::'##... ##::. ##:: ###:: ##:'##... ##::                                               
 ####'####::'##:. ##:: ####: ##::'##:. ##:: ##:::..:::: ##:: ####: ##: ##:::..:::                                               
 ## ### ##:'##:::. ##: ## ## ##:'##:::. ##: ##::'####:: ##:: ## ## ##: ##::'####:                                               
 ##. #: ##: #########: ##. ####: #########: ##::: ##::: ##:: ##. ####: ##::: ##::                                               
 ##:.:: ##: ##.... ##: ##:. ###: ##.... ##: ##::: ##::: ##:: ##:. ###: ##::: ##::                                               
 ##:::: ##: ##:::: ##: ##::. ##: ##:::: ##:. ######:::'####: ##::. ##:. ######:::                                               
..:::::..::..:::::..::..::::..::..:::::..:::......::::....::..::::..:::......::::    '''

@bot.command(pass_context=True,aliases=['gr'],brief='Give roles to members.')
async def giverole(ctx, member: discord.Member, *, role: discord.Role = None):
    '''!giverole <member> <role>'''
    if not ctx.message.author.server_permissions.manage_roles:
        pgiverole=discord.Embed(title='Error',description='You don\'t have permission to give roles to members!',color=0xFF0000)
        pgiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=pgiverole)
    if not member:
        mgiverole=discord.Embed(title='Error',description='You must specify a member!',color=0xFF0000)
        mgiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=mgiverole)
    if not role:
        rgiverole=discord.Embed(title='Error',description='You must specify a role!',color=0xFF0000)
        rgiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rgiverole)
    if role not in ctx.message.server.roles:
        ngiverole=discord.Embed(title='Error',description='That isn\'t a role!',color=0xFF0000)
        ngiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ngiverole)
    try:
        rolegive = discord.utils.get(ctx.message.server.roles, name=role)
        await bot.add_roles(member, role)
        sgiverole=discord.Embed(title='Giverole',description=f'{ctx.message.author.mention} has given the role, {role}, to {member.name}!',color=0x00FF00)
        sgiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=sgiverole)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            egiverole=discord.Embed(title='Error',description='The person you are trying to give a role to has high permissions.',color=0xFF0000)
            egiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=egiverole)
        else:
            pass
@bot.command(pass_context=True,aliases=['tr'],brief='Take roles from members')
async def takerole(ctx, member: discord.Member, *, role: discord.Role = None):
    '''!takerole <member> <role>'''
    if not ctx.message.author.server_permissions.manage_roles:
        ptakerole=discord.Embed(title='Error',description='You don\'t have permission to give roles to members!',color=0xFF0000)
        ptakerole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ptakerole)
    if not member:
        mtakerole=discord.Embed(title='Error',description='You must specify a member!',color=0xFF0000)
        mtakerole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=mtakerole)
    if not role:
        rtakerole=discord.Embed(title='Error',description='You must specify a role!',color=0xFF0000)
        rtakerole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rtakerole)
    if role not in ctx.message.server.roles:
        ntakerole=discord.Embed(title='Error',description='That isn\'t a role!',color=0xFF0000)
        ntakeerole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=ntakerole)
    try:
        await bot.remove_roles(member, role)
        stakerole=discord.Embed(title='Takerole',description=f'{ctx.message.author.mention} has taken the role, {role}, from {member.name}!',color=0x00FF00)
        stakerole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        await bot.say(embed=stakerole)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            egiverole=discord.Embed(title='Error',description=f'The person you are trying to take a role from has high permissions.',color=0xFF0000)
            egiverole.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=etakerole)
        else:
            pass

'''
'##::::'##::'#######::'########::'########:'########:::::'###::::'########:'####::'#######::'##::: ##:                          
 ###::'###:'##.... ##: ##.... ##: ##.....:: ##.... ##:::'## ##:::... ##..::. ##::'##.... ##: ###:: ##:                          
 ####'####: ##:::: ##: ##:::: ##: ##::::::: ##:::: ##::'##:. ##::::: ##::::: ##:: ##:::: ##: ####: ##:                          
 ## ### ##: ##:::: ##: ##:::: ##: ######::: ########::'##:::. ##:::: ##::::: ##:: ##:::: ##: ## ## ##:                          
 ##. #: ##: ##:::: ##: ##:::: ##: ##...:::: ##.. ##::: #########:::: ##::::: ##:: ##:::: ##: ##. ####:                          
 ##:.:: ##: ##:::: ##: ##:::: ##: ##::::::: ##::. ##:: ##.... ##:::: ##::::: ##:: ##:::: ##: ##:. ###:                          
 ##:::: ##:. #######:: ########:: ########: ##:::. ##: ##:::: ##:::: ##::::'####:. #######:: ##::. ##:                          
..:::::..:::.......:::........:::........::..:::::..::..:::::..:::::..:::::....:::.......:::..::::..::   '''
@bot.command(pass_context=True,brief='Kick members.')
async def kick(ctx, member : discord.Member=None,*, reason='The kick hammer has spoken!'):
    '''!kick <member> [reason]'''
    if not ctx.message.author.server_permissions.kick_members:
        pkick=discord.Embed(title='Error',description='You don\'t have permission to kick members!',color=0xFF0000)
        pkick.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=pkick)
    if not member:
        mkick=discord.Embed(title='Error',description='You must specify a member!',color=0xFF0000)
        mkick.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=mkick)
    if not reason:
        rkick=discord.Embed(title='Error',description='You must specify a reason!',color=0xFF0000)
        rkick.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rkick)
    try:
        await bot.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            ekick=discord.Embed(title='Error',description='The person you are trying to kick has high permissions.',color=0xFF0000)
            ekick.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=ekick)
        else:
            pass
    skick=discord.Embed(title='Kick',description=f'{ctx.message.author.mention} has kicked {member.name}, because: {reason}',color=0x00FF00)
    skick.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=skick)
    return await bot.send_message(member, f'You have been kicked from {discord.Server.name} by {ctx.message.author.mention}, because {reason}', tts=True) 

@bot.command(pass_context=True,brief='Ban members.')
async def ban(ctx, member : discord.Member=None,*, reason='The ban hammer has spoken!'):
    '''!ban <member> [reason]'''
    if not ctx.message.author.server_permissions.kick_members:
        pban=discord.Embed(title='Error',description='You don\'t have permission to ban members!',color=0xFF0000)
        pban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=pban)
    if not member:
        mban=discord.Embed(title='Error',description='You must specify a member!',color=0xFF0000)
        mban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=mban)
    if not reason:
        rban=discord.Embed(title='Error',description='You must specify a reason!',color=0xFF0000)
        rban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rban)
    try:
        await bot.ban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            eban=discord.Embed(title='Error',description='The person you are trying to ban has high permissions.',color=0xFF0000)
            eban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=eban)
        else:
            pass
    sban=discord.Embed(title='Ban',description=f'{ctx.message.author.mention} has banned {member.name}, because: {reason}',color=0x00FF00)
    sban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=sban)
    return await bot.send_message(member, f'You have been banned from {discord.Server.name} by {ctx.message.author.mention}, because {reason}', tts=True) 

@bot.command(pass_context=True,brief='Unban members.')
async def unban(ctx, member : discord.Member=None,*, reason='The unban hammer has spoken!'):
    '''!unban <member> [reason]'''
    await bot.say('May not work currently, but I\'ll give it a go!')
    if not ctx.message.author.server_permissions.kick_members:
        punban=discord.Embed(title='Error',description='You don\'t have permission to unban members!',color=0xFF0000)
        punban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=punban)
    if not member:
        munban=discord.Embed(title='Error',description='You must specify a member!',color=0xFF0000)
        munban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=munban)
    if not reason:
        runban=discord.Embed(title='Error',description='You must specify a reason!',color=0xFF0000)
        runban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=runban)
    try:
        await bot.unban(discord.Server,member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            eunban=discord.Embed(title='Error',description='The person you are trying to unban has high permissions.',color=0xFF0000)
            eunban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=eunban)
        else:
            pass
    sunban=discord.Embed(title='Unban',description=f'{ctx.message.author.mention} has unbanned {member.name}, because: {reason}',color=0x00FF00)
    sunban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=unban)
    return await bot.send_message(member, f'You have been unbanned from {discord.Server.name} by {ctx.message.author.mention}, because {reason}', tts=True) 

@bot.command(pass_context=True,brief='Ban then unban someone to clear all messages within 7 days.')
async def softban(ctx, member : discord.Member=None,*, reason='The softban hammer has spoken!'):
    '''!softban <member> [reason]'''
    if not ctx.message.author.server_permissions.kick_members:
        psoftban=discord.Embed(title='Error',description='You don\'t have permission to softban members!',color=0xFF0000)
        psoftban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=psoftban)
    if not member:
        msoftban=discord.Embed(title='Error',description='You must specify a member!',color=0xFF0000)
        msoftban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=msoftban)
    if not reason:
        rsoftban=discord.Embed(title='Error',description='You must specify a reason!',color=0xFF0000)
        rsoftban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        return await bot.say(embed=rsoftban)
    try:
        await bot.ban(member, delete_message_days=7)
        await bot.unban(discord.Server,member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            esoftban=discord.Embed(title='Error',description='The person you are trying to softban has high permissions.',color=0xFF0000)
            esoftban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            return await bot.say(embed=esoftban)
        else:
            pass
    ssoftban=discord.Embed(title='Softban',description=f'{ctx.message.author.mention} has softbanned {member.name}, because: {reason}',color=0x00FF00)
    ssoftban.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=ssoftban)
    return await bot.send_message(member, f'You have been softbanned from {discord.Server.name} by {ctx.message.author.mention}, because {reason}', tts=True) 

bot.run(os.environ.get('TOKEN'))