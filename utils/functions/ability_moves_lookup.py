import itertools

import discord

from constants.aesthetic import Emojis
from constants.new_abilities import abilities
from constants.new_moves_preview import moves
from constants.pokemons import *
from constants.straymons_constants import DEFAULT_EMBED_COLOR
from utils.logs.debug_log import debug_enabled, debug_log, enable_debug
from utils.logs.pretty_log import pretty_log
from straydex.functions.main import send_sd_logs

#enable_debug(f"{__name__}.get_move_learned_by_pokemon")
#enable_debug(f"{__name__}.get_ability_learned_by_pokemon")
#enable_debug(f"{__name__}.ability_moves_lookup")
# Combine all the mons dictionaries into one lookup

ALL_MONS = {}
ALL_MONS.update(common_mons)
ALL_MONS.update(uncommon_mons)
ALL_MONS.update(rare_mons)
ALL_MONS.update(superrare_mons)
ALL_MONS.update(legendary_mons)
ALL_MONS.update(mega_mons)
ALL_MONS.update(gigantamax_mons)
ALL_MONS.update(shiny_mons)
ALL_MONS.update(shiny_mega_mons)
ALL_MONS.update(shiny_gigantamax_mons)
ALL_MONS.update(golden_mons)
ALL_MONS.update(exclusive_mons)


def normalize_move_name(move_name: str) -> str:
    """
    Normalize user input for moves:
    - Lowercase everything
    - Replace spaces with hyphens
    """
    return move_name.strip().lower().replace(" ", "-")


def normalize_pokemon_name(name: str) -> str:
    """
    Normalize Pokémon names consistently:
    - Lowercase everything
    - Strip whitespace
    """
    return name.strip().lower()


def normalize_ability_name(ability_name: str) -> str:
    """
    Normalize user input for abilities:
    - Lowercase everything
    - Strip whitespace
    """
    return ability_name.strip().lower()


def get_move_learned_by_pokemon(move_names):
    if isinstance(move_names, str):
        move_names = [move_names]
    result_set = None
    for move_name in move_names:
        pretty_log("debug", f"Looking up move: {move_name}", label="AbilityMovesLookup")
        move = get_move_data(move_name)
        if not move:
            pretty_log(
                "warning",
                f"Move '{move_name}' not found in any damage class.",
                label="AbilityMovesLookup",
            )
            return set()
        # Normalize Pokémon names here
        learned = {
            normalize_pokemon_name(p) for p in move.get("learned_by_pokemon", [])
        }
        pretty_log(
            "debug",
            f"Move '{move_name}' learned by {len(learned)} Pokémon.",
            label="AbilityMovesLookup",
        )
        if result_set is None:
            result_set = learned
        else:
            before = len(result_set)
            result_set = result_set.intersection(learned)
            pretty_log(
                "debug",
                f"Intersected with '{move_name}': {before} → {len(result_set)} Pokémon.",
                label="AbilityMovesLookup",
            )
    return result_set if result_set is not None else set()


def get_move_learned_by_pokemon_any(move_names):
    if isinstance(move_names, str):
        move_names = [move_names]
    result_set = set()
    for move_name in move_names:
        pretty_log(
            "debug", f"[ANY] Looking up move: {move_name}", label="AbilityMovesLookup"
        )
        move = get_move_data(move_name)
        if not move:
            pretty_log(
                "warning",
                f"[ANY] Move '{move_name}' not found in any damage class.",
                label="AbilityMovesLookup",
            )
            continue
        # Normalize Pokémon names here
        learned = {
            normalize_pokemon_name(p) for p in move.get("learned_by_pokemon", [])
        }
        pretty_log(
            "debug",
            f"[ANY] Move '{move_name}' learned by {len(learned)} Pokémon.",
            label="AbilityMovesLookup",
        )
        result_set = result_set.union(learned)
    return result_set


def get_ability_learned_by_pokemon(ability_name):
    pretty_log(
        "debug", f"Looking up ability: {ability_name}", label="AbilityMovesLookup"
    )
    ability = abilities.get(ability_name)
    if not ability or "pokemons" not in ability:
        pretty_log(
            "warning",
            f"Ability '{ability_name}' not found or has no associated pokemons.",
            label="AbilityMovesLookup",
        )
        return [], []
    pokemons = ability["pokemons"]
    std = [normalize_pokemon_name(p) for p in pokemons.get("standard", [])]
    hid = [normalize_pokemon_name(p) for p in pokemons.get("hidden", [])]
    pretty_log(
        "debug", f"Standard: {len(std)}, Hidden: {len(hid)}", label="AbilityMovesLookup"
    )
    return std, hid


def get_move_data(move_name):
    for dmg_class in moves:
        if move_name in moves[dmg_class]:
            return moves[dmg_class][move_name]
    return None


def format_pokemon_name(name: str) -> str:
    """
    Format Pokémon names into a nice title-case form with special handling for forms.
    """
    name = name.strip().lower()
    parts = name.split("-")

    form_map = {
        "mega": "Mega",
        "primal": "Primal",
        "hisui": "Hisuian",
        "galar": "Galarian",
        "alola": "Alolan",
        "paldea": "Paldean",
        "totem": "Totem",
        "gmax": "Gigantamax",
    }

    # Handle Mega forms with extra suffix (e.g. mewtwo-mega-y)
    if "mega" in parts and len(parts) > 2:
        base = parts[0].capitalize()
        suffix = parts[-1].upper()
        return f"Mega-{base}-{suffix}"

    # Handle mapped forms
    if parts[-1] in form_map:
        base = "-".join(parts[:-1]).capitalize()
        return f"{form_map[parts[-1]]}-{base}"

    # Default: title-case each part
    return "-".join([p.capitalize() for p in parts])


# Helper: get all non-empty combinations of moves (up to 4 moves)
def get_move_combinations(move_names):
    combos = []
    n = len(move_names)
    for r in range(1, n + 1):
        combos.extend(itertools.combinations(move_names, r))
    return combos


# Helper: get Pokémon with ability and all moves in combo
def get_pokemon_with_ability_and_moves(ability_pokemon_set, combo):
    result = ability_pokemon_set
    for move in combo:
        learned = get_move_learned_by_pokemon(move)
        result = result.intersection(learned)
    return result


# Helper: format a field for a move combo
def format_combo_field(combo, pokes):
    combo_str = ", ".join([m.title() for m in combo])
    if len(combo) == 1:
        name = f"{Emojis.ribbon} With {combo_str}"
    else:
        name = f"{Emojis.ribbon} With all of: {combo_str}"
    if not pokes:
        value = "❌ No matches"
    else:
        filtered = []
        for p in sorted(pokes):
            formatted = format_pokemon_name(p)
            # Validation: check if formatted (lowercase) is in ALL_MONS (lowercase keys)
            # ALL_MONS keys are already lowercase, so just lower the formatted name
            if formatted.lower() in ALL_MONS:
                filtered.append(formatted)
        if not filtered:
            value = "❌ No matches"
        else:
            value = ", ".join(filtered)
    return {"name": name, "value": value, "inline": False}


# Helper: get ability and move descriptions from static dicts
def get_info_descriptions(ability_name, move_names):
    # Ability info
    ability = abilities.get(ability_name, {})
    ability_effect = (
        ability.get("effect") or ability.get("desc") or "No description found."
    )
    # Moves info
    move_infos = []
    for m in move_names:
        found = False
        for dmg_class in moves:
            if m in moves[dmg_class]:
                move = moves[dmg_class][m]
                # Use render_effect_text for effect_full and effect_short
                desc = (
                    move.get("effect_full")
                    or move.get("effect_short")
                    or move.get("desc")
                    or "No description found."
                )
                desc = render_effect_text(desc, move.get("effect_chance"))
                damage_class = move.get("damage_class", "?")
                move_type = move.get("type", "?")
                priority = move.get("priority", "?")
                power = move.get("power", "?")
                move_infos.append(
                    {
                        "name": m.title(),
                        "desc": desc,
                        "damage_class": damage_class,
                        "type": move_type,
                        "priority": priority,
                        "power": power,
                    }
                )
                found = True
                break
        if not found:
            move_infos.append(
                {
                    "name": m.title(),
                    "desc": "No description found.",
                    "damage_class": "?",
                    "type": "?",
                    "priority": "?",
                    "power": "?",
                }
            )
    return ability_effect, move_infos


def render_effect_text(effect_text, effect_chance=None):
    """
    Replace $effect_chance in effect text with the actual value, and make the text more natural.
    - If effect_chance is 100, remove 'has a 100% chance to' and make it a direct statement.
    - If effect_chance is not None and not 100, replace $effect_chance with the value.
    - If $effect_chance is not in the text, return as is.
    """
    if effect_text is None:
        return None
    if "$effect_chance" not in effect_text:
        return effect_text
    if effect_chance is None:
        return effect_text.replace("$effect_chance", "?")
    try:
        chance = int(effect_chance)
    except Exception:
        return effect_text.replace("$effect_chance", str(effect_chance))
    # If 100%, make it a direct statement
    if chance == 100:
        # Remove 'Has a 100% chance to' or similar phrasing
        import re

        # Try to match and remove the phrase
        new_text = re.sub(r"[Hh]as a 100% chance to ", "", effect_text)
        new_text = new_text.replace("$effect_chance", "100")
        # Capitalize if needed
        if new_text and new_text[0].islower():
            new_text = new_text[0].upper() + new_text[1:]
        return new_text
    else:
        return effect_text.replace("$effect_chance", str(chance))


# --- Discord UI for navigation ---
class AbilityMovesLookupView(discord.ui.View):
    def __init__(
        self, ability_name, move_names, page, total_pages, show_info, requester
    ):
        super().__init__(timeout=120)
        self.ability_name = ability_name
        self.move_names = move_names
        self.page = page
        self.total_pages = total_pages
        self.show_info = show_info
        self.requester = requester

        if show_info:
            # On info page: show Info + Pokémons button
            self.add_item(InfoButton(self))
            self.add_item(PokemonsButton(self))
        else:
            # On results page: show Prev/Next + Info
            self.add_item(PreviousButton(self, disabled=(page <= 0)))
            self.add_item(NextButton(self, disabled=(page >= total_pages - 1)))
            self.add_item(InfoButton(self))


class NextButton(discord.ui.Button):
    def __init__(self, parent, disabled=False):
        super().__init__(
            style=discord.ButtonStyle.secondary,
            emoji=Emojis.right_arrow,
            label="Next",
            disabled=disabled,
        )
        self.parent = parent

    async def callback(self, interaction: discord.Interaction):
        await ability_moves_lookup(
            interaction,
            self.parent.ability_name,
            self.parent.move_names,
            self.parent.page + 1,
            False,
            self.parent.requester,
        )


class PreviousButton(discord.ui.Button):
    def __init__(self, parent, disabled=False):
        super().__init__(
            style=discord.ButtonStyle.secondary,
            emoji=Emojis.left_arrow,
            label="Previous",
            disabled=disabled,
        )
        self.parent = parent

    async def callback(self, interaction: discord.Interaction):
        await ability_moves_lookup(
            interaction,
            self.parent.ability_name,
            self.parent.move_names,
            self.parent.page - 1,
            False,
            self.parent.requester,
        )


class InfoButton(discord.ui.Button):
    def __init__(self, parent):
        super().__init__(
            style=discord.ButtonStyle.secondary, label="Info", emoji=Emojis.info
        )
        self.parent = parent

    async def callback(self, interaction: discord.Interaction):
        await ability_moves_lookup(
            interaction,
            self.parent.ability_name,
            self.parent.move_names,
            self.parent.page,
            True,  # switch to info view
            self.parent.requester,
        )


class PokemonsButton(discord.ui.Button):
    def __init__(self, parent):
        super().__init__(
            style=discord.ButtonStyle.secondary,
            label="Pokémons",
            emoji=Emojis.purple_ball,
        )
        self.parent = parent

    async def callback(self, interaction: discord.Interaction):
        await ability_moves_lookup(
            interaction,
            self.parent.ability_name,
            self.parent.move_names,
            self.parent.page,
            False,  # back to results view
            self.parent.requester,
        )


# --- Main lookup with pagination and info ---
async def ability_moves_lookup(
    interaction_or_message,
    ability_name,
    move_names,
    page=0,
    show_info=False,
    requester=None,
):
    pretty_log(
        "debug",
        f"[ability_moves_lookup] Called with ability_name='{ability_name}', move_names={move_names}, page={page}, show_info={show_info}",
        label="AbilityMovesLookup",
    )
    ability_name = normalize_ability_name(ability_name)
    move_names = [normalize_move_name(m) for m in move_names]
    standard_pokemon, hidden_pokemon = get_ability_learned_by_pokemon(ability_name)
    ability_pokemon_set = set(standard_pokemon + hidden_pokemon)

    if not ability_pokemon_set:
        pretty_log(
            "debug",
            f"[ability_moves_lookup] No Pokémon found for ability '{ability_name}'",
            label="AbilityMovesLookup",
        )
        embed = discord.Embed(
            title=f"Pokémon with Ability '{ability_name}'",
            description="⚠️ No Pokémon found with this ability.",
            color=discord.Color.red(),
        )
        if isinstance(interaction_or_message, discord.Interaction):
            await interaction_or_message.response.edit_message(embed=embed, view=None)
        else:
            await interaction_or_message.reply(embed=embed)
        pretty_log(
            "debug",
            f"[ability_moves_lookup] Sent 'no Pokémon found' embed.",
            label="AbilityMovesLookup",
        )
        return

    combos = get_move_combinations(move_names)
    fields = [
        format_combo_field(
            combo, get_pokemon_with_ability_and_moves(ability_pokemon_set, combo)
        )
        for combo in combos
    ]

    # Check if all fields are '❌ No matches'
    all_no_matches = (
        all(f["value"] == "❌ No matches" for f in fields) if fields else True
    )

    fields_per_page = 5
    total_pages = (len(fields) + fields_per_page - 1) // fields_per_page
    page = max(0, min(page, total_pages - 1))
    paged_fields = fields[page * fields_per_page : (page + 1) * fields_per_page]

    if show_info:
        ability_desc, move_infos = get_info_descriptions(ability_name, move_names)
        embed = discord.Embed(
            title="Ability and Move(s) Info", color=DEFAULT_EMBED_COLOR
        )
        embed.add_field(
            name=f"{Emojis.star} {ability_name.title()} (Ability)",
            value=f">>> {ability_desc}",
            inline=False,
        )
        for move in move_infos:
            other_info_str = f"- **Type:** {move['type'].title()} | **Class:** {move['damage_class'].title()} | **Power:** {move['power']} | **Priority:** {move['priority']}"
            move_value = f"{other_info_str}\n>>> {move['desc']}"
            embed.add_field(
                name=f"{Emojis.flower2} {move['name']} (Move)",
                value=move_value,
                inline=False,
            )
        embed.set_footer(text=f"Info page")
    else:
        if all_no_matches:
            try:
                await interaction_or_message.reply(
                    "No possible combination for ability and moves."
                )
                pretty_log(
                    "debug",
                    f"[ability_moves_lookup] Sent plain text 'no possible combination' message.",
                    label="AbilityMovesLookup",
                )
            except Exception as e:
                pretty_log(
                    "error",
                    f"[ability_moves_lookup] Exception sending plain text: {e}",
                    label="AbilityMovesLookup",
                    include_trace=True,
                )
            return
        else:
            embed = discord.Embed(
                title=f"{Emojis.cupcake} Pokémon with Ability '{ability_name.title()}'",
                color=DEFAULT_EMBED_COLOR,
            )
            for f in paged_fields:
                embed.add_field(**f)
            embed.set_footer(text=f"Page {page+1}/{total_pages}")

    view = AbilityMovesLookupView(
        ability_name, move_names, page, total_pages, show_info, requester
    )


    try:
        if isinstance(interaction_or_message, discord.Interaction):
            await interaction_or_message.response.edit_message(embed=embed, view=view)
            pretty_log(
                "debug",
                f"[ability_moves_lookup] Sent embed via interaction.edit_message.",
                label="AbilityMovesLookup",
            )
        else:
            await interaction_or_message.reply(embed=embed, view=view)
            pretty_log(
                "debug",
                f"[ability_moves_lookup] Sent embed via message.reply.",
                label="AbilityMovesLookup",
            )
    except Exception as e:
        pretty_log(
            "error",
            f"[ability_moves_lookup] Exception sending embed: {e}",
            label="AbilityMovesLookup",
            include_trace=True,
        )
