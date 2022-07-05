import discord.py
from discord.ext import commands


Class Bye(commands.cog)
    def __init__(self,client)
    self.client = client


    @commands.cog.listener()
    async def on_member_leave(self, ctx,member):
    guild =  client.get_guild(844199297523646505)
    channel = guild.get_channel(863605206301671454)
    await channel.send(f":tada: {member.mention just left the sever")
