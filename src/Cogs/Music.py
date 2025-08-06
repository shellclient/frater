import pomice, os, discord
from discord.ext import commands 
from datetime import datetime

class Music(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot
        self.queue = pomice.Queue(100)
        self.pomice = pomice.NodePool()

    async def start_nodes(self):
        await self.pomice.create_node(
            bot=self.bot,
            host=os.getenv('LAVALINK_HOST'),
            port=int(os.getenv('LAVALINK_PORT')),
            password=os.getenv('LAVALINK_PASSWD'),
            identifier=os.getenv('LAVALINK_NAME')
        )


    @commands.Cog.listener()
    async def on_pomice_track_end(self, player: pomice.Player, track: pomice.Track, _):
        """Se activa cuando una pista termina de reproducirse""" 
        
        if self.queue.is_empty:
            await player.stop()
            return

        # Reproducir la siguiente canción
        if self.queue.size > 0:
            await player.play(track=self.queue.get())
            


    @commands.command(name='play', aliases=['p', 'P'], help='el bot empieza a cantar 🤑')
    async def play(self, ctx, *, query=None):
        if ctx.author.id == 1284711004831485974:
            await ctx.send('callate vos más bien')
            return

        if query and ctx.author.voice:
            try:
                if not ctx.voice_client:
                    await ctx.invoke(self.join)

                player = ctx.voice_client

                if not self.queue.is_empty and not player.is_playing:
                    await player.play(track=self.queue.get())
                    return

                results = await player.get_tracks(query)

                if not results:
                    await ctx.send("No veo resultados para ese tema, mala mía")

                if isinstance(results, pomice.Playlist):
                    await player.play(track=results.tracks[0])
                    embed = discord.Embed(
                        title="Reproductor",
                        description=f"🔊 Reproduciendo a continuación:\n[{results[0].title}]({results[0].uri})",
                        colour=0x00b0f4,
                        timestamp=datetime.now()
                    )
                    embed.set_footer(text="Frater")

                    await ctx.send(embed=embed)
                
                else:
                    await player.play(track=results[0])
                    embed = discord.Embed(
                        title="Reproductor",
                        description=f"🔊 Reproduciendo a continuación:\n[{results[0].title}]({results[0].uri})",
                        colour=0x00b0f4,
                        timestamp=datetime.now()
                    )
                    embed.set_footer(text="Frater")

                    await ctx.send(embed=embed)
            
            except Exception as err:
                await ctx.send(f'E: `{err}`. Echenle la culpa a E y le mandan eso de mi parte')
                raise
        
        elif not query and ctx.author.voice:
            if not self.queue.is_empty and not player.is_playing:
                track = self.queue.get()
                await player.play(track=track)
                embed = discord.Embed(
                    title="Reproductor",
                    description=f"🔊 Reproduciendo a continuación:\n[{track.title}]({track.uri})",
                    colour=0x00b0f4,
                    timestamp=datetime.now()
                )
                embed.set_footer(text="Frater")

                await ctx.send(embed=embed)
                return

        else:
            await ctx.send(f"Vea bro, esta es la sintaxis: `{await self.bot.get_prefix(ctx.message)}play <nombre del tema>` (sobra decir que tienes que estar en vc)")
    
    
    @commands.command(name='q', aliases=['Q'], help='Listar canción a la cola')
    async def q(self, ctx, *, query=None):
        if ctx.author.id == 1284711004831485974:
            await ctx.send('callate vos más bien')
            return
        
        if not query:
            await ctx.send(f"En la cola hay **{self.queue.size}** canciones")
            return
        
        if query and ctx.author.voice:
            try:
                if not ctx.voice_client:
                    await ctx.invoke(self.join)

                player = ctx.voice_client
                
                results = await player.get_tracks(query)

                if not results:
                    await ctx.send("No veo resultados para ese tema, mala mía")
                    return

                if isinstance(results, pomice.Playlist):
                    print('playlist')
                    if len(results.tracks) > 100:
                        await ctx.send("Playlist demasiado grande. Límite: 100 canciones.")
                        return
                    
                    for track in results.tracks:
                        self.queue.put(track)

                    await ctx.send(f"**{len(results.tracks)}** canciones añadidas a la cola")
                    await player.play(self.queue.get())

                    embed = discord.Embed(
                        title="Reproductor",
                        description=f"❕ Añadiendo a la lista de reproducción:\n[{results[0].title}]({results[0].uri})",
                        colour=0x00b0f4,
                        timestamp=datetime.now()
                    )
                    embed.set_footer(text="Frater")

                    await ctx.send(embed=embed)

                
                else:
                    size = self.queue.size
                    self.queue.put(results[0])
                    embed = discord.Embed(
                        title="Reproductor",
                        description=f"❕ Añadiendo a la lista de reproducción:\n[{results[0].title}]({results[0].uri})",
                        colour=0x00b0f4,
                        timestamp=datetime.now()
                    )
                    embed.set_footer(text="Frater")
                    await ctx.send(embed=embed)

                    if size == 0 and not player.is_playing:
                        track = self.queue.get()
                        
                        await player.play(track)

                        embed = discord.Embed(
                            title="Reproductor",
                            description=f"🔊 Reproduciendo a continuación:\n[{track.title}]({track.uri})",
                            colour=0x00b0f4,
                            timestamp=datetime.now()
                        )
                        embed.set_footer(text="Frater")

                        await ctx.send(embed=embed)

            
            except Exception as err:
                await ctx.send(f'E: `{err}`. Echenle la culpa a E y le mandan eso de mi parte')
                raise


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


    @commands.command(name='pause', help="Pausa la canción actual.")
    async def pause(self, ctx):
        if ctx.author.id == 1284711004831485974:
            await ctx.send('andate a dormir')
            return

        if ctx.voice_client.is_paused and ctx.author.voice:
            await ctx.send('Ya está pausado tonto del culo')

        else:
            await ctx.voice_client.set_pause(True)
            await ctx.send('`Pause ⏸️` Un negro acaba de pausar la music')


    @commands.command(name='resume', aliases=['r', 'R'], help='Despausa la canción (creo)')
    async def resume(self, ctx):
        if ctx.voice_client.is_paused and ctx.author.voice:
            await ctx.send('`Resume ▶️` despausao')
            await ctx.voice_client.set_pause(False)
        
        elif ctx.voice_client.is_playing and ctx.author.voice:
            await ctx.send('qué mierda quieres hacer? Si la música ya está sonando')

        else:
            await ctx.send('mi hermano, no está sonando ningún tema y vos lo querés despausar, sos estúpido o respiras por el culo? 😍😍😍')


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
