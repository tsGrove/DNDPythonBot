barbarian_features = {
    "rage": {
        "level": '1',
        "desc": "In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action.\n"
                 "While raging, you gain the following benefits if you aren’t wearing heavy armor:\n"
                 "You have advantage on Strength checks and Strength saving throws.\n"
                 "When you make a melee weapon attack using Strength, "
                "you gain a bonus to the damage roll that increases"
                 " as you gain levels as a barbarian, as shown in the Rage Damage column of the Barbarian table.\n"
                 "You have resistance to bludgeoning, piercing, and slashing damage.\n"
                 "If you are able to cast spells, you can’t cast them or concentrate on them while raging\n."
                 "Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends"
                 " and you haven’t attacked a hostile creature since your last turn or taken damage since then."
                 " You can also end your rage on your turn as a bonus action.\n"
                 "Once you have raged the number of times shown for your barbarian level in the Rages column of the"
                 " Barbarian table, you must finish a long rest before you can rage again."
    },
    "unarmored defense": {
        'level': '1',
        'desc': 'While you are not wearing any armor, your Armor Class equals 10 + your Dexterity modifier +'
                 ' your Constitution modifier. You can use a shield and still gain this benefit.'
    },
    "reckless attack": {
        "level": '2',
        "desc": "Starting at 2nd level, you can throw aside all concern for defense to attack with fierce desperation. "
                "When you make your first attack on your turn, you can decide to attack recklessly. "
                "Doing so gives you advantage on melee weapon attack rolls using Strength during this turn,"
                " but attack rolls against you have advantage until your next turn."
    },
    "danger sense": {
        'level': '2',
        'desc': 'At 2nd level, you gain an uncanny sense of when things nearby aren’t as they should be, '
                'giving you an edge when you dodge away from danger.\n'
                'You have advantage on Dexterity saving throws against effects that you can see,'
                ' such as traps and spells. To gain this benefit, you can’t be blinded, deafened, or incapacitated.'
    },
    'primal path': {
        'level': '3',
        'desc': 'At 3rd level, you choose a path that shapes the nature of your rage. The Path of the Berserker is '
                 'detailed at the end of the class description, and additional primal paths are available in other '
                 'sources. Your choice grants you features at 3rd level and again at 6th, 10th, and 14th levels.'
    },
    'ability score improvement': {
        'level': '4',
        'desc': 'When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, '
                 'you can increase one ability score of your choice by 2, or you can increase two ability scores of'
                 ' your choice by 1. As normal, you can’t increase an ability score above 20 using this feature.'
    },
    'extra attack': {
        'level': '5',
        'desc': 'Beginning at 5th level, you can attack twice, instead of once, '
                 'whenever you take the Attack action on your turn.'
    },
    'fast movement': {
        'level': '5',
        'desc': 'Starting at 5th level, your speed increases by 10 feet while you aren’t wearing heavy armor.'
    },

    'feral instinct': {
        'level': '7',
        'desc': 'By 7th level, your instincts are so honed that you have advantage on initiative rolls.\n'
                 'Additionally, if you are surprised at the beginning of combat and aren’t incapacitated,'
                 ' you can act normally on your first turn, but only if you enter your rage before '
                 'doing anything else on that turn.'
    },
    'brutal critical': {
        'level': '9',
        'desc': 'Beginning at 9th level, you can roll one additional weapon damage die when determining '
                 'the extra damage for a critical hit with a melee attack.\n'
                 'This increases to two additional dice at 13th level and three additional dice at 17th level.'
    },
    'relentless rage': {
        'level': '11',
        'desc': 'Starting at 11th level, your rage can keep you fighting despite grievous wounds.\n '
                 'If you drop to 0 hit points while you’re raging and don’t die outright, you can make a'
                 'DC 10 Constitution saving throw. If you succeed, you drop to 1 hit point instead.\n'
                 'Each time you use this feature after the first, the DC increases by 5. '
                 'When you finish a short or long rest, the DC resets to 10.'
    },
    'persistent rage': {
        'level': '15',
        'desc': 'Beginning at 15th level, your rage is so fierce that it ends early only if you '
                 'fall unconscious or if you choose to end it.'
    },
    'indomitable might': {
        'level': '18',
        'desc': 'Beginning at 18th level, if your total for a Strength check is less than your '
                 'Strength score, you can use that score in place of the total.'
    },
    'primal champion': {
        'level': '20',
        'desc': 'At 20th level, you embody the power of the wilds. '
                 'Your Strength and Constitution scores increase by 4. Your maximum for those scores is now 24.'
    },
}

bard_features = {
    'bardic_inspiration': {
        'level': '1',
        'desc': 'You can inspire others through stirring words or music. To do so, '
                'you use a bonus action on your turn to choose one creature other than yourself within '
                '60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a d6.\n'
                'Once within the next 10 minutes, the creature can roll the die and add the number rolled to one '
                'ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the '
                'd20 before deciding to use the Bardic Inspiration die, but must decide before the DM says whether the '
                'roll succeeds or fails. Once the Bardic Inspiration die is rolled, it is lost. A creature can have '
                'only one Bardic Inspiration die at a time.\n'
                'You can use this feature a number of times equal to your Charisma modifier (a minimum of once). '
                'You regain any expended uses when you finish a long rest.\n'
                'Your Bardic Inspiration die changes when you reach certain levels in this class. '
                'The die becomes a d8 at 5th level, a d10 at 10th level, and a d12 at 15th level.'
    },
    'jack of all trades': {
        'level': '2',
        'desc': 'Starting at 2nd level, you can add half your proficiency bonus, rounded down, '
                'to any ability check you make that doesn’t already include your proficiency bonus.'
    },
    'song of rest': {
        'level': '2',
        'desc': 'Beginning at 2nd level, you can use soothing music or oration to help revitalize your wounded allies '
                'during a short rest. If you or any friendly creatures who can hear your performance regain hit points'
                ' at the end of the short rest by spending one or more Hit Dice, each of those '
                'creatures regains an extra 1d6 hit points.\n'
                'The extra hit points increase when you reach certain levels in this class: to 1d8 at 9th level,'
                ' to 1d10 at 13th level, and to 1d12 at 17th level.'
    },
    'bard college': {
        'level': '3',
        'desc': 'At 3rd level, you delve into the advanced techniques of a bard college of your choice: '
                'the College of Lore detailed at the end of the class description or another from the Players Handbook'
                ' or other sources. Your choice grants you features at 3rd level and again at 6th and 14th level.'
    },
    'expertise': {
        'level': '3',
        'desc': 'At 3rd level, choose two of your skill proficiencies. Your proficiency bonus is '
                'doubled for any ability check you make that uses either of the chosen proficiencies.\n'
                'At 10th level, choose two more of your skill proficiencies.'
                ' Your proficiency bonus is doubled for any ability check you make '
                'that uses either of the chosen proficiencies.'
    },
    'ability score increase': {
        'level': '4',
        'desc': 'When you reach 4th level, and again at 8th, 12th, 16th, and 19th level,'
                ' you can increase one ability score of your choice by 2, or you can increase two '
                'ability scores of your choice by 1. As normal, you can’t increase an ability score above 20'
                ' using this feature.\n'
                'Using the optional feats rule, you can forgo taking this '
                'feature to take a feat of your choice instead.'
    },
    'font of inspiration': {
        'level': '5',
        'desc': 'Beginning when you reach 5th level, you regain all of your expended uses of '
                'Bardic Inspiration when you finish a short or long rest.'
    },
    'countercharm': {
        'level': '6',
        'desc': 'At 6th level, you gain the ability to use musical notes or words of power to disrupt '
                'mind-influencing effects. As an action, you can start a performance that lasts until the end of'
                ' your next turn. During that time, you and any friendly creatures within 30 feet of you have '
                'advantage on saving throws against being frightened or charmed. A creature must be able to hear you'
                ' to gain this benefit. The performance ends early if you are incapacitated or silenced or'
                ' if you voluntarily end it (no action required).'
    },
    'magical secrets': {
        'level': '10',
        'desc': 'At 14th level, you have plundered magical knowledge from a wide spectrum of disciplines.'
                ' Choose two spells from any classes, including this one. A spell you choose must be of a level '
                'you can cast, as shown on the Bard table, or a cantrip.\n'
                'The chosen spells count as bard spells for you and are included in the number in the Spells Known '
                'column of the Bard table.\n'
                'You learn two additional spells from any classes at 18th level.'
    },
    'superior inspiration': {
        'level': '20',
        'desc': 'At 20th level, when you roll initiative and have no uses of Bardic Inspiration left, '
                'you regain one use.'
    }
}

cleric_features = {
        'divine domain': {
        'level' : '1',
        'desc' : 'Choose one domain related to your deity: Knowledge, Life, Light, Nature, Tempest, Trickery, or War.'
                 ' The Life domain is detailed at the end of the class description and provides examples of gods'
                 ' associated with it. See the Player’s Handbook for details on all the domains.Your choice grants'
                 ' you domain spells and other features when you choose it at 1st level. It also grants you additional '
                 'ways to use Channel Divinity when you gain that feature at 2nd level, and additional benefits at 6th,'
                 ' 8th, and 17th levels'
    },
    'domain spells': {
        'level': '1',
        'desc': 'Each domain has a list of spells — its domain spells — that you gain at the cleric levels noted in the'
                ' domain description. Once you gain a domain spell, you always have it prepared, and it doesn’t'
                ' count against the number of spells you can prepare each day.\n'
                'If you have a domain spell that doesn’t appear on the cleric spell list, the spell is '
                'nonetheless a cleric spell for you.'
    },
    'channel divinity': {
        'level': '2',
        'desc': 'At 2nd level, you gain the ability to channel divine energy directly from your deity, using that'
                ' energy to fuel magical effects. You start with two such effects: Turn Undead and an effect '
                'determined by your domain. Some domains grant you additional effects as you advance in levels, '
                'as noted in the domain description.\n'
                'When you use your Channel Divinity, you choose which effect to create. You must then finish a short '
                'or long rest to use your Channel Divinity again.\n'
                'Some Channel Divinity effects require saving throws. When you use such an effect from this class,'
                ' the DC equals your cleric spell save DC.\n'
                'Beginning at 6th level, you can use your Channel Divinity twice between rests, and beginning at'
                ' 18th level, you can use it three times between rests. When you finish a short or long rest, you '
                'regain your expended uses.'
    },
    'ability score improvement': {
        'level': '4',
        'desc': 'When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability'
                ' score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal,'
                ' you can’t increase an ability score above 20 using this feature.\n'
                'Using the optional feats rule, you can forgo taking this feature to take a feat of your '
                'choice instead.'
    },
    'divine intervention': {
        'level': '10',
        'desc': 'Beginning at 10th level, you can call on your deity to intervene on your behalf when '
                'your need is great.\n'
                'Imploring your deity’s aid requires you to use your action. Describe the assistance you seek, and roll '
                'percentile dice. If you roll a number equal to or lower than your cleric level, your deity intervenes'
                '. The DM chooses the nature of the intervention; the effect of any cleric spell or cleric domain spell'
                ' would be appropriate.\n'
                'If your deity intervenes, you can’t use this feature again for 7 days. Otherwise, you can use '
                'it again after you finish a long rest.\n'
                'At 20th level, your call for intervention succeeds automatically, no roll required.'
    },

}

    # '': {
    #     'level' : '',
    #     'desc' : ''
    # },
    #

class_dicts = {'barbarian': barbarian_features, 'bard': bard_features, 'cleric': cleric_features}
