from webserver import keep_alive
import discord
import os
import json
import DiscordUtils
from discord.ext import commands
from io import BytesIo

intents = discord.Intents.all()

client = commands.bot(command_prefix = '!', intents=intents )

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements to execute this command you need to be an admin/mod :angry:")

#ban player.
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

#unbans player.
@client.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

# cogs
@client.command()
async def load(ctx, extention):
    client.load_extension(f'cogs.{extention}')

@client.command()
async def unload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#kick user
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason="no reason provided you probally broken on of the rule on the discord sever"
    await ctx.guild.kick(member)
    await ctx.send(f'User {member.mention} has been kicked for {reason}')



# level system
@client.event
async def on_member_join(member):
    with open('levels.json', 'r') as f:
        users = json.load(f)


    await update_data(users, member)

    with open('levels.json', 'w') as f:
        json.dump(users, f)

@client.event
async def on_message(message):
    with open('levels.json', 'r') as f:
        users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author , 5)
        await level_up(users, message.author, message.channel)

    with open('levels.json' , 'r') as f:
        json.dump(users, f)

async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['experience'] = 0
        users[user.id]['level'] = 1

async def add_experience(users, user, exp):
    users[user.id]['experience'] += exp

async def level_up(users, user , channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
        await client.send_message(channel, '{} has leveled up to level {}'.format(user.mention, lvl_end))
        users[user.id]['level'] = lvl_end
    
#mute    
@client.command(ctx)
@commands.has_permissions(kick_members=True)
async def mute(ctx, role:discord.Role, user: discord.Member):
    await user.add_roles(muterole)
    await ctx.send(f'{user.metion} was muted')
 
#unmute 
@client.command(ctx)
@commands.has_permissions(kick_members=True)
async def unmute(ctx, role:discord.Role, user: discord.Member):
    await user.remove_roles(muterole)
    await ctx.send(f'{user.metion} was unmuted')
   
#info about user   
userinfo = bot.get_user(user_id)

async def userinfo(ctx, *, user: discord.User)
    await ctx.send(f'getting {userinfo} info')

       
       
@Client.command(pass_context = True)
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in Client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await Client.delete_messages(mgs)
    
@client.event(pass_context = True)
async def on_message(message,ctx):
    ChannelGet = await Channel.send(text)
    await ChannelGet.add_reaction('👋')
  	response = await message.channel.send("Hello") 
	await ctx.send('Hi')

@client.event(pass_context = True)
async def on_message(message,ctx):
    ChannelGet = await Channel.send(text)
    await ChannelGet.add_reaction('👋')
  	response = await message.channel.send("Hi") 
	await ctx.send('Hello')
    
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")

@client.command(ctx)
async def aboutbrandonbr1(message, ctx):
    await ctx.send("I am a Male who lives somewhere in Trinadad and Tobago like and to develop modpack,mods,plugins,addons for minecraft as a hobby and I also like helping people in open source projects my peffered pronouns are: he/him")


@client.command(ctx)
async def discordinvite(message, ctx)
    await ctx.send("permanent discord invite link:https://discord.gg/ekwhqs6ubz") 

@client.command(ctx)
async def mylinks(message, ctx)
    embed=discord.Embed(title="Link", url="https://linktr.ee/jerios", description="linktree:https://linktr.ee/jerios Website:https://brandonbr1.github.io/ weebly website:https://brandonmohammed666.weebly.com/ Github:https://github.com/Brandonbr1 Reddit:https://www.reddit.com/user/Thedemon_slayerlove Youtube:https://www.youtube.com/channel/UCcKah14SCQeg_jB39d_ok0g?sub_confirmation=1 Twitter:https://twitter.com/BrandonM666_ Curseforge:https://www.curseforge.com/members/brandonmohammed666/projects PMC:https://www.planetminecraft.com/member/mohammedbrandon/ Website:https://www.minecraftforum.net/members/brandon7579898", color=0xFF5733)
    await ctx.send(embed=embed)
    
#@client.command(ctx)
#async def commands(message, ctx)
#    embed=discord.Embed(title="Link", url="https://linktr.ee/jerios", description="commands: !aboutbrandon  !mylinks !discordinvite ", color=0xFF5733)
#    await ctx.send(embed=embed)

    
#run the bot
client.run(TOKEN)

