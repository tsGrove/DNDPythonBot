import discord
from discord.ext import commands
import requests
from env import BOT_TOKEN
import json


def searchable(x):
    x = x.lower()
    x = x.strip()
    x = x.replace(" ", "-")
    x = x.replace("_", "-")

    return x


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('My body is ready')


@bot.command()
async def info(cxt):
    await cxt.send("Hi! Im a Dungeons and Dragons search bot designed by Shea. "
                   "Here are a list of commands I have avaliable:\n"
                   "!ability-search\n"
                   "!spell-search\n")


@bot.command()
async def search(cxt, arg):
    API_ENDPOINT = f"https://www.dnd5eapi.co/api/{arg}"
    url = requests.get(url=API_ENDPOINT)
    url.raise_for_status()
    result = url.json()['desc'][1]
    print(result)
    await cxt.send(result)


@bot.command()
async def spell_search(cxt, arg):
    arg = searchable(arg)
    spell_endpoint = f"https://www.dnd5eapi.co/api/spells/{arg}"
    url = requests.get(url=spell_endpoint)
    print(arg)
    spell_data = (json.loads(url.content))
    if url.status_code == 200:
        if 'damage' in spell_data:
            spell_desc = spell_data['desc']
            spell_duration = spell_data['duration']
            spell_damage = spell_data['damage']['damage_type']['name']
            spell_range = spell_data['range']
            spell_components = spell_data['components']
            spell_concentration = spell_data['concentration']
            spell_cast_time = spell_data['casting_time']
            spell_info = spell_desc, spell_duration, spell_damage, spell_range, spell_components, spell_concentration, \
                         spell_cast_time
            await cxt.send(spell_info)

        else:
            spell_desc = spell_data['desc']
            spell_duration = spell_data['duration']
            spell_range = spell_data['range']
            spell_components = spell_data['components']
            spell_concentration = spell_data['concentration']
            spell_cast_time = spell_data['casting_time']
            spell_info = spell_desc, spell_duration, spell_range, spell_components, spell_concentration, spell_cast_time
            await cxt.send(spell_info)

    elif url.status_code == 404:
        await cxt.send("Unfortunately the page you're searching for doesnt exist! "
                       "Maybe check spelling or a different command.")

    else:
        print("Yeah king ngl we aren't sure whats happening rn. gl and gg")


bot.run(BOT_TOKEN)
