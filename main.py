import os, disnake, dotenv, glob, sqlite3
from disnake.ext import commands, tasks
from helpers import db

bot = commands.InteractionBot(intents=disnake.Intents.all())
token = dotenv.get_key('.env', 'BOT_TOKEN')

# Setzt den Status des Bots auf "Schaut nach Gewinnspielen"
@bot.event
async def on_ready():
    print(f'Bot ist online als {bot.user}')
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name="nach neuen Gewinnspielen"))

print('='*10)
for filename in glob.glob('modules/**/*.py', recursive=True):
    n = filename.replace('\\', '.').replace('/', '.')
    if n.split('.')[2][0] != '~':
        bot.load_extension(n.replace('.py', ''))
        print('Loaded {}'.format(n.removeprefix('modules.')))
        continue

    print('Skipping {}'.format(n.removeprefix('modules.')))

sqlite3.connect(db.DATABASE_PATH)
bot.run(token)
