import discord
from discord.ui import View, Button
from straydex.desc import SD_EX_DICT

class SDExploreHelper:
    """
    🌟 SDExploreHelper - Your friendly helper to explore secret map info! 🌟

    This helper class wraps around your nested SD_EX_DICT data structure,
    making it super easy to fetch texts, secrets, images, colors, and icons
    related to different maps like grass, fire, water, and underwater.

    How to use:
    1. Create an instance by passing your nested dictionary:
       helper = SDExploreHelper(SD_EX_DICT)

    2. Use the handy methods to get info for a specific map key ('sg', 'sf', etc.):
       - helper.get_text("sg")          # Gets main description text for grass map
       - helper.get_secret("sg", "sg3") # Gets secret #3 under grass map
       - helper.get_image("sw", "sw2")  # Gets image URL for water map secret #2
       - helper.get_color("sf")         # Gets color code for fire map
       - helper.list_secrets("su")      # Gets all underwater map secrets as a dict

    Each method gracefully returns defaults if keys are missing,
    so no worries about KeyErrors or crashes! 🛡️
    """

    def __init__(self, data_dict):
        self.data = data_dict  # Store your magical nested dictionary here

    def get_text(self, map_key):
        """✨ Get the main description text for a map (like 'sg' for grass map)."""
        return self.data.get(map_key, {}).get("text", "No description found. ❌")

    def get_secret(self, map_key, secret_key):
        """🔍 Retrieve a specific secret's text under a map (e.g., 'sg3' under 'sg')."""
        return (
            self.data.get(map_key, {})
            .get("secrets", {})
            .get(secret_key, "Secret not found! 🕵️‍♂️")
        )

    def get_image(self, map_key, image_key):
        """🖼️ Fetch the image URL for a particular secret or map image."""
        return self.data.get(map_key, {}).get("images", {}).get(image_key, None)

    def get_color(self, map_key):
        """🎨 Get the color integer (discord embed color) for a given map."""
        return self.data.get(map_key, {}).get("color", 0)  # Default black if missing

    def get_header_icon(self, map_key):
        """🖼️ Get the header icon URL for a map (shown at the top of embeds)."""
        return self.data.get(map_key, {}).get("header_icon", "")

    def get_footer_icon(self, map_key):
        """🖼️ Get the footer icon URL for a map (shown at the bottom of embeds)."""
        return self.data.get(map_key, {}).get("footer_icon", "")

    def get_header_text(self, map_key):
        """📋 Get the header text for a map (like 'TOTAL SECRETS: 7')."""
        return self.data.get(map_key, {}).get("header_text", "")

    def get_footer_text(self, map_key):
        """📋 Get the footer text for a map (like 'UNLOCKABLE: Golden Treecko')."""
        return self.data.get(map_key, {}).get("footer_text", "")

    def list_secrets(self, map_key):
        """🗝️ Return all secrets for a map as a dict: secret_key -> secret_text."""
        return self.data.get(map_key, {}).get("secrets", {})

    def list_images(self, map_key):
        """🖼️ Return all images for a map as a dict: image_key -> image_url."""
        return self.data.get(map_key, {}).get("images", {})


async def build_sd_secret_embed(sd_helper, explore_map: str, secret_key: str):
    """
    ✨ Build a Discord embed for a specific secret in a map.

    Parameters:
    - sd_helper: SDExploreHelper instance to fetch data from your secrets dict.
    - explore_map: The map key (e.g., 'sg', 'sf', 'sw', 'su') — identifies which map.
    - secret_key: The specific secret key within the map (e.g., 'sg1', 'sf2').

    Returns:
    - discord.Embed ready to send with the secret's text, colors, and icons.
    """
    secret_text = sd_helper.list_secrets(explore_map).get(
        secret_key, "No secret found. 💨"
    )
    color = sd_helper.get_color(explore_map)
    header_icon = sd_helper.get_header_icon(explore_map)
    footer_icon = sd_helper.get_footer_icon(explore_map)
    header_text = sd_helper.get_header_text(explore_map)
    footer_text = sd_helper.get_footer_text(explore_map)
    image_url = sd_helper.get_image(map_key=explore_map, image_key=secret_key)
    # def get_image(self, map_key, image_key):

    embed = discord.Embed(
        description=secret_text,
        color=color,
    )
    embed.set_author(name=header_text, icon_url=header_icon)
    embed.set_footer(text=footer_text, icon_url=footer_icon)
    embed.set_image(url=image_url)

    return embed


async def build_sd_main_secret_embed(
    guild: discord.Guild,
    explore_map: str,
    user_id: int,
    user_display_name: str,
):
    """
    🎀 Build the main secret embed and the button view for navigating secrets in a map.

    Parameters:
    - guild: Discord guild to get icon or other guild-related info.
    - explore_map: The map key, e.g. 'sg', 'sf', 'sw', 'su'.
    - user_id: Discord user ID allowed to interact with the buttons.

    Returns:
    - If the map has no secrets (like 'su'), returns just the embed.
    - Otherwise returns a tuple: (embed, SecretSelectionView, None)
    """
    sd_helper = SDExploreHelper(SD_EX_DICT)

    # For initial display, pick the first secret key available or a sensible default
    secret_keys = list(sd_helper.list_secrets(explore_map).keys())
    initial_secret = secret_keys[0] if secret_keys else None
    # If map is 'su' (underwater) or has no secrets, return embed only

    desc = sd_helper.get_text(explore_map)
    color = sd_helper.get_color(explore_map)
    header_icon = sd_helper.get_header_icon(explore_map)
    footer_icon = sd_helper.get_footer_icon(explore_map)
    header_text = sd_helper.get_header_text(explore_map)
    footer_text = sd_helper.get_footer_text(explore_map)
    image_url = sd_helper.get_image(explore_map, explore_map)

    embed = discord.Embed(description=desc, color=color)
    embed.set_author(name=header_text, icon_url=header_icon)
    embed.set_footer(text=footer_text, icon_url=footer_icon)
    embed.set_image(url=image_url)

    if explore_map == "su":
        return embed
    else:
        view = SecretSelectionView(sd_helper, explore_map, initial_secret, user_id)
        return embed, view, None


def map_label(secret_key: str) -> str:
    # Remove all non-numeric suffix, default to 1 if none found
    import re

    match = re.search(r"(\d+)$", secret_key)
    map_num = int(match.group(1)) if match else 1
    return f"Map {map_num}"


class SecretSelectionView(View):
    """
    💙 Interactive view with buttons for each secret in a map.

    Only the user with matching user_id can interact to switch secrets.

    Clicking a secret button updates the embed to show that secret's info,
    and disables that secret's button to show it’s active.
    """

    def __init__(self, sd_helper, explore_map: str, current_secret: str, user_id: int):
        super().__init__(timeout=None)  # persistent view, no timeout
        self.sd_helper = sd_helper
        self.map_key = explore_map
        self.current_secret = current_secret
        self.user_id = user_id

        # Load all secrets for this map, e.g. {"sg1": "...", "sg2": "..."}
        self.secrets = self.sd_helper.list_secrets(self.map_key)

        # Add one button per secret to the view
        for secret_key in self.secrets.keys():
            self.add_item(self.make_button(secret_key))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        """👮 Allow only the authorized user to interact with buttons."""
        if interaction.user.id != self.user_id:
            await interaction.response.send_message(
                "Sorry, this button isn't for you! 💢", ephemeral=True
            )
            return False
        return True

    def make_button(self, secret_key):
        """🎛️ Create a button for a secret, disabling it if it's currently selected."""
        label = map_label(secret_key)

        button = Button(
            label=label,
            style=discord.ButtonStyle.secondary,
            custom_id=f"secret_{secret_key}",
            disabled=(secret_key == self.current_secret),  # disable currently selected
        )

        async def callback(interaction: discord.Interaction):
            try:
                self.current_secret = secret_key
                self.clear_items()
                for sk in self.secrets.keys():
                    self.add_item(self.make_button(sk))

                # Rebuild the embed for the newly selected secret
                embed = await build_sd_secret_embed(
                    self.sd_helper, self.map_key, self.current_secret
                )

                await interaction.response.edit_message(embed=embed, view=self)
            except Exception:
                await interaction.response.send_message(
                    "An error occurred while switching secrets. Please try again later.",
                    ephemeral=True,
                )

        button.callback = callback
        return button
