# 💫━━━━━━━━━━━━━━━━━━━━━━━━━
#       🌸 Market Value Cache 🌸
# 💫━━━━━━━━━━━━━━━━━━━━━━━━━
market_value_cache: dict[str, dict] = {}
# Structure:
# {
#   "pokemon_name": {
#       "pokemon": str,
#       "dex_number": int,
#       "is_exclusive": bool,
#       "lowest_market": int,
#       "current_listing": int,
#       "true_lowest": int,
#       "listing_seen": int,
#       "image_link": str | None,
#       "rarity": str,
#       "emoji_id": str,
#       "base_atk": int,
#       "base_def": int,
#       "base_hp": int,
#       "base_spa": int,
#       "base_spd": int,
#       "base_spe": int,
#       "weight": int,
#       "ability": str,
#   },
#   ...
# }

# 💫━━━━━━━━━━━━━━━━━━━━━━━━━
#       🌸 Straymon Member Cache 🌸
# 💫━━━━━━━━━━━━━━━━━━━━━━━━━
straymon_member_cache: dict[int, dict] = {}
# Structure:
# user_id -> {
#   "user_name": str,
#   "channel_id": int
#   "faction": str
# }

# 💫━━━━━━━━━━━━━━━━━━━━━━━━━
#       🌸 Webhook URL Cache 🌸
# 💫━━━━━━━━━━━━━━━━━━━━━━━━━
webhook_url_cache: dict[int, dict] = {}
# Structure:
# {
#   channel_id: {
#       "channel_name": str,
#       "url": str,
#   },
#   ...
