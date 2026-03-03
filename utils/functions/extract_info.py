import re

# Define patterns for different info types
INFO_PATTERNS = {
    "catch rate": [
        r"catch rate.*?(\d+%)",
        r"base catch rate.*?(\d+%)",
    ],
    "method to obtain": [
        r"METHOD TO OBTAIN:\s*-\s*(.+)",
        r"obtainable.*",
    ],
    "friendship gain": [
        r"friendship gain.*?(\d+x)",
    ],
    "time condition": [
        r"night time.*?(\d+%)",
    ],
}

# Synonyms mapping (so users can ask in natural language)
SYNONYMS = {
    "catch rate": ["chance", "probability", "rate", "success"],
    "method to obtain": ["get", "find", "obtain", "reward", "source"],
    "friendship gain": ["friendship", "bond", "affection"],
    "time condition": ["night", "day", "time"],
}


def extract_info(user_message: str, description: str):
    user_message_lower = user_message.lower()

    # Try to match based on synonyms
    for info_type, synonyms in SYNONYMS.items():
        if any(word in user_message_lower for word in synonyms + [info_type]):
            # Search description with patterns
            for pattern in INFO_PATTERNS.get(info_type, []):
                match = re.search(pattern, description, re.IGNORECASE | re.DOTALL)
                if match:
                    return f"{info_type.capitalize()}: {match.group(1).strip()}"
            # If no regex match, return section fallback
            if info_type == "method to obtain":
                # Grab everything after METHOD TO OBTAIN
                method_match = re.search(
                    r"\*\*METHOD TO OBTAIN:\*\*(.*)",
                    description,
                    re.IGNORECASE | re.DOTALL,
                )
                if method_match:
                    return f"Method to obtain: {method_match.group(1).strip()}"
    return "I found the item, but I’m not sure which detail you want."
