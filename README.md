# 🎵 Frater Bot

![Python](https://img.shields.io/badge/python-v3.13+-blue.svg)
![Discord.py](https://img.shields.io/badge/discord.py-v2.0+-blue.svg)
![Pomice](https://img.shields.io/badge/pomice-latest-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A powerful Discord music bot built with Python, featuring music playback, fun commands, and server utilities.

## ✨ Features

### 🎶 Music Commands
- **Play music** from YouTube, Spotify, and other sources
- **Queue management** with playlist support
- **Volume control** and audio effects
- **Voice channel management** (join/leave)
- **Pause/Resume** functionality

### 🎭 Fun Commands  
- **Message snipe** - Recover deleted messages
- **Say command** - Make the bot say custom messages
- **Interactive responses** with personality

### 🛠️ Utility Commands
- **Message management** - Clear messages in bulk
- **Channel nuke** - Completely reset channels
- **Custom help system** - Organized command documentation
- **Permission-based access** control

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- Discord Bot Token
- Lavalink Server (for music functionality)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shellclient/frater.git
   cd frater
   ```

2. **Install dependencies**
   ```bash
   pip install pipenv
   pipenv install
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   TOKEN=your_discord_bot_token
   PREFIX=!
   LAVALINK_HOST=localhost
   LAVALINK_PORT=2333
   LAVALINK_PASSWD=youshallnotpass
   LAVALINK_NAME=default-node
   ```

4. **Run the bot**
   ```bash
   pipenv run dev
   ```

## 🎵 Lavalink Setup

For music functionality, you need a Lavalink server running:

1. Download Lavalink from [here](https://github.com/freyacodes/Lavalink/releases)
2. Configure `application.yml`
3. Run Lavalink: `java -jar Lavalink.jar`

## 📝 Commands

### Music
| Command | Aliases | Description |
|---------|---------|-------------|
| `!play <song>` | `!p` | Play music from various sources |
| `!join` | `!j` | Join your voice channel |
| `!leave` | `!l` | Leave the voice channel |
| `!pause` | - | Pause the current track |
| `!resume` | `!r` | Resume playback |
| `!volume <1-100>` | `!v` | Change playback volume |

### Fun
| Command | Description |
|---------|-------------|
| `!snipe` | Recover the last deleted message |
| `!say <message>` | Make the bot say something |

### Utilities
| Command | Description |
|---------|-------------|
| `!clear <amount>` | Delete specified number of messages |
| `!nuke` | Reset the entire channel |
| `!help [category]` | Show available commands |

## 🏗️ Project Structure

```
frater/
├── src/
│   ├── Cogs/
│   │   ├── Music.py    # Music functionality
│   │   ├── Fun.py      # Entertainment commands
│   │   └── Utils.py    # Utility commands
│   └── index.py        # Main bot file
├── Pipfile             # Dependencies
├── .env               # Environment variables
└── README.md          # You are here!
```

## 🔧 Development

### Running in development mode
```bash
pipenv run dev
```

This uses `nodemon` to automatically restart the bot when files change.

### Adding new commands
1. Create commands in the appropriate Cog file
2. Use the `@commands.command()` decorator
3. Add proper error handling and help text

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This bot includes some humorous and informal language in its responses. It's designed for casual Discord servers and friend groups. Please review and modify the language to suit your community's standards.

## 🐛 Known Issues

- Some music sources may require additional configuration
- Voice channel permissions need to be properly set
- Lavalink connection required for music functionality

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the [Discord.py documentation](https://discordpy.readthedocs.io/)
- Review [Pomice documentation](https://github.com/cloudwithax/pomice)


