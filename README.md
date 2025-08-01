# 🎵 Frater Bot

![Python](https://img.shields.io/badge/python-v3.13+-blue.svg)
![Discord.py](https://img.shields.io/badge/discord.py-v2.0+-blue.svg)
![Pomice](https://img.shields.io/badge/pomice-latest-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Un bot (muy básico) de música para Discord construido con Python, que incluye reproducción de música, comandos divertidos y utilidades para el servidor.

## ✨ Características

### 🎶 Comandos de Música
- **Reproducir música** desde YouTube, Spotify y otras fuentes
- **Gestión de cola** con soporte para listas de reproducción
- **Control de volumen** y efectos de audio
- **Gestión de canales de voz** (unirse/salir)
- **Funcionalidad de pausa/reanudar**

### 🎭 Comandos Divertidos  
- **Snipe de mensajes** - Recuperar mensajes eliminados
- **Comando say** - Hacer que el bot diga mensajes personalizados
- **Respuestas interactivas** con personalidad

### 🛠️ Comandos de Utilidad
- **Gestión de mensajes** - Borrar mensajes en lotes
- **Nuke de canal** - Reiniciar completamente canales
- **Sistema de ayuda personalizado** - Documentación organizada de comandos
- **Control de acceso** basado en permisos

## 🚀 Inicio Rápido

### Requisitos Previos
- Python 3.12+
- Token de Bot de Discord
- Servidor Lavalink (para funcionalidad de música)

### Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/shellclient/frater.git
   cd frater
   ```

2. **Instalar dependencias**
   ```bash
   pip install pipenv
   pipenv shell      # <--- Iniciar el entorno
   pipenv install    # <--- Instalar dependencias
   ```

3. **Configurar variables de entorno**
   Crear un archivo `.env` en el directorio raíz:
   ```env
   TOKEN=tu_token_del_bot_de_discord
   PREFIX=!
   LAVALINK_HOST=localhost
   LAVALINK_PORT=2333
   LAVALINK_PASSWD=youshallnotpass
   LAVALINK_NAME=default-node
   ```

4. **Ejecutar el bot**
   En modo desarrollo:
   ```bash
   pipenv run dev
   ```

   Normal:
   ```bash
   python -m src.index 
   ```

## 🎵 Configuración de Lavalink

Para la funcionalidad de música, necesitas un servidor Lavalink ejecutándose:

1. Descargar Lavalink desde [aquí](https://github.com/freyacodes/Lavalink/releases)
2. Configurar `application.yml`
3. Ejecutar Lavalink: `java -jar Lavalink.jar`

## 📝 Comandos

### Música
| Comando | Alias | Descripción |
|---------|-------|-------------|
| `!play <canción>` | `!p` | Reproducir música de varias fuentes |
| `!join` | `!j` | Unirse a tu canal de voz |
| `!leave` | `!l` | Salir del canal de voz |
| `!pause` | - | Pausar la pista actual |
| `!resume` | `!r` | Reanudar reproducción |
| `!volume <1-100>` | `!v` | Cambiar volumen de reproducción |

### Diversión
| Comando | Descripción |
|---------|-------------|
| `!snipe` | Recuperar el último mensaje eliminado |
| `!say <mensaje>` | Hacer que el bot diga algo |

### Utilidades
| Comando | Descripción |
|---------|-------------|
| `!clear <cantidad>` | Eliminar número especificado de mensajes |
| `!nuke` | Reiniciar todo el canal |
| `!help [categoría]` | Mostrar comandos disponibles |

## 🏗️ Estructura del Proyecto

```
frater/
├── src/
│   ├── Cogs/
│   │   ├── Music.py    # Funcionalidad de música
│   │   ├── Fun.py      # Comandos de entretenimiento
│   │   └── Utils.py    # Comandos de utilidad
│   └── index.py        # Archivo principal del bot
├── Pipfile             # Dependencias
├── .env               # Variables de entorno
└── README.md          # ¡Estás aquí!
```

## 🔧 Desarrollo

### Ejecutar en modo desarrollo
```bash
pipenv run dev
```

Esto usa `nodemon` para reiniciar automáticamente el bot cuando los archivos cambien.

### Agregar nuevos comandos
1. Crear comandos en el archivo Cog apropiado
2. Usar el decorador `@commands.command()`
3. Agregar manejo de errores adecuado y texto de ayuda

## 🤝 Contribuir

1. Hacer fork del repositorio
2. Crear una rama de característica (`git checkout -b feature/caracteristica-increible`)
3. Confirmar tus cambios (`git commit -m 'Agregar característica increíble'`)
4. Subir a la rama (`git push origin feature/caracteristica-increible`)
5. Abrir una Pull Request

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## ⚠️ Descargo de Responsabilidad

Este bot incluye algunos lenguajes humorísticos e informales en sus respuestas. Está diseñado para servidores casuales de Discord y grupos de amigos. Por favor, revisa y modifica el lenguaje para adaptarlo a los estándares de tu comunidad.

## 🐛 Problemas Conocidos

- Algunas fuentes de música pueden requerir configuración adicional
- Los permisos del canal de voz necesitan estar configurados apropiadamente
- Se requiere conexión a Lavalink para la funcionalidad de música

## 📞 Soporte

Si encuentras problemas o tienes preguntas:
- Abrir un issue en GitHub
- Consultar la [documentación de Discord.py](https://discordpy.readthedocs.io/)
- Revisar la [documentación de Pomice](https://github.com/cloudwithax/pomice)
