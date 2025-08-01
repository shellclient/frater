import discord
from datetime import datetime
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.deleted_msgs = []


    @commands.Cog.listener()
    async def on_message_delete(self, m) -> object:
        if len(self.deleted_msgs):
            
            self.deleted_msgs.insert(0, {
            'guild_id': str(m.author.guild.id),
            'author': m.author,
            'content': m.content,
            'avatar': m.author.avatar
            })
        else:
            self.deleted_msgs.insert(0, {
                'guild_id': str(m.author.guild.id),
                'author': m.author,
                'content': m.content,
                'avatar': m.author.avatar
            })   

    @commands.command(name='snipe', aliases=['sn'], help='recupera el último mensaje borrao')
    async def snipe(self, ctx):
        if len(self.deleted_msgs):
            for i in range(len(self.deleted_msgs)):
                print(list(enumerate(self.deleted_msgs[i])))
                if self.deleted_msgs[i]['guild_id'] == str(ctx.author.guild.id):
                    embed=discord.Embed(description=f"{self.deleted_msgs[i]['content']}", color=0x9900ff)
                    embed.set_author(name=f"{self.deleted_msgs[i]['author']}", icon_url=f"{self.deleted_msgs[i]['avatar']}")
                    embed.set_footer(text=f"{datetime.now().strftime('%x %I:%M %p')}")
                    await ctx.send(embed=embed)
                    del self.deleted_msgs[i]
        else:
            await ctx.send("No hay mensajes eliminados, pero estoy vigilando. ಠ_ಠ")

    
    @commands.command(name='say', description='hacer que el bot diga algo')
    @commands.has_permissions(manage_messages=True, moderate_members=True)
    async def say(self, ctx, *, args):
        await ctx.send(args)
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(Fun(bot))