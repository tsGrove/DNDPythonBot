import discord
from discord.ext import commands
import requests
from env import BOT_TOKEN
import json
import lists


def searchable(x):
    x = x.lower()
    x = x.strip()
    x = x.replace(" ", "-")
    x = x.replace("_", "-")
    x = x.replace(".", "-")
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
                   "!spell-search: A command capable of searching spells returning: A description, duration, "
                   "damage-type (if the spell has one), range, components required, is the spell requires concentration"
                   " or not, and the casting time. \n"
                   "!spell_list: Creates a list of spells for the user based on either School of Magic, or spell level.")


@bot.command()
async def class_info(cxt, arg):
    class_endpoint = f"https://www.dnd5eapi.co/api/classes/{arg}"
    searchable(arg)
    url = requests.get(url=class_endpoint)
    url.raise_for_status()
    class_data = (json.loads(url.content))
    if url.status_code == 200:
        print(class_data)



@bot.command()
async def spell_search(cxt, arg):
    arg = searchable(arg)
    spell_endpoint = f"https://www.dnd5eapi.co/api/spells/{arg}"
    url = requests.get(url=spell_endpoint)
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
            await cxt.send(f"Description: {spell_desc}, Duration: {spell_duration}, Damage: {spell_damage}")
            await cxt.send(f"Range: {spell_range}, Components Needed: {spell_components}, Need Concentration? {spell_concentration}. Cast Time: {spell_cast_time}")

        else:
            spell_desc = spell_data['desc']
            spell_duration = spell_data['duration']
            spell_range = spell_data['range']
            spell_components = spell_data['components']
            spell_concentration = spell_data['concentration']
            spell_cast_time = spell_data['casting_time']
            await cxt.send(f"Description: {spell_desc}, Duration: {spell_duration}")
            await cxt.send(f"Range: {spell_range}, Components Needed: {spell_components}, Need Concentration? {spell_concentration}. Cast Time: {spell_cast_time}")

    elif url.status_code == 404:
        await cxt.send("Unfortunately the page you're searching for doesnt exist!"
                       "Maybe check spelling or a different command.\n"
                       "If searching for a spell with two words, like animate dead, be sure to include a symbol seperating the "
                       "words, like -, _, or a period.")

    else:
        print("Unfortunately we aren't sure whats going on! API or the server might be down, sorry :-(")


@bot.command()
async def spell_list(cxt, arg):
    if arg in lists.spell_schools:
        spell_endpoint = f"https://www.dnd5eapi.co/api/spells?school={arg}"
        url = requests.get(url=spell_endpoint)
        information = json.loads(url.content)
        entry = 0
        spells = []
        for spell in information['results']:
            spells.append(information['results'][entry]['name'])
            entry += 1
        await cxt.send(spells)

    elif arg in lists.spell_levels:
        spell_endpoint = f"https://www.dnd5eapi.co/api/spells?level={arg}"
        url = requests.get(url=spell_endpoint)
        information = json.loads(url.content)
        entry = 0
        spells = []
        for spell in information['results']:
            spells.append(information['results'][entry]['name'])
            entry += 1
        await cxt.send(spells)

    else:
        await cxt.send("Yo we couldn't find what you was looking for sorry king, maybe trying checking spelling"
                       "or making sure you entered just one number for spell levels. ")

bot.run(BOT_TOKEN)
