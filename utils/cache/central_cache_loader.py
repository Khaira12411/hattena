# 💜────────────────────────────────────────────
#       🟣 Centralized Cache Loader 💜
#       🎀 Calls all individual caches 🎀
# 💜────────────────────────────────────────────


from utils.cache.cache_list import market_value_cache
from utils.db.market_value_db import load_market_cache_from_db
from utils.logs.pretty_log import pretty_log
from utils.cache.webhook_url_cache import load_webhook_url_cache
from .straymon_member_cache import load_straymon_member_cache
from .straydex_guild_cache import load_straydex_guild_cache
from .abilities_cache import load_abilities_cache

# 💜────────────────────────────────────────────
#     🟣 Load Everything in One Go
# 💜────────────────────────────────────────────
async def load_all_caches(bot):
    """
    Centralized function to load all caches.
    Calls each cache loader and logs memory summary.
    """
    try:

        # 💠 Load Straymon Member Cache
        await load_straymon_member_cache(bot)

        # 🌐 Load Webhook URLs
        await load_webhook_url_cache(bot)

        # 🛒 Load Market Value Cache from database
        await load_market_cache_from_db(bot)

        # 🗺️ Load Straydex Guild Cache
        await load_straydex_guild_cache(bot)

        """# 🌸 Load Abilities Cache
        await load_abilities_cache(bot)"""

        # 🎀 Unified summary log
        pretty_log(
            tag="",
            label="🦋 CENTRAL CACHE",
            message=(f"All caches refreshed and loaded "),
        )
    except Exception as e:
        pretty_log(
            tag="error",
            message=f"Failed to load all caches: {e}",
        )
