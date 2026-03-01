import re

from constants.ask_hattena.overall import STOPWORDS, TOPICS
from utils.logs.debug_log import debug_enabled, debug_log, enable_debug
enable_debug(f"{__name__}.match_topic")
def normalize(text: str) -> list[str]:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)  # remove punctuation
    tokens = text.split()
    return [t for t in tokens if t not in STOPWORDS]


def match_topic(user_message: str):
    raw = user_message.lower()
    raw = re.sub(r"[^a-z0-9\s]", "", raw)

    tokens = normalize(user_message)
    debug_log(f"Raw: {raw}")
    debug_log(f"Tokens: {tokens}")

    topic_scores = {}
    topic_matches = {}

    for topic_name, topic_data in TOPICS.items():
        matched_keywords = set()

        for keyword in topic_data["keywords"]:
            keyword = keyword.lower()
            if keyword in raw or keyword in tokens:
                matched_keywords.add(keyword)

        score = len(matched_keywords)
        topic_scores[topic_name] = score
        topic_matches[topic_name] = matched_keywords

        debug_log(
            f"Topic '{topic_name}' matched keywords: {matched_keywords}, score: {score}"
        )

    # 🚨 UNIQUE KEYWORD OVERRIDE
    for topic, matches in topic_matches.items():
        for keyword in matches:
            if all(
                keyword not in other_matches
                for other_topic, other_matches in topic_matches.items()
                if other_topic != topic
            ):
                debug_log(
                    f"Unique keyword '{keyword}' found in topic '{topic}' → override"
                )
                return topic

    best_score = max(topic_scores.values(), default=0)
    if best_score == 0:
        debug_log("No matches found → returning None")
        return None

    tied_topics = [t for t, s in topic_scores.items() if s == best_score]
    debug_log(f"Tied topics: {tied_topics} with score {best_score}")

    if len(tied_topics) == 1:
        debug_log(f"Winner: {tied_topics[0]}")
        return tied_topics[0]

    # 🧠 fallback: more matches wins
    best_topic = max(tied_topics, key=lambda t: len(topic_matches[t]), default=None)
    debug_log(f"Fallback winner: {best_topic}")
    return best_topic
