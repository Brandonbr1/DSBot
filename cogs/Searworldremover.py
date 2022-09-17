import discord.py
from discord.ext import commands


Class Swear(commands.cog)
    def __init__(self,client)
    self.client = client


    @commands.cog.listener(self, message, user)
    async def on_message(message):
    if message.author.id == bot.user.id:
        return
    msg_content = message.content.lower()

    curseWord = ['fuck', 'dick', "shit", "asshole", "cunt", "bitch", "Pussy", "Cock","Dickhead", "Motherfucker"]
    
    if any(word in msg_content for word in curseWord):
        await message.delete(*, delay=None)       
