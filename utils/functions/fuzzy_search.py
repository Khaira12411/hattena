from rapidfuzz import process

# Your cached Pokémon list
from utils.cache.market_value_cache import get_pokemon_names_cache

from utils.logs.debug_log import debug_log, enable_debug

enable_debug(f"{__name__}.fuzzy_search")
def fuzzy_search(query,threshold=80):

    choices = get_pokemon_names_cache()  # Get the list of Pokémon names from cache
    # Normalize input
    query = query.strip().lower()
    debug_log(f"Fuzzy search for query: '{query}'")
    choices_norm = [c.lower() for c in choices]

    # Run fuzzy match
    match = process.extractOne(query, choices_norm)

    if match and match[1] >= threshold:
        # Return the original name (not lowercased)
        debug_log(f"Fuzzy match found: '{match[0]}' with score {match[1]}")
        return choices[choices_norm.index(match[0])]
    else:
        debug_log("No fuzzy match found above threshold.")
        return None



