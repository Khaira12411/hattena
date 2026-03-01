from .keywords import HATT_KEYWORDS
# 🌿───────────────────────────────🌿
# 💜 HATTENA STOPWORDS
# 🌿───────────────────────────────🌿


STOPWORDS = {
    "what",
    "is",
    "the",
    "how",
    "do",
    "i",
    "where",
    "can",
    "a",
    "an",
    "in",
    "on",
    "to",
    "of",
    "for",
    "pls",
    "please",
}
# 🌿───────────────────────────────🌿
# 💜 HATTENA KNOWLEDGE TOPICS
# 🌿───────────────────────────────🌿

TOPICS = {
    "safari_zone_info": {
        "keywords": HATT_KEYWORDS.safari_zone,
        "cmd": "szi",
    },
    "safari_zone_secrets": {
        "keywords": HATT_KEYWORDS.safari_zone_secrets,
        "cmd": "szse",
    },
}
