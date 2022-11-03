import discord
from discord.ext import commands
import requests
from env import BOT_TOKEN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('My body is ready')
#
#
# @bot.command()
# async def test(cxt, arg):
#     await cxt.send(arg)


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
    # result.strip("[]")
    print(result)
    await cxt.send(result)


@bot.command()
async def spell_search(cxt, arg):
    spell_endpoint = f"https://www.dnd5eapi.co/api/spells/{arg}"
    url = requests.get(url=spell_endpoint)
    print(url.raise_for_status())
    if url.raise_for_status == 200:
        spell_desc = url.json()['desc']
        spell_duration = url.json()['duration']
        spell_damage = url.json()['damage']['damage_type']['name']
        spell_info = spell_desc, spell_duration, spell_damage
        await cxt.send(spell_info)

    elif url.raise_for_status == 404:
        await cxt.send("Sorry, looks like what you searched for doesn't exist!\n"
                       "Maybe check for spelling.")

    else:
        await cxt.send("We aren't sure whats going on right now, I apologise!")

bot.run(BOT_TOKEN)
