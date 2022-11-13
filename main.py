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
    arg = searchable(arg)
    class_endpoint = f"https://www.dnd5eapi.co/api/classes/{arg}"
    url = requests.get(url=class_endpoint)
    url.raise_for_status()
    class_data = (json.loads(url.content))
    if url.status_code == 200:

        class_name = class_data['name']
        hit_die = class_data['hit_die']
        class_prof = class_data['proficiency_choices']
        num_of_prof = class_data['proficiency_choices'][0]['choose']
        skill_prof = class_prof[0]['from']['options']
        starting_profs = class_data['proficiencies']

        skills = []
        free_shit = []

        for item in starting_profs:
            start = item['name']
            free_shit.append(start)

        for skill in skill_prof:
            skill_variable = skill['item']['name']
            skill_variable = skill_variable.replace('Skill: ', '')
            skills.append(skill_variable)

        await cxt.send(f"Class: {class_name}, Hit Die: d{hit_die}, Can pick {num_of_prof} proficiencies, from: {skills}")
        await cxt.send(f"The {class_name} gains these proficiencies by default: {free_shit}")


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
                       "If searching for a spell with two words, like animate dead, "
                       "be sure to include a symbol separating the words, like -, _, or a period.")

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

@bot.command()
async def skills(cxt, arg):
    arg = searchable(arg)
    skill_endpoint = f"https://www.dnd5eapi.co/api/skills/{arg}"
    url = requests.get(url=skill_endpoint)
    if url.status_code == 200 and arg in lists.skill_list:
        skill_info = json.loads(url.content)
        await cxt.send(skill_info['name'])
        await cxt.send(skill_info['desc'])

    else:
        await cxt.send("Sorry, we couldn't find the skill you're looking for. "
                       "Maybe check spelling or a different command!")

@bot.command()
async def ability_score(cxt, arg):
    arg = searchable(arg)
    ability_endpoint = f"https://www.dnd5eapi.co/api/ability-scores/{arg}"
    url = requests.get(url=ability_endpoint)
    if url.status_code == 200 and arg in lists.ability_scores:
        ability_info = json.loads(url.content)
        await cxt.send(ability_info['full_name'])
        await cxt.send(ability_info['desc'])

bot.run(BOT_TOKEN)
