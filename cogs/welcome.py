import discord.py
from discord.ext import commands


Class Welcomer(commands.cog)
    def __init__(self,client)
    self.client = client


    @commands.cog.listener()
    async def on_member_join(member):
    guild =  client.get_guild(844199297523646505)
    channel = guild.get_channel(863605206301671454)
    await channel.send(f":tada: Welcome to the sever {member.mention} you joining our discord sever means so mutch to us")
    





