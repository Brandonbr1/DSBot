import discord,os,json
from discord.ext import commands

intents = discord.Intents.all()

client = commands.bot(command_prefix = '!', intents=intents )

#gets the config.json to get the token
if os.path.exists(os.getcwd() + "/config.json" ):
    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token": ""}

    with open(os.getcwd() + "/config.json", "w+" ) as f:
        json.dump(configTemplate, f)

token = configData["Token"]

@client.event()
async def on_member_join(member):
    guild =  client.get_guild(844199297523646505)
    channel = guild.get_channel(863605206301671454)
    await channel.send(f":tada: Welcome to the sever {member.mention} you joining our discord sever means so mutch to us")

@client.event()
async def on_member_leave(member):
    guild =  client.get_guild(844199297523646505)
    channel = guild.get_channel(863605206301671454)
    await channel.send(f"it looks like {member.mention} has left our discord sever it is sad but we thank {member.mention} for joining our discord sever")



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
async def load(ctx, extention):
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
    
 # delete swear word   
@client.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    msg_content = message.content.lower()

    curseWord = ['fuck', 'dick', "shit", "asshole", "cunt", "bitch", "Pussy", "Cock","Dickhead", "Motherfucker"]
    
    if any(word in msg_content for word in curseWord):
        await message.delete(*, delay=None)
       
       
@Client.command(pass_context = True)
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in Client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await Client.delete_messages(mgs)
    
@client.event(pass_context = True)
async def on_message(message,ctx):
  	response = await message.channel.send("Hello") 
	await ctx.send('Hi')

@client.event(pass_context = True)
async def on_message(message,ctx):
  	response = await message.channel.send("Hi") 
	await ctx.send('Hello')
    
#run the bot
client.run(token)

