# 💫━━━━━━━━━━━━━━━━━━━━━━━━━
#       🌸 Market Value Cache 🌸
# 💫━━━━━━━━━━━━━━━━━━━━━━━━━
market_value_cache: dict[str, dict] = {}

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
