from constants.straydex import SD_EMOJIS

ball_emojis = {
    "pokeball": SD_EMOJIS.pokeball,
    "greatball": SD_EMOJIS.greatball,
    "ultraball": SD_EMOJIS.ultraball,
    "premierball": SD_EMOJIS.premierball,
    "masterball": SD_EMOJIS.masterball,
    "diveball": SD_EMOJIS.diveball,
    "beastball": SD_EMOJIS.beastball,
    "moonball": SD_EMOJIS.moonball,
    "lureball": SD_EMOJIS.lureball,
    "luxuryball": SD_EMOJIS.luxuryball,
    "netball": SD_EMOJIS.netball,
    "duskball": SD_EMOJIS.duskball,
    "friendball": SD_EMOJIS.friendball,
    "fastball": SD_EMOJIS.fastball,
    "heavyball": SD_EMOJIS.heavyball,
    "quickball": SD_EMOJIS.quickball,
    "loveball": SD_EMOJIS.loveball,

}

ball_catch_rate = {
    "pokeball": 10,
    "greatball": 25,
    "ultraball": 35,
    "premierball": 50,
    "masterball": 100,
    "beastball": 0,
    "diveball": 30,
}

catch_rate_map = {
    "common": {
        "non_patron_gen_1_8": 70,
        "held_item_pokemon": 25,
        "fishing": 45,
    },
    "uncommon": {
        "non_patron_gen_1_8": 60,
        "held_item_pokemon": 20,
        "fishing": 35,
    },
    "rare": {
        "non_patron_gen_1_8": 37,
        "held_item_pokemon": 15,
        "fishing": 25,
    },
    "superrare": {
        "non_patron_gen_1_8": 20,
        "held_item_pokemon": 10,
        "fishing": 15,
    },
    "legendary": {
        "non_patron_gen_1_8": 5,
        "held_item_pokemon": 0,
        "fishing": 5,
    },
    "shiny": {
        "non_patron_gen_1_8": 0,
        "held_item_pokemon": 0,
        "fishing": 0,
    },
    "golden": {
        "non_patron_gen_1_8": 0,
        "held_item_pokemon": 0,
        "fishing": 0,
    },
}
