import random

import discord


def parse_embed_color(value: str | int | None) -> int | None:
    """
    Converts a color input to a Discord-compatible decimal color.
    Accepts:
      - Hex string with or without # (e.g., '#b19cd9', 'b19cd9')
      - Decimal int (e.g., 11674137)
    Returns:
      - int in range 0..16777215
      - None if invalid
    """
    if value is None:
        return None

    if isinstance(value, int):
        if 0 <= value <= 0xFFFFFF:
            return value  # ✅ Already valid 24-bit
        # If too big (ARGB), strip alpha/top byte
        if value > 0xFFFFFF:
            return value & 0xFFFFFF
        return None

    if isinstance(value, str):
        val = value.strip().lstrip("#")
        try:
            # Try hex first
            if all(c in "0123456789abcdefABCDEF" for c in val):
                return int(val, 16)
            # Otherwise, treat as decimal
            return int(val) & 0xFFFFFF
        except ValueError:
            return None

    return None


# 💙 PASTEL BLUES
PASTEL_BLUE_COLORS = [
    discord.Color.from_rgb(173, 216, 230),  # Light Blue 🩵
    discord.Color.from_rgb(176, 224, 230),  # Powder Blue 🧊
    discord.Color.from_rgb(135, 206, 250),  # Light Sky Blue 🌤️
    discord.Color.from_rgb(175, 238, 238),  # Pale Turquoise 🌊
    discord.Color.from_rgb(191, 239, 255),  # Cloudy Blue ☁️
    discord.Color.from_rgb(180, 220, 250),  # Soft Blue 🫐
    discord.Color.from_rgb(200, 230, 255),  # Ice Blue 🧊
]

# 💚 PASTEL GREENS
PASTEL_GREEN_COLORS = [
    discord.Color.from_rgb(152, 251, 152),  # Pale Green 🪴
    discord.Color.from_rgb(144, 238, 144),  # Light Green 🥒
    discord.Color.from_rgb(193, 255, 193),  # Minty Green 🌿
    discord.Color.from_rgb(204, 255, 229),  # Aloe Mist 🧼
    discord.Color.from_rgb(178, 255, 221),  # Seafoam Green 🧽
    discord.Color.from_rgb(202, 255, 191),  # Pastel Avocado 🥑
]

# 💖 PASTEL PINKS
PASTEL_PINK_COLORS = [
    discord.Color.from_rgb(255, 182, 193),  # Light Pink 🌸
    discord.Color.from_rgb(255, 192, 203),  # Baby Pink 🍼
    discord.Color.from_rgb(255, 209, 220),  # Cotton Candy 🍬
    discord.Color.from_rgb(255, 200, 230),  # Sakura Blush 🌺
    discord.Color.from_rgb(255, 228, 237),  # Rosy Cloud ☁️
]

# 💜 PASTEL PURPLES
PASTEL_PURPLE_COLORS = [
    discord.Color.from_rgb(216, 191, 216),  # Thistle 💐
    discord.Color.from_rgb(221, 160, 221),  # Plum Cream 🍇
    discord.Color.from_rgb(230, 200, 250),  # Lavender Milk 🥛
    discord.Color.from_rgb(200, 162, 200),  # Soft Violet 🫧
    discord.Color.from_rgb(224, 192, 255),  # Lilac Mist 🌫️
]

# 💛 PASTEL YELLOWS
PASTEL_YELLOW_COLORS = [
    discord.Color.from_rgb(255, 255, 224),  # Light Yellow 🍋
    discord.Color.from_rgb(250, 250, 210),  # Lemon Chiffon 🍰
    discord.Color.from_rgb(255, 255, 153),  # Banana Milk 🍌
    discord.Color.from_rgb(255, 255, 170),  # Dandelion Glow 🌼
    discord.Color.from_rgb(255, 250, 205),  # Buttercup 🧈
]

# 🧡 PASTEL ORANGES
PASTEL_ORANGE_COLORS = [
    discord.Color.from_rgb(255, 204, 153),  # Apricot 🍑
    discord.Color.from_rgb(255, 218, 185),  # Peach Puff 🍑
    discord.Color.from_rgb(255, 229, 180),  # Creamsicle 🍦
    discord.Color.from_rgb(255, 221, 179),  # Orange Sherbet 🍧
    discord.Color.from_rgb(255, 200, 150),  # Soft Tangerine 🍊
]

# 🌊 PASTEL TEALS
PASTEL_TEAL_COLORS = [
    discord.Color.from_rgb(175, 238, 238),  # Pale Turquoise 🐬
    discord.Color.from_rgb(180, 255, 250),  # Light Aqua 💧
    discord.Color.from_rgb(150, 222, 209),  # Seafoam 🌿
    discord.Color.from_rgb(170, 255, 238),  # Soft Teal 🧵
    discord.Color.from_rgb(160, 240, 230),  # Misty Teal 🫖
]

# 🧸 PASTEL BROWNS
PASTEL_BROWN_COLORS = [
    discord.Color.from_rgb(222, 184, 135),  # Burlywood 🍞
    discord.Color.from_rgb(210, 180, 140),  # Tan 👜
    discord.Color.from_rgb(230, 200, 170),  # Soft Caramel 🍯
    discord.Color.from_rgb(200, 170, 140),  # Latte ☕
    discord.Color.from_rgb(245, 222, 179),  # Wheat 🥖
]

# ❤️ PASTEL REDS
PASTEL_RED_COLORS = [
    discord.Color.from_rgb(255, 160, 160),  # Light Coral 🌺
    discord.Color.from_rgb(255, 182, 180),  # Soft Blush 🍓
    discord.Color.from_rgb(255, 204, 203),  # Cherry Cream 🍒
    discord.Color.from_rgb(250, 150, 150),  # Strawberry Milk 🥛
    discord.Color.from_rgb(255, 190, 190),  # Rosy Mist 🌹
]


def get_pastel_color_by_name(name: str | None = None):
    """Return a random pastel color based on the given name."""
    pastel_map = {
        "red": get_random_pastel_red,
        "blue": get_random_pastel_blue,
        "green": get_random_pastel_green,
        "pink": get_random_pastel_pink,
        "purple": get_random_pastel_purple,
        "yellow": get_random_pastel_yellow,
        "orange": get_random_pastel_orange,
        "teal": get_random_pastel_teal,
        "brown": get_random_pastel_brown,
    }

    if name is None:
        return get_random_pastel_color()  # fallback to any pastel

    # Normalize string
    key = name.lower()
    if key in pastel_map:
        return pastel_map[key]()  # call the corresponding getter
    else:
        return get_random_pastel_color()  # fallback if unknown


def get_random_pastel_red():
    return random.choice(PASTEL_RED_COLORS)


# === 🌷 Pastel Getters ===
def get_random_pastel_red():
    return random.choice(PASTEL_RED_COLORS)


def get_random_pastel_blue():
    return random.choice(PASTEL_BLUE_COLORS)


def get_random_pastel_green():
    return random.choice(PASTEL_GREEN_COLORS)


def get_random_pastel_pink():
    return random.choice(PASTEL_PINK_COLORS)


def get_random_pastel_purple():
    return random.choice(PASTEL_PURPLE_COLORS)


def get_random_pastel_yellow():
    return random.choice(PASTEL_YELLOW_COLORS)


def get_random_pastel_orange():
    return random.choice(PASTEL_ORANGE_COLORS)


def get_random_pastel_teal():
    return random.choice(PASTEL_TEAL_COLORS)


def get_random_pastel_brown():
    return random.choice(PASTEL_BROWN_COLORS)


def get_random_pastel_color():
    all_pastel_colors = (
        PASTEL_BLUE_COLORS
        + PASTEL_GREEN_COLORS
        + PASTEL_PINK_COLORS
        + PASTEL_PURPLE_COLORS
        + PASTEL_YELLOW_COLORS
        + PASTEL_ORANGE_COLORS
        + PASTEL_TEAL_COLORS
        + PASTEL_BROWN_COLORS
        + PASTEL_RED_COLORS
    )
    return random.choice(all_pastel_colors)
