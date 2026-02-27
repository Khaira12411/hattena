import asyncio

import discord

from straydex.desc import *
from straydex.embeds import *

# === Example async handlers for ARs ===


async def wb_info(boss: str):
    # Simulate fetching or generating info for a World Boss
    await asyncio.sleep(0.1)  # simulate async call (DB, API, etc)
    return f"🌟 World Boss Info for **{boss.upper()}**"


async def mega_chamber_info(stage: str = None):
    # Example Mega Chamber AR handler
    await asyncio.sleep(0.1)
    if stage:
        return f"⚔️ Mega Chamber Strategy for stage **{stage}**"
    return "⚔️ General Mega Chamber info."


async def default_response():
    return "❓ This command is not yet implemented."


# === Straydex AR dictionary mapping ===
straydex_ar = {
    "h": {
        "": {
            "text": SD_MAIN_DESC.h,
            "image_url": SD_MAIN_IMAGES.Help,
            "function": build_sd_main_embed,
        }
    },
    "ba": {
        "": {
            "text": SD_MAIN_DESC.ba,
            "image_url": SD_MAIN_IMAGES.Battle,
            "function": build_sd_main_embed,
        }
    },
    "ac": {
        "": {
            "text": SD_MAIN_DESC.ac,
            "image_url": SD_MAIN_IMAGES.AC,
            "function": build_sd_main_embed,
        }
    },
    "co": {
        "": {
            "text": SD_MAIN_DESC.co,
            "image_url": SD_MAIN_IMAGES.Coll,
            "function": build_sd_main_embed,
        }
    },
    "ev": {
        "": {
            "text": SD_MAIN_DESC.ev,
            "image_url": SD_MAIN_IMAGES.Events,
            "function": build_sd_main_embed,
        }
    },
    "ex": {
        "": {
            "text": SD_MAIN_DESC.ex,
            "image_url": SD_MAIN_IMAGES.Explore,
            "function": build_sd_main_embed,
        }
    },
    "fa": {
        "": {
            "text": SD_MAIN_DESC.fa,
            "image_url": SD_MAIN_IMAGES.Factions,
            "function": build_sd_main_embed,
        }
    },
    "it": {
        "": {
            "text": SD_MAIN_DESC.it,
            "image_url": SD_MAIN_IMAGES.Items,
            "function": build_sd_main_item_embed,
        }
    },
    "mc": {
        "": {
            "text": SD_MAIN_DESC.mc,
            "image_url": SD_MAIN_IMAGES.MC,
            "function": build_sd_main_embed,
        }
    },
    "mh": {
        "": {
            "text": SD_MAIN_DESC.mh,
            "image_url": SD_MAIN_IMAGES.MH,
            "function": build_sd_main_embed,
        }
    },
    "mr": {
        "": {
            "text": SD_MAIN_DESC.mr,
            "image_url": SD_MAIN_IMAGES.MR,
            "function": build_sd_main_embed,
        }
    },
    "pa": {
        "": {
            "patreon": "COMMON",
            "function": build_sd_main_patreon_embed,
        }
    },
    "po": {
        "": {
            "text": SD_MAIN_DESC.po,
            "image_url": SD_MAIN_IMAGES.Pokemon,
            "function": build_sd_main_embed,
        }
    },
    "tr": {
        "": {
            "function": build_sd_main_trainer_embed,
        }
    },
    "ty": {
        "": {
            "text": SD_MAIN_DESC.ty,
            "image_url": SD_MAIN_IMAGES.Types,
            "function": build_sd_main_embed,
        }
    },
    "wb": {
        "": {
            "text": SD_MAIN_DESC.wb,
            "image_url": SD_MAIN_IMAGES.WB,
            "function": build_sd_main_embed,
        },
    },
    "ubg": {
        "": {
            "text": SD_MAIN_DESC.ubg,
            "image_url": SD_MAIN_IMAGES.UBG,
            "function": build_sd_main_embed,
        }
    },
    "sz": {
        "": {
            "text": SD_MAIN_DESC.sz,
            "image_url": SD_MAIN_IMAGES.SZ,
            "function": build_sd_main_embed,
        }
    },

    "straymon": {
        "": {
            "text": SD_STRAYMON_DESC.sm1,
            "image_url": None,
            "image_url_second": SD_MAIN_IMAGES.Straymons_Clan,
            "text_second": SD_STRAYMON_DESC.sm2,
            "function": build_sd_two_embed,
        }
    },
    "ic": {
        "": {
            "text": SD_MAIN_DESC.ic,
            "image_url": SD_MAIN_IMAGES.Icons,
            "function": build_sd_main_embed,
        }
    },
}

# Pokemon AR
po_sub_no_buttons = [
    "gro",
    "inc",
    "lao",
    "met",
    "sla",
    "yve",
    "sol",
    "zek",
    "res",
    "lug",
    "gar",
    "xer",
    "gir",
    "ete",
    "tyr",
    "hat",
    "cor",
]
po_sub_w_buttons = [
    "pal",
    "nec",
    "deb",
    "kyu",
    "mew",
    "kyo",
    "dia",
    "ray",
    "nor",
    "set",
    "arc",
    "zac",
    "wor",
]
for sub in po_sub_no_buttons:
    straydex_ar["po"][sub] = {
        "sub_cmd": sub,
        "function": build_sd_po_embed,
    }
for sub in po_sub_w_buttons:
    straydex_ar["po"][sub] = {
        "sub_cmd": sub,
        "function": build_sd_po_main_embed,
    }

# MC AR
mc_sub = [
    "abo",
    "abs",
    "aer",
    "agg",
    "ala",
    "alt",
    "amp",
    "aud",
    "ban",
    "bee",
    "bla",
    "blz",
    "cam",
    "chx",
    "chy",
    "dia",
    "gal",
    "gar",
    "gav",
    "gen",
    "gla",
    "gya",
    "her",
    "hou",
    "kan",
    "laa",
    "lao",
    "lop",
    "luc",
    "man",
    "maw",
    "med",
    "met",
    "mmx",
    "mmy",
    "pid",
    "pin",
    "ray",
    "sab",
    "sal",
    "sce",
    "sci",
    "sha",
    "slo",
    "ste",
    "swa",
    "tyr",
    "ven",
]
for sub in mc_sub:
    straydex_ar["mc"][sub] = {
        "sub_cmd": sub,
        "function": build_sd_main_mc_embed,
    }

# FA AR
fa_sub = ["i", "fa", "aq", "fl", "ga", "ma", "pl", "sk", "ye", "ro"]
for sub in fa_sub:
    if sub == "i":
        straydex_ar["fa"][sub] = {
            "text": SD_FA_DESC.i,
            "function": build_sd_main_embed,
        }
    else:
        straydex_ar["fa"][sub] = {
            "sub_cmd": sub,
            "function": build_sd_main_fa_embed,
        }

# WB AR
wb_bosses = [
    "i",
    "gri",
    "uss",
    "alc",
    "app",
    "fla",
    "but",
    "coa",
    "cop",
    "cor",
    "hat",
    "mel",
    "cha",
    "bla",
    "cen",
    "cin",
    "dre",
    "dur",
    "eet",
    "eev",
    "gar",
    "gen",
    "int",
    "kin",
    "lap",
    "mac",
    "meo",
    "pik",
    "ril",
    "san",
    "sno",
    "tox",
    "urs",
    "ven",
]
for boss in wb_bosses:
    if boss == "i":
        straydex_ar["wb"][boss] = {
            "text": WB_ConsitentStrat.i,
            "function": build_sd_main_embed,
            "image_url": SD_MAIN_IMAGES.WB,
        }
    else:
        straydex_ar["wb"][boss] = {
            "function": build_sd_wb_embed,
    }
# Achievement AR
ac_sub = ["bat", "cat", "dex", "fis", "gen", "ite", "res"]
for sub in ac_sub:
    straydex_ar["ac"][sub] = {
        "text": getattr(SD_AC, sub),
        "function": build_sd_main_embed,
    }

# 🐾 Battle AR Subcommand Setup

# 🌸 Standard battle subcommands → use normal embed (cute and simple!)
standard_battle_sub = ["reg", "ti", "ic"]

# ✨ Special battle subcommands → use battle-specific embed (extra flair!)
special_battle_sub = ["cba", "cbo", "cma", "cse", "leg", "ts"]

# 🍰 Assign handlers for standard subcommands
for sub in standard_battle_sub:
    straydex_ar["ba"][sub] = {
        "text": getattr(
            SD_BATTLE_DESC, sub
        ),  # 📝 Grab the description from SD_BATTLE_DESC
        "function": build_sd_main_embed,  # 🎨 Use the standard embed builder
    }

# 🎀 Assign handlers for special subcommands
for sub in special_battle_sub:
    data = sd_battle_dict[sub]
    straydex_ar["ba"][sub] = {
        "text": data["desc"],
        "button_label": data["button_label"],
        "button_emoji": data["button_emoji"],
        "thumbnail_url": data["thumbnail_url"],
        "sub_cmd": sub,  # 🗝️ Pass the key so the handler knows which battle type to load
        "function": build_sd_main_battle_embed,  # ✨ Battle-special embed builder for extra sparkle
    }


# Meowhelper AR
mh_sub = ["lo", "mi", "pi", "ti", "ut", "go"]
for sub in mh_sub:
    straydex_ar["mh"][sub] = {
        "text": getattr(SD_MH, sub),
        "function": build_sd_main_embed,
    }


# EV AR
ev_sub = ["gpi", "gpp"]
for sub in ev_sub:
    if sub == "gpp":
        straydex_ar["ev"][sub] = {
            "text": getattr(SD_EV, sub),
            "function": build_sd_main_embed,
        }
    else:
        straydex_ar["ev"][sub] = {
            "text": getattr(SD_EV, sub),
            "text_second": "# SAMPLE ANSWER",
            "image_url": getattr(SD_MAIN_IMAGES, "Sample_Riddle"),
            "image_url_second": getattr(SD_MAIN_IMAGES, "Answered_Riddle"),
            "function": build_sd_two_embed,
        }
# IT AR
it_sub = [
    "amuletcoin",
    "assaultvest",
    "auxguard",
    "auxpower",
    "auxpowerguard",
    "blackbelt",
    "blackglasses",
    "bosscoin",
    "catchingcharm",
    "charcoal",
    "choiceband",
    "choicecloak",
    "choicescarf",
    "choicespecs",
    "dowsingmachine",
    "dragonfang",
    "dxp",
    "evostone",
    "expcharm",
    "expertbelt",
    "expshare",
    "fairyfeather",
    "fluffytail",
    "focusband",
    "focussash",
    "fullrestore",
    "grazz",
    "grepaberry",
    "hardstone",
    "hondewberry",
    "honey",
    "incense",
    "incubator",
    "itemring",
    "kelpsyberry",
    "largepack",
    "leftovers",
    "lifeorb",
    "loadeddice",
    "luckincense",
    "luckyegg",
    "magnet",
    "maxpotion",
    "maxrepel",
    "maxrevive",
    "metronome",
    "miracleseed",
    "mistylure",
    "mysticwater",
    "nevermeltice",
    "poisonbarb",
    "pokedoll",
    "pokelure",
    "pokeradar",
    "poketoy",
    "pomegberry",
    "poweranklet",
    "powerband",
    "powerbelt",
    "powerbracer",
    "powerlens",
    "powerweight",
    "qrs",
    "qualotberry",
    "quickclaw",
    "rarecandy",
    "repel",
    "scanner",
    "seaflute",
    "sharpbeak",
    "shinycharm",
    "silkscarf",
    "silverpowder",
    "sitrusberry",
    "softsand",
    "soothebell",
    "spelltag",
    "superincubator",
    "superrepel",
    "tamatoberry",
    "teamboost",
    "teammedallion",
    "twistedspoon",
    "wiseglasses",
    "zoomlens",
    "loveball",
    "quickball",
    "heavyball",
    "fastball",
    "friendball",
    "duskball",
    "netball",
    "lureball",
    "luxuryball",
    "moonball",
    "auspiciousarmor",
    "deepseascale",
    "deepseatooth",
    "dubicousdisc",
    "galaricacuff",
    "galaricawreath",
    "maliciousarmor",
    "prismscale",
    "protector",
    "reapercloth",
    "sachet",
    "upgrade",
    "whippeddream",
    "dawnstone",
    "duskstone",
    "firestone",
    "icestone",
    "leafstone",
    "moonstone",
    "opalstone",
    "shinystone",
    "sunstone",
    "thunderstone",
    "waterstone",
    "dragonscale",
    "electirizer",
    "kingsrock",
    "magmarizer",
    "metalcoat",
    "razorclaw",
    "razorfang",
    # Added by user request
    "shadowwing",
    "abilitypatch",
    "abilitycapsule",
    "timegear",
    "scubagear",
    "abilityshield",
    "airballoon",
    "bigroot",
    "clearamulet",
    "covertcloak",
    "eviolite",
    "flameorb",
    "heavydutyboots",
    "lightball",
    "rockyhelmet",
    "safetygoogles",
]

for sub in it_sub:
    straydex_ar[sub] = {
        "text": getattr(SD_IT, sub),
        "image_url": getattr(SD_IT_IMAGES, sub),
        "function": build_sd_item_embed,
    }

# Icon AR
ic_sub = ["fa", "mc"]
for sub in ic_sub:
    straydex_ar["ic"][sub] = {
        "text": getattr(SD_ICONS, sub),
        "function": build_sd_main_embed,
    }



types_list = [
    "bug",
    "dark",
    "dragon",
    "electric",
    "fairy",
    "fighting",
    "fire",
    "flying",
    "ghost",
    "grass",
    "ground",
    "ice",
    "normal",
    "poison",
    "psychic",
    "rock",
    "steel",
    "water",
]


for t in types_list:
    type_info[t] = {
        "thumbnail": type_info[t]["thumbnail"],
        "image": type_info[t]["image"],
        "color": type_info[t]["color"],
        "function": build_sd_type_embed,
    }

# MR Sub Commands:
mr_sub = ["beg", "faq", "cha", "cur", "upg", "end"]
for sub in mr_sub:
    straydex_ar["mr"][sub] = {
        "text": getattr(SD_MR_DESC, sub),
        "function": build_sd_main_embed,
    }

# Explore SubCommands
ex_sub = ["i", "rs", "sg", "sf", "sw", "su"]

for sub in ex_sub:
    if sub in (
        "i",
        "rs",
    ):  # fixed condition, original `if sub == "i" or "rs"` always True
        straydex_ar["ex"][sub] = {
            "text": getattr(SD_EX, sub),
            "function": build_sd_main_embed,  # for example, your normal embed builder
        }
    else:
        # For 'sg', 'sf', 'sw', 'su' subcommands
        # We'll pass the map key and the function to build the secret embed
        straydex_ar["ex"][sub] = {
            "explore_map": sub,  # Pass the map key so the handler knows what map to load
            "function": build_sd_main_secret_embed,
        }
# UBG subcommands
ubg_sub = [
    "cap",
    "cas",
    "cat",
    "cos",
    "cur",
    "dai",
    "fid",
    "fis",
    "loc",
    "lvl",
    "pok",
    "res",
    "swa",
    "tra",
]
for sub in ubg_sub:
    if sub == "cap":
        straydex_ar["ubg"][sub] = {
            "text": getattr(SD_UBG, sub),
            "text_second": None,
            "image_url": getattr(SD_UBG_IMAGES, "captcha1"),
            "image_url_second": getattr(SD_UBG_IMAGES, "captcha2"),
            "function": build_sd_two_embed,
        }
    else:
        straydex_ar["ubg"][sub] = {
            "text": getattr(SD_UBG, sub),
            "image_url": SD_MAIN_IMAGES.UBG,
            "function": build_sd_main_embed,
        }

# Map main commands to their generic handler functions
generic_handlers = {
    "wb": build_sd_wb_embed,
    "ac": build_sd_main_embed,
    "it": build_sd_item_embed,
    # Add more main command handlers here
}
