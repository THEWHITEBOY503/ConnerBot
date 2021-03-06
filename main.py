#Conner Bot. Version 2.0


#Starting the bot
print('Starting Conner Bot')
import discord
import asyncio
import datetime as dt
from discord.ext import commands
bot = commands.Bot(command_prefix='_')
starttime = dt.datetime.utcnow()
bot.remove_command("help")

#What happens after the bot has started
@bot.event
async def on_ready():
    print('Ready!')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='_help'))


#Commands
@bot.event
async def on_message(message):
    if message.content.startswith('_hi'):
        #ech
        print('Ran _hi')
#Add new lines with this:
#@bot.command(name='commandname', pass_context=True)
#async def commandname(ctx):
#Then go to the bottom of this file

    @bot.command(name='help', pass_context=True)
    async def help(ctx):
        await bot.send_message(message.channel, 'Ok. I have attempted to DM you my commands. If you did not get a DM, check your server settings')
        embed=discord.Embed(title="Commands", color=0x2db0ff)
        embed.set_author(name="Conner Bot", url='https://discord.gg/usWqeSF', icon_url='https://media.discordapp.net/attachments/354388052178894869/380138617592610827/mountain_grid___vaporwave_by_davidfigueira-db1ug68.jpg')
        #Add a line using embed.add_field(name="Text", value="Subtext", inline=False)
        embed.add_field(name="_help", value="DMs you this screen", inline=False)
        embed.add_field(name="_donate", value="Gives you a link to donate to me.", inline=False)
        embed.add_field(name="_ping", value="Runs a speedtest.", inline=False)
        embed.add_field(name="_cmds", value="Shows beta commands.", inline=False)
        embed.add_field(name="_kick", value="Kicks a user. Tag a user to be kicked.", inline=False)
        embed.add_field(name="_ban", value="Bans a user. Tag a user to be banned.", inline=False)
        embed.add_field(name="cb.leaderboard", value="Check where you are on the ConnerBot message leaderboard", inline=False)
        emebd.add_field(name="cb.profile", value="See your current level and XP count", inline=False)
        embed.set_footer(text="Yaw YEET")
        await bot.send_message(message.author, embed=embed)
        print('Ran help')
        bot.remove_command("help")

    @bot.command(name='donate', pass_context=True)
    async def donate(ctx):
        await bot.send_message(message.channel, 'Conner Bot runs on a GCP free tier. Consider donating.')
        await bot.send_message(message.channel, 'https://paypal.me/THEWHITEBOY503')
        await bot.send_message(message.channel, 'If you would rather donate bitcoin, my address is 1NfwCX46Qh1AviveQPupEM1mCj2ncPAVn3 https://a.doko.moe/nwbcnf.jpeg')
        print('Ran donate')

    @bot.command(name='ver', pass_context=True)
    async def ver(ctx):
        await bot.send_message(message.channel, 'Conner Bot v2.2')
        print('Ran ver')

    @bot.command(name='ping', pass_context=True)
    async def ping(ctx):
        message_time = message.timestamp
        localtime = dt.datetime.utcnow()
        lagtime = (localtime - message_time) / 2
        await bot.send_message(message.channel, f"Pong! {lagtime.microseconds / 1000}ms")
        print('Ran ping')
        print(f"Ping: {lagtime.microseconds / 1000}ms")

    @bot.command(name='cmds', pass_context=True)
    async def cmds(ctx):
        await bot.send_message(message.channel, 'Check your DMs')
        embed=discord.Embed(title="Extra Commands", color=0x2db0ff)
        embed.set_author(name="Conner Bot", url='https://discord.gg/usWqeSF', icon_url='https://media.discordapp.net/attachments/354388052178894869/380138617592610827/mountain_grid___vaporwave_by_davidfigueira-db1ug68.jpg')
        embed.add_field(name="_ver", value="Shows my version", inline=False)
        embed.add_field(name="_uptime", value="Shows the bots uptime", inline=False)
        embed.add_field(name="_info", value="Some info about me", inline=False)
        embed.add_field(name="_connerweb", value="The bot isn't finished", inline=False)
        embed.set_footer(text="haha you probably won't use these")
        await bot.send_message(message.author, embed=embed)
        print('Ran _cmds')

    @bot.command(name='uptime', pass_context=True)
    async def uptime(ctx):
        await bot.send_message(message.channel, f"{dt.datetime.utcnow() - starttime}")
        print('Ran _uptime')
        print(f"Uptime: {dt.datetime.utcnow() - starttime}")

    @bot.command(name='connerweb', pass_context=True)
    @commands.has_permissions(send_messages=True)
    async def connerweb(ctx):
        await bot.send_message(message.channel, 'http://connerbot.tk')
        print('Ran _connerweb')

    @bot.command(name='kick', pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member:discord.Member):
        await bot.kick(member)
        await bot.send_message(message.channel, 'User has been kicked.')
        print('Ran _kick')

    @bot.command(name='ban', pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, member:discord.Member):
        await bot.ban(member)
        await bot.send_message(message.channel, 'User has been banned. May they never come back.')
        print('Ran _ban')
        bot.remove_command("ban")

    #make sure the weather update script is running or this will be out of date
    @bot.command(name='weather', pass_context=True)
    async def var(ctx):
        await bot.send_file(message.channel, 'weather.png')

    @bot.command(name='leaderboard', pass_context=True)
    async def var(ctx):
        await bot.send_message(message.channel, 'Hm, there seems to be a mistake... Were you trying to run `cb.leaderboard`?')

    @bot.command(name='profile', pass_context=True)
    async def var(ctx):
        await bot.send_message(message.channel, 'Hm, there seems to be a mistake... Were you trying to run `cb.profile`?')


#These prevent the bot from breaking. When you add a new command, give them a bot.remove_command
    await bot.process_commands(message)
    bot.remove_command("help")
    bot.remove_command("donate")
    bot.remove_command("ver")
    bot.remove_command("ping")
    bot.remove_command("cmds")
    bot.remove_command("uptime")
    bot.remove_command("connerweb")
    bot.remove_command("kick")
    bot.remove_command("ban")
    bot.remove_command("weather")
    bot.remove_command("leaderboard")
    bot.remove_command("profile")

#Tells Conner Bot who it is. Don't leak this token.
bot.run('token here')
