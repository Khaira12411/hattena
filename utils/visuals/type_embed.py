import discord

from constants.straydex import SD_EMOJIS
from constants.weakness_chart import weakness_chart
from utils.functions.pokemon_func import (
    get_dex_number_by_name,
    get_display_name,
    get_name_via_dex,
)
from utils.functions.stats_and_abilities_functions import (
    get_immunities_based_on_abilities,
)
from utils.logs.pretty_log import pretty_log
from utils.visuals.get_pokemon_gifs import get_pokemon_gif

TYPE_EMOJIS = {
    "grass": SD_EMOJIS.grasstype,
    "fire": SD_EMOJIS.firetype,
    "water": SD_EMOJIS.watertype,
    "electric": SD_EMOJIS.electrictype,
    "ice": SD_EMOJIS.icetype,
    "fighting": SD_EMOJIS.fightingtype,
    "poison": SD_EMOJIS.poisontype,
    "ground": SD_EMOJIS.groundtype,
    "flying": SD_EMOJIS.flyingtype,
    "psychic": SD_EMOJIS.psychictype,
    "bug": SD_EMOJIS.bugtype,
    "rock": SD_EMOJIS.rocktype,
    "ghost": SD_EMOJIS.ghosttype,
    "dragon": SD_EMOJIS.dragontype,
    "dark": SD_EMOJIS.darktype,
    "steel": SD_EMOJIS.steeltype,
    "fairy": SD_EMOJIS.fairytype,
    "normal": SD_EMOJIS.normaltype,
}

TYPE_COLOR = {
    "grass": 6469722,
    "fire": 16555092,
    "water": 5017806,
    "electric": 16045116,
    "ice": 7522494,
    "fighting": 13386860,
    "poison": 11037382,
    "ground": 13988163,
    "flying": 9087190,
    "psychic": 16020082,
    "bug": 7201172,
    "rock": 12628104,
    "ghost": 5401256,
    "dragon": 813760,
    "dark": 6050916,
    "steel": 5933728,
    "fairy": 15502564,
    "normal": 9739428,
}


import re

POKEMON_ALIASES = {
    # Only unique/abbreviation aliases not covered by dynamic normalization
    "mmy": "mega-mewtwo-y",
    "mmx": "mega-mewtwo-x",
    "mcx": "mega-charizard-x",
    "mcz": "mega-charizard-z",
    "mray": "mega-rayquaza",
    "mgard": "mega-gardevoir",
    "caly shadow": "calyrex-shadow",
    "calyrex shadow": "calyrex-shadow",
}


def normalize_pokemon_alias(name):
    n = name.lower().replace("_", " ").replace("-", " ").strip()

    # Dynamic Gmax (Gigantamax) forms
    gmax_match = re.match(r"gmax[ -]?(\w+)", n)
    if gmax_match:
        return f"gigantamax-{gmax_match.group(1)}"

    # Dynamic Arceus forms
    # Only match if there is a form after 'arceus' or 'arc'
    arc_match = re.match(r"(arc|arceus)[ -]+(\w+)", n)
    if arc_match and arc_match.group(2) != "arceus":
        return f"arceus-{arc_match.group(2)}"
    if n == "arceus" or n == "arc":
        return "arceus"

    # Dynamic Mega forms
    mega_match = re.match(r"mm([xy])", n)
    if mega_match:
        return f"mega-mewtwo-{mega_match.group(1)}"
    if n == "mcx":
        return "mega-charizard-x"
    if n == "mcz":
        return "mega-charizard-z"
    if n.startswith("mega "):
        return n.replace(" ", "-")

    # Fallback to static aliases if needed
    return POKEMON_ALIASES.get(n, n)


def get_type_embed_color(pokemon_name: str) -> int:
    weaknesses = weakness_chart.get(pokemon_name.lower())
    if not weaknesses:
        pretty_log(
            "warn",
            f"No weaknesses found for {pokemon_name}",
        )
        return None

    types = weaknesses.get("types", [])
    if not types:
        pretty_log(
            "warn",
            f"No types found for {pokemon_name}",
        )
        return None

    return TYPE_COLOR.get(types[0], 0x74CEC0)


# -------------------- Reusable Parsing Functions --------------------
def parse_normal_pokemon(
    dex_int: int, first_index: str, dex_count: int, is_digit: bool
):
    """Handles regular Pokemon input (1-6999, or weighted 1001/9001 style for shiny/golden)"""

    # If first digit is 7 and dex has 4 digits, use it as-is
    if first_index == "7" and dex_count == 4:
        base_dex = dex_int
        # Lookup exact dex in weakness_chart
        variant_name = next(
            (
                name
                for name, data in weakness_chart.items()
                if int(data["dex"]) == base_dex
            ),
            None,
        )
    else:
        base_dex = (dex_int - 1) % 1000 + 1
        # Lookup using %1000 and exclude 7xxx dex
        variant_name = next(
            (
                name
                for name, data in weakness_chart.items()
                if int(data["dex"]) % 1000 == base_dex
                and not data["dex"].startswith("7")
            ),
            None,
        )

    shiny_golden_tag = ""
    if dex_count == 4:
        if first_index == "1":
            shiny_golden_tag = "Shiny"
        elif first_index == "9":
            shiny_golden_tag = "Golden"

    if not variant_name:
        pretty_log(
            "warn",
            f"Failed to resolve normal Pokemon for dex {dex_int}",
        )

    return variant_name, shiny_golden_tag, base_dex, is_digit


# -------------------- Resolver --------------------
def get_pokemon_from_input(pokemon_input: str):
    """Main resolver function: handles name, normal dex, and forms"""
    pokemon = pokemon_input.lower().strip()
    shiny_golden_tag = ""
    is_digit = False
    for prefix, tag in [("shiny ", "Shiny"), ("golden ", "Golden")]:
        if pokemon.startswith(prefix):
            pokemon = pokemon[len(prefix) :].strip()
            shiny_golden_tag = tag
            break

    normalized_alias_name = normalize_pokemon_alias(pokemon)

    normalized_name = normalized_alias_name.replace(" ", "-")
    pretty_log(
        "debug",
        f"Attempting to resolve Pokemon input '{pokemon_input}' -> normalized_alias_name: '{normalized_alias_name}', normalized_name: '{normalized_name}'",
    )
    # Name lookup
    if normalized_name in weakness_chart:
        dex_val = int(weakness_chart[normalized_name]["dex"])
        # Always return 4 values for consistency
        return normalized_name, shiny_golden_tag, dex_val, False

    # Dex input
    if pokemon.isdigit():
        dex_str = str(pokemon)
        first_index = dex_str[0]
        dex_int = int(pokemon)
        dex_count = len(dex_str)
        is_digit = True

        # Check if this dex directly matches a shiny/golden form in weakness_chart
        direct_match = next(
            (
                name
                for name, data in weakness_chart.items()
                if int(data["dex"]) == dex_int
            ),
            None,
        )
        if direct_match:
            # Try to infer tag from the name if present
            tag = ""
            if direct_match.startswith("shiny "):
                tag = "Shiny"
            elif direct_match.startswith("golden "):
                tag = "Golden"
            return direct_match, tag, dex_int, True

        return parse_normal_pokemon(dex_int, first_index, dex_count, is_digit)

    pretty_log(
        "error",
        f"Unresolved Pokemon input: '{pokemon_input}'",
    )
    return None, None, None, None


# -------------------- Embed Builder --------------------
def build_weakness_embed_from_input(pokemon_input: str) -> discord.Embed | None:
    # normalized first

    variant_name, shiny_golden_tag, base_dex, is_digit = get_pokemon_from_input(
        pokemon_input
    )
    if variant_name == "shadow-mewtwo":
        variant_name = "shadow mewtwo"  # Fix for space in name not matching keys in weakness_chart
        
    pretty_log(
        "debug",
        f"Resolved Pokemon input '{pokemon_input}' to variant_name: '{variant_name}', shiny_golden_tag: '{shiny_golden_tag}', base_dex: '{base_dex}', is_digit: {is_digit}",
    )
    if not variant_name:
        return None, None, None

    weaknesses = weakness_chart.get(variant_name)
    if not weaknesses:
        pretty_log(
            "warn",
            f"No weaknesses found for {variant_name}",
        )
        return None, None, None

    types = weaknesses.get("types", [])
    SD_EMOJISs_str = "".join(TYPE_EMOJIS.get(t, "") for t in types)

    # 🟢 Clean up title (fix Mega hyphen issue)
    def clean_display_name(raw_name: str, tag: str | None = None) -> str:
        display_name = raw_name.title()
        if "mega-" in raw_name.lower():
            display_name = display_name.replace("Mega-", "Mega ").replace("-", " ")
        # Avoid double tag if already present
        if tag:
            lowered = display_name.lower()
            if not lowered.startswith(tag.lower()):
                display_name = f"{tag} {display_name}"
        return display_name

    dex_number = pokemon_input if is_digit else get_dex_number_by_name(variant_name)
    display_name = clean_display_name(variant_name, shiny_golden_tag)
    embed_title = f"{SD_EMOJISs_str} {display_name} #{dex_number}"
    image_lookup_name = (
        variant_name if not is_digit else get_name_via_dex(str(pokemon_input))
    )

    embed_color = TYPE_COLOR.get(types[0], 0x74CEC0) if types else 0x74CEC0

    mult_order = ["4x", "2x", "1x", "1/2x", "1/4x", "0x"]
    description_lines = []
    for mult in mult_order:
        if mult in weaknesses and weaknesses[mult]:
            types_with_emoji = [
                f"{TYPE_EMOJIS.get(t, '')} {t.capitalize()}" for t in weaknesses[mult]
            ]
            description_lines.append(f"**{mult}**: {', '.join(types_with_emoji)}")

    image_url = get_pokemon_gif(image_lookup_name)
    embed = discord.Embed(
        title=embed_title,
        description="\n\n".join(description_lines),
        color=embed_color,
    )
    if image_url:
        embed.set_thumbnail(url=image_url)

    notes = get_immunities_based_on_abilities(variant_name)
    if notes and notes[2]:  # Check if note string is present
        embed.add_field(name="Notes:", value=notes[2], inline=False)
    return embed, description_lines, embed_title
