import discord 
from discord.ext import commands

class Utils(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot


    @commands.command(name='clear', aliases=['c'], help='Borra la cantidad de mensajes indicada (por defecto 1)')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 2):
        if amount < 1:
            return await ctx.send("❌ Debes especificar un número mayor que 0.", delete_after=5)
        
        deleted = await ctx.channel.purge(limit=amount + 1)
        confirmation = await ctx.send(f"🧹 He borrado {len(deleted)-1} mensajes.", delete_after=5)


    @commands.command(name='nuke', help='Elimina todos los mensajes del canal')
    @commands.has_permissions(manage_channels=True)
    async def nuke(self, ctx):
        channel = ctx.channel
        new_channel = await channel.clone(reason=f"Nuked by {ctx.author}")
        await channel.delete()
        await new_channel.send("💣 ¡Canal nuked!")


    @commands.command(name='help', help='Muestra este mensaje')
    async def help(self, ctx, *input):
        prefix = await self.bot.get_prefix(ctx.message)
        owner = 722465763373613088	

        if not input:
            try:
                owner = ctx.guild.get_member(owner).mention

            except AttributeError as e:
                owner = owner

            emb = discord.Embed(
                title='Lista de comandos', color=discord.Color.blurple(),
                description=f'Usa `{prefix}help <category>` para más información\n sobre esa categoría'
            )

            cogs_desc = ''
            for cog in self.bot.cogs:
                cogs_desc += f'`{cog}`\n'

            # adding 'list' of cogs to embed
            emb.add_field(name='Categorías', value=cogs_desc, inline=True)

            commands_desc = ''

            for command in self.bot.walk_commands():
            
                if not command.cog_name and not command.hidden:
                    commands_desc += f'{command.name} - {command.help}\n'

            if commands_desc:
                emb.add_field(name='No pertenece a la categoría', value=commands_desc, inline=False)


        elif len(input) == 1:

            for cog in self.bot.cogs:
                if cog.lower() == input[0].lower():

                    emb = discord.Embed(
                        title=f'{cog} - Commands', 
                        description=self.bot.cogs[cog].__doc__,
                        color=discord.Color.green()
                    )

                    for command in self.bot.get_cog(cog).get_commands():
                        if not command.hidden:
                            emb.add_field(name=f"`{prefix}{command.name}`", value=command.help, inline=False)
                    break

            else:
                emb = discord.Embed(
                    title="Comando desconocido",
                    description=f"No encontramos `{input[0]}` en la lista de comandos.",
                    color=discord.Color.blue()
                )

        elif len(input) > 1:
            emb = discord.Embed(title="Error",
                description=f"Sintaxis `{prefix}help <category>`",
                color=discord.Color.blurple()
            )

        # sending reply embed using our own function defined above
        await ctx.send(embed=emb)

async def setup(bot):
    await bot.add_cog(Utils(bot))