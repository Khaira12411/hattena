from constants.new_pokemons import pokemons

immunity_abilities = {
    "dry-skin": ["fire"],
    "earth-eater": ["ground"],
    "flash-fire": ["fire"],
    "levitate": ["ground"],
    "lightning-rod": ["electric"],
    "motor-drive": ["electric"],
    "sap-sipper": ["grass"],
    "storm-drain": ["water"],
    "thick-fat": ["fire", "ice"], # Only half damage from both
    "volt-absorb": ["electric"], # restores hp by 25%  when hit by electric move, but still immune to it
    "water-absorb": ["water"], # restores hp by 25% when hit by water move, but still immune to it
    "well-baked-body": ["fire"], # Immune to fire , raises defenses by 2 stages when hit by fire move
}

def get_immunities_based_on_abilities(pokemon_name):
    """Return a list of types that the given Pokémon is immune to based on its abilities."""
    immunities = set()
    abilities = get_pokemon_abilities(pokemon_name)
    if not abilities:
        return []
    for ability in abilities.get("standard", []) + abilities.get("hidden", []):
        types = immunity_abilities.get(ability, [])
        immunities.update(types)
    return list(immunities)

# Add a special note for shedinja's Wonder Guard only fire , flying, rock, ghost, and dark can hit it
def normalize_pokemon_name(name):
    """
    Convert user input like 'mega-absol' or 'gigantamax-alcremie' to PokéAPI key.
    Handles Mega, Gigantamax, Primal, and regional forms.
    """
    name = name.lower().replace(" ", "-")
    # Mega forms
    if name.startswith("mega-"):
        base = name[5:]
        # Handle possible -x or -y
        if base.endswith("-x") or base.endswith("-y"):
            return f"{base[:-2]}-mega-{base[-1]}"
        return f"{base}-mega"
    # Gigantamax forms
    if name.startswith("gigantamax-"):
        base = name[11:]
        return f"{base}-gmax"
    # Primal forms
    if name.startswith("primal-"):
        base = name[7:]
        return f"{base}-primal"
    # Alolan, Galarian, Hisuian, Paldean, etc.
    for region in ["alolan", "galarian", "hisuian", "paldean"]:
        if name.startswith(f"{region}-"):
            base = name[len(region) + 1 :]
            return f"{base}-{region}"
    return name


def get_pokemon_stats(name):
    """Return the stats dictionary for the given Pokémon name."""
    key = normalize_pokemon_name(name)
    return pokemons.get(key, {}).get("stats")


def get_pokemon_abilities(name):
    """Return the abilities dictionary for the given Pokémon name."""
    key = normalize_pokemon_name(name)
    return pokemons.get(key, {}).get("abilities")


def get_pokemons_with_ability(ability_name):
    """Return a list of Pokémon names that have the given ability (standard or hidden)."""
    result = []
    for name, data in pokemons.items():
        abilities = data.get("abilities", {})
        if ability_name in abilities.get(
            "standard", []
        ) or ability_name in abilities.get("hidden", []):
            result.append(name)
    return result


def get_pokemons_by_weight(min_weight=None, max_weight=None):
    """Return a list of Pokémon names filtered by weight (in kg)."""
    result = []
    for name, data in pokemons.items():
        weight = data.get("stats", {}).get("weight")
        if weight is not None:
            if (min_weight is None or weight >= min_weight) and (
                max_weight is None or weight <= max_weight
            ):
                result.append(name)
    return result


def get_pokemons_by_stat(stat, min_value=None, max_value=None):
    """Return a list of Pokémon names filtered by a specific stat."""
    result = []
    for name, data in pokemons.items():
        value = data.get("stats", {}).get(stat)
        if value is not None:
            if (min_value is None or value >= min_value) and (
                max_value is None or value <= max_value
            ):
                result.append(name)
    return result


def pretty_print_pokemon(name):
    """Prints a formatted summary of the Pokémon's stats and abilities."""
    key = normalize_pokemon_name(name)
    data = pokemons.get(key)
    if not data:
        print(f"No data for {name}")
        return
    print(f"{name.title()}\nStats: {data['stats']}\nAbilities: {data['abilities']}")
