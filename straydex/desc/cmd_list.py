from straydex.AR.h import (
    fa_sub,
    mc_sub,
    po_sub_no_buttons,
    po_sub_w_buttons,
    safari_zone_sub,
    wb_bosses,
    ac_sub,
    standard_battle_sub,
    special_battle_sub,
    mh_sub,
    ev_sub,
    it_sub,
    ic_sub,
    types_list,
    mr_sub,
    ex_sub,
    ubg_sub,
)

list_of_main_straydex_cmds = [
    "ac",  # Achievement Codex
    "ba",  # Battle Codex
    "co",  # Collection Codex
    "ev",  # Event Codex
    "ex",  # Explore Codex
    "fa",  # Faction Codex
    "ic",  # Icon Codex
    "it",  # Item Codex
    "mc",  # Mega Chamber Codex
    "mh",  # Meowhelper Codex
    "mr",  # Meowrogue Codex
    "pa",  # Patreon Codex
    "po",  # Pokemon Codex
    "ps",  # Power Station Codex
    "rps",  # RPS Game Codex
    "sz",  # Safari Zone Codex
    "tcg",  # TCG Codex
    "tr",  # Trainer Codex
    "ty",  # Types Codex
    "wb",  # World Boss Codex
    "ubg",  # Ultimate Beginner Guide
    "straymon",  # Straymon Clan
]
safari_cmds = []
for sub in safari_zone_sub:
    safari_cmds.append("sz" + sub)

pokemon_cmds = []
for sub in po_sub_no_buttons:
    pokemon_cmds.append("po" + sub)
for sub in po_sub_w_buttons:
    pokemon_cmds.append("po" + sub)

mc_cmds = []
for sub in mc_sub:
    mc_cmds.append("mc" + sub)

fa_cmds = []
for sub in fa_sub:
    fa_cmds.append("fa" + sub)

wb_cmds = []
for sub in wb_bosses:
    wb_cmds.append("wb" + sub)

ac_cmds = []
for sub in ac_sub:
    ac_cmds.append("ac" + sub)

battle_cmds = []
for sub in standard_battle_sub:
    battle_cmds.append("ba" + sub)
for sub in special_battle_sub:
    battle_cmds.append("ba" + sub)

mh_cmds = []
for sub in mh_sub:
    mh_cmds.append("mh" + sub)

ev_cmds = []
for sub in ev_sub:
    ev_cmds.append("ev" + sub)

