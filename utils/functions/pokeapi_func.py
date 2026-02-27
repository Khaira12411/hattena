import aiohttp


async def fetch_pokemon_stats_from_api(
    name: str, weight_only: bool = False
) -> dict | None:
    """
    Fetch Pokémon stats and abilities from PokéAPI.
    Returns a dict with keys: base_atk, base_spe, base_spa, base_def, base_spd, weight, ability
    If multiple abilities, ability is a comma-separated string.
    If weight_only is True, only returns {'weight': weight}.
    Returns None if not found or error.
    """
    url_name = format_name_for_api_lookup(name)
    url = f"https://pokeapi.co/api/v2/pokemon/{url_name}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return None
                data = await resp.json()
        if weight_only:
            return {"weight": data.get("weight")}
        stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
        abilities = [a["ability"]["name"] for a in data["abilities"]]
        return {
            "base_atk": stats.get("attack"),
            "base_spe": stats.get("speed"),
            "base_spa": stats.get("special-attack"),
            "base_def": stats.get("defense"),
            "base_spd": stats.get("special-defense"),
            "weight": data.get("weight"),
            "ability": ",".join(abilities),
        }
    except Exception:
        return None


def format_name_for_api_lookup(name: str) -> str:
    """
    Format a Pokémon name for API lookup by converting to lowercase and replacing spaces with hyphens.
    """
    name = name.lower().replace(" ", "-")
    # Handle Mega, Primal, Alolan, Galarian, Hisuian, etc.
    special_forms = [
        "mega",
        "primal",
        "alola",
        "galar",
        "hisui",
        "paldea",
        "gigantamax",
        "totem",
        "origin",
        "eternamax",
        "starter",
    ]
    # Handle Mega Mewtwo X/Y and similar forms
    # e.g., mega-mewtwo-x or mega-mewtwo-y or mega mewtwo x
    if name.startswith("mega-mewtwo-") and (name.endswith("-x") or name.endswith("-y")):
        letter = name[-1]
        return f"mewtwo-mega-{letter}"
    # General special forms
    for form in special_forms:
        if name.startswith(form + "-"):
            rest = name[len(form) + 1 :]
            # Check for trailing -x or -y (for other possible forms)
            if rest.endswith("-x") or rest.endswith("-y"):
                base = rest[:-2]
                letter = rest[-1]
                return f"{base}-{form}-{letter}"
            return f"{rest}-{form}"
        if name.endswith("-" + form):
            # already in correct format
            return name
        # e.g., mewtwo-mega-x or mewtwo-mega-y
        if name.endswith("-" + form + "-x") or name.endswith("-" + form + "-y"):
            return name
    return name
    return name
    return name
