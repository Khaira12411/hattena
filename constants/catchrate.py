from constants.straydex import SD_EMOJIS
from constants.weakness_chart import weakness_chart as WEAKNESS_CHART
from utils.functions.pokeapi_func import get_pokemon_stats, get_pokemon_weight
from utils.cache.straymon_member_cache import fetch_straymon_member_cache
from .fish_rarity import FISH_RARITY

DUSKBALL_CATCH_RATE_DURING_NIGHT = 58
MOONBALL_CATCH_RATE_DURING_MIDNIGHT = 74
NETBALL_BASE_CATCH_RATE = 10
NETBALL_WATER_BUG_TYPES_CATCH_RATE = 66

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

fast_ball_catch_rate = {
    "base": 10,
    "speed_75_plus": 70,
    "speed_90_plus": 100,
}
heavy_ball_catch_rate = {
    "base": 10,
    "weight_100_plus": 55,
    "weight_200_plus": 75,
    "weight_300_plus": 95,
}
ball_catch_rate = {
    "pokeball": 10,
    "greatball": 25,
    "ultraball": 35,
    "premierball": 50,
    "masterball": 100,
    "beastball": 0,
    "diveball": 30,
    "duskball": 10,
    "friendball": 10,
    "luxuryball": 10,
    "loveball": 10,
    "moonball": 10,
    "lureball": 90,  # Only in fishing
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
catch_rates = {
    "non_patreon_gen_1_8": {
        "common": 70,
        "uncommon": 60,
        "rare": 37,
        "superrare": 20,
        "legendary": 5,
        "shiny": 0,
        "golden": 0,
    },
    "held_item_pokemon": {
        "common": 25,
        "uncommon": 20,
        "rare": 15,
        "superrare": 10,
        "legendary": 0,
        "shiny": 0,
        "golden": 0,
    },
    "fishing": {
        "common": 45,
        "uncommon": 35,
        "rare": 25,
        "superrare": 15,
        "legendary": 5,
        "shiny": 0,
        "golden": 0,
    },
}
water_states_map = {
    "intense": -10,
    "strong": -7,
    "moderate": -5,
    "calm": 5,
    "special": 10,
}
ultrabeast_list = [
    "nihilego",
    "buzzwole",
    "pheromosa",
    "xurkitree",
    "celesteela",
    "kartana",
    "guzzlord",
    "poipole",
    "naganadel",
    "stakataka",
    "blacephalon",
]
fishing_golden = [
    "kyogre",
    "wailmer",
    "tentacool",
    "poliwag",
]
def get_pokemon_types(pokemon_name):
    """
    Returns a list of types for the given Pokémon name using WEAKNESS_CHART.
    If the Pokémon is not found, returns an empty list.
    """
    entry = WEAKNESS_CHART.get(pokemon_name)
    if entry and "types" in entry:
        return entry["types"]
    return []


def netball_catch_rate(pokemon_name):
    types = get_pokemon_types(pokemon_name)
    if "Water" in types or "Bug" in types:
        return NETBALL_WATER_BUG_TYPES_CATCH_RATE # 66% catch rate for Water and Bug types
    return NETBALL_BASE_CATCH_RATE # 10% catch rate for all other types

def can_pokemon_be_fished(pokemon_name):
    """Checks if a Pokémon can be obtained through fishing based on the FISH_RARITY mapping."""
    return pokemon_name in FISH_RARITY

async def fast_ball_catch_rate(bot, pokemon_name):
    stats = await get_pokemon_stats(bot, pokemon_name)
    if not stats:
        return fast_ball_catch_rate["base"]  # Default to base if stats are unavailable

    speed = stats.get("base_spe", 0)
    if speed >= 90:
        return fast_ball_catch_rate["speed_90_plus"]
    elif speed >= 75:
        return fast_ball_catch_rate["speed_75_plus"]
    else:
        return fast_ball_catch_rate["base"]

async def heavy_ball_catch_rate(pokemon_name):
    weight = await get_pokemon_weight(pokemon_name)
    if weight is None:
        return heavy_ball_catch_rate["base"]  # Default to base if weight is unavailable
    weight_value = int(weight.replace(" kg", ""))
    if weight_value >= 300:
        return heavy_ball_catch_rate["weight_300_plus"]
    elif weight_value >= 200:
        return heavy_ball_catch_rate["weight_200_plus"]
    elif weight_value >= 100:
        return heavy_ball_catch_rate["weight_100_plus"]
    else:
        return heavy_ball_catch_rate["base"]

async def calculate_catch_rate(bot, pokemon_name, is_straymon=False, is_held_item=False):
    """Calculates the catch rate for a Pokémon based on its types, stats, and weight for special balls."""
    is_patreon = False
    patreon_bonus = 0
    catch_rate_bonus = 0
    if is_straymon:
        member_info = fetch_straymon_member_cache(bot.user.id)
        if member_info:
            is_patreon = member_info.get("is_patreon", False)
            catch_rate_bonus = member_info.get("catch_rate_bonus", 0)

    if is_patreon:
        patreon_bonus = 5