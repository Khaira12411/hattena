weather_abilities = {
    "drizzle": {
        "weather": "Rain",
        "effect": "Sets Rain for 5 turns",
        "pokemon": ["Pelipper", "Politoed", "Kyogre"],
    },
    "drought": {
        "weather": "Sun",
        "effect": "Sets Harsh Sunlight for 5 turns",
        "pokemon": ["Torkoal", "Ninetales", "Groudon"],
    },
    "orichalcum_pulse": {
        "weather": "Sun",
        "effect": "Sets Harsh Sunlight for 5 turns and boosts Attack by 30%",
        "pokemon": ["Koraidon"],
    },
    "snow_warning": {
        "weather": "Snow",
        "effect": "Sets Snowstorm for 5 turns",
        "pokemon": ["Alolan Ninetales", "Abomasnow"],
    },
    "sand_stream": {
        "weather": "Sandstorm",
        "effect": "Sets Sandstorm for 5 turns",
        "pokemon": ["Tyranitar", "Hippowdon"],
    },
}

weather_moves = {
    "sun": {
        "solar_beam": {
            "effect": "Normally 2-turn, but in Sun it fires instantly",
            "power": 120,
            "type": "Grass",
            "pokemon": ["Venusaur", "Exeggutor", "Charizard"],
            "cons": "Weaker in Rain/Sand/Snow (power halved)",
        },
        "solar_blade": {
            "effect": "Physical version of Solar Beam, instant in Sun",
            "power": 125,
            "type": "Grass",
            "pokemon": ["Lurantis", "Kartana"],
            "cons": "Still requires charge in other weather",
        },
        "weather_ball": {
            "effect": "Becomes Fire-type in Sun, doubled power",
            "power": 100,
            "type": "Fire",
            "pokemon": ["Castform", "Roserade"],
            "cons": "Type changes with weather, less reliable outside Sun",
        },
        "morning_sun/synthesis/moonlight": {
            "effect": "Heal more HP in Sun (⅔ max)",
            "power": None,
            "type": "Status",
            "pokemon": ["Espeon", "Venusaur", "Umbreon"],
            "cons": "Heal less in Rain/Sand/Snow (¼ max)",
        },
    },
    "rain": {
        "thunder": {
            "effect": "Accuracy becomes 100% in Rain",
            "power": 110,
            "type": "Electric",
            "pokemon": ["Zapdos", "Jolteon", "Kyogre"],
            "cons": "50% accuracy in Sun",
        },
        "hurricane": {
            "effect": "Accuracy becomes 100% in Rain",
            "power": 110,
            "type": "Flying",
            "pokemon": ["Tornadus", "Pelipper"],
            "cons": "50% accuracy in Sun",
        },
        "weather_ball": {
            "effect": "Becomes Water-type in Rain, doubled power",
            "power": 100,
            "type": "Water",
            "pokemon": ["Castform", "Ludicolo"],
            "cons": "Type changes with weather, less reliable outside Rain",
        },
        "morning_sun/synthesis/moonlight": {
            "effect": "Heal less HP in Rain (¼ max)",
            "power": None,
            "type": "Status",
            "pokemon": ["Umbreon", "Roserade"],
            "cons": "Not optimal healing in Rain",
        },
    },
    "snow": {
        "blizzard": {
            "effect": "Accuracy becomes 100% in Snow",
            "power": 110,
            "type": "Ice",
            "pokemon": ["Glaceon", "Abomasnow", "Lapras"],
            "cons": "70% accuracy outside Snow",
        },
        "aurora_veil": {
            "effect": "Can only be used in Snow; halves damage for 5 turns",
            "power": None,
            "type": "Status",
            "pokemon": ["Alolan Ninetales"],
            "cons": "Completely unusable outside Snow",
        },
        "weather_ball": {
            "effect": "Becomes Ice-type in Snow, doubled power",
            "power": 100,
            "type": "Ice",
            "pokemon": ["Castform", "Vanilluxe"],
            "cons": "Type changes with weather, less reliable outside Snow",
        },
    },
    "sandstorm": {
        "weather_ball": {
            "effect": "Becomes Rock-type in Sandstorm, doubled power",
            "power": 100,
            "type": "Rock",
            "pokemon": ["Castform", "Tyranitar"],
            "cons": "Type changes with weather, less reliable outside Sandstorm",
        },
        "shore_up": {
            "effect": "Restores more HP in Sandstorm (⅔ max)",
            "power": None,
            "type": "Status",
            "pokemon": ["Palossand"],
            "cons": "Normal healing outside Sandstorm",
        },
    },
}
