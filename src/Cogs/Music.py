import pomice, os
from discord.ext import commands
from discord import utils


class Music(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot
        self.pomice = pomice.NodePool()

    async def start_nodes(self):
        await self.pomice.create_node(
            bot=self.bot,
            host=os.getenv('LAVALINK_HOST'),
            port=int(os.getenv('LAVALINK_PORT')),
            password=os.getenv('LAVALINK_PASSWD'),
            identifier=os.getenv('LAVALINK_NAME')
        )

    def IS_URL(self, args) -> bool:
        return args[0].startswith('http://') or args[0].startswith('https://')
    # <-------------------------------- COMMANDS ------------------------------------>


    @commands.command(name='join', aliases=['j', 'J'], help='Entrar al canal de voz')
    async def join(self, ctx):
        try:
            if ctx.author.voice is None or ctx.author.voice.channel is None:
                await ctx.send("y a dónde putas me voy a meter si no estás en un vc? Malparido tonto")

            vc = ctx.author.voice.channel
            await vc.connect(cls=pomice.Player)
            await ctx.send(f"Hora de chambear? 👀")

        except Exception as err:
            await ctx.send(f'E: `{err}`. Echenle la culpa a E y le mandan eso de mi parte')
            raise


    @commands.command(name='play', aliases=['p', 'P'], help='el bot empieza a cantar 🤑')
    async def play(self, ctx, *, query=None):
        if ctx.author.id == 1284711004831485974:
            await ctx.send('callate vos más bien')
            return

        if query:
            try:
                if not ctx.voice_client:
                    await ctx.invoke(self.join)

                player = ctx.voice_client
                results = await player.get_tracks(query)

                if not results:
                    await ctx.send("No veo resultados para ese tema, mala mía")

                if isinstance(results, pomice.Playlist):
                    await player.play(track=results.tracks[0])
                
                else:
                    await player.play(track=results[0])
            
            except Exception as err:
                await ctx.send(f'E: `{err}`. Echenle la culpa a E y le mandan eso de mi parte')
                raise
        
        else:
            await ctx.send(f"Vea bro, esta es la sintaxis: `{await self.bot.getPrefix(ctx.message)}play <nombre del tema>`")


    @commands.command(name='pause', help="Pausa la canción actual.")
    async def pause(self, ctx):
        if ctx.author.id == 1284711004831485974:
            await ctx.send('andate a dormir')
            return

        if ctx.voice_client.is_paused:
            await ctx.send('Ya está pausado tonto del culo')

        else:
            await ctx.voice_client.set_pause(True)
            await ctx.send('`Pause ⏸️` Un negro acaba de pausar la music')


    @commands.command(name='resume', aliases=['r', 'R'], help='Despausa la canción (creo)')
    async def resume(self, ctx):
        if ctx.voice_client.is_paused:
            await ctx.send('`Resume ▶️` despausao')
            await ctx.voice_client.set_pause(False)
        
        elif ctx.voice_client.is_playing:
            await ctx.send('qué mierda quieres hacer? Si la música ya está sonando')

        else:
            await ctx.send('mi hermano, no está sonando ningún tema y vos lo querés despausar, sos estúpido o respiras por el culo? 😍😍😍😍')


    @commands.command(help='Cambia el volumen de esa vuelta', aliases=['v', 'V'])
    async def volume(self, ctx, value=None):
        if ctx.author.id == 1284711004831485974:
            await ctx.send('cansona detectada')
            return

        if ctx.author.voice and ctx.voice_client.is_playing:
            if not value:
                await ctx.send(f'Ahora mismo estamos al {ctx.voice_client.volume}% 🔊')
        
            elif int(value):
                await ctx.voice_client.set_volume(int(value))
                await ctx.send(f' 🔊 {value}%')


    @commands.command(name='leave', aliases=['l', 'L'], help='hace que el bot se vaya a comprar cigarros')
    async def leave(self, ctx):
        if ctx.author.id == 1284711004831485974:
            await ctx.send("A ti te tengo que ignorar")

        if ctx.voice_client is not None:
            await ctx.voice_client.destroy()
            


async def setup(bot):
    await bot.add_cog(Music(bot))
