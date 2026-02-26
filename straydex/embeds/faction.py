import discord
from discord.ui import Button, View
from straydex.desc import get_faction_value_dynamic
from straydex.config import SD_CONFIG
from utils.logs.pretty_log import pretty_log
from straydex.functions.main import (
    remove_line_from_desc,
    send_sd_logs,
    get_default_footer,
)

def get_main_faction(variation_key: str) -> str:
    """
    Extract the main faction from a variation key.
    how to use:
    print(get_main_faction("aq2"))  # "aq"

    Examples:
    - "aq2" -> "aq"
    - "fl3" -> "fl"
    - "ga"  -> "ga"
    """
    # Remove trailing digits
    return variation_key.rstrip("0123456789")


async def build_sd_fa_embed(
    guild: discord.Guild,
    user_id: str,
    sub_cmd: str,
    user_display_name: str,
):
    main_faction = get_main_faction(sub_cmd)

    # Default Variable per Faction
    color = get_faction_value_dynamic(main_faction=main_faction, category="color")
    thumbnail_url = get_faction_value_dynamic(
        main_faction=main_faction, category="thumbnail"
    )

    # Getting Description, header_text, header_icon
    desc = get_faction_value_dynamic(variation=sub_cmd, category="desc")
    header_text = get_faction_value_dynamic(variation=sub_cmd, category="header_text")
    header_icon = get_faction_value_dynamic(variation=sub_cmd, category="header_icon")

    # Conditions for footer , and footer icon
    faction_footer_text = get_faction_value_dynamic(
        variation=sub_cmd, category="footer_text"
    )
    faction_footer_icon = get_faction_value_dynamic(
        variation=sub_cmd, category="footer_icon"
    )

    if faction_footer_icon:
        footer_icon = faction_footer_icon
        footer_text = faction_footer_text
    else:
        footer_text = get_default_footer(user_display_name)
        footer_icon = guild.icon.url

    # Building Embed
    embed = discord.Embed(description=desc, color=color)
    embed.set_author(name=header_text, icon_url=header_icon)
    embed.set_thumbnail(url=thumbnail_url)
    embed.set_footer(text=footer_text, icon_url=footer_icon)

    return embed


async def build_sd_main_fa_embed(
    guild: discord.Guild,
    user_id: str,
    sub_cmd: str,
    user_display_name: str,
):
    content = get_faction_value_dynamic(variation=sub_cmd, category="content")
    embed = await build_sd_fa_embed(
        guild=guild,
        user_id=user_id,
        sub_cmd=sub_cmd,
        user_display_name=user_display_name,
    )

    view = SDFactionView(guild=guild, sub_cmd=sub_cmd, user_id=user_id)
    return embed, view, content


class SDFactionView(View):
    def __init__(self, guild: discord.Guild, sub_cmd: str, user_id: int):
        super().__init__(timeout=None)
        self.guild = guild
        self.sub_cmd = sub_cmd
        self.user_id = user_id

        #
        try:
            # 💙 Determine main faction (strips trailing numbers)
            main_faction = get_main_faction(sub_cmd)
            FACTIONS_VARIANTS = [
                "aq",
                "aq2",
                "aq3",
                "fl",
                "fl2",
                "fl3",
                "ga",
                "ga2",
                "ga3",
                "ga4",
                "ma",
                "ma2",
                "ma3",
                "pl",
                "pl2",
                "pl3",
                "sk",
                "sk2",
                "sk3",
                "ye",
                "ye2",
                "ye3",
                "ro",
                "ro2",
                "ro3",
                "ro4",
            ]

            # 💙 Get all variant keys for this faction, sorted so base comes first
            self.variant_keys = sorted(
                [k for k in FACTIONS_VARIANTS if k.startswith(main_faction)],
                key=lambda k: (len(k), k),
            )

            # 💙 Add buttons for each variant safely
            for idx, key in enumerate(self.variant_keys):

                # ✅ Fetch label, default to "Unknown" if missing
                label = (
                    get_faction_value_dynamic(variation=key, category="button_label")
                    or "Unknown"
                )

                # ✅ Fetch emoji, default to ❔ if missing
                emoji = (
                    get_faction_value_dynamic(variation=key, category="button_emoji")
                    or "❔"
                )

                # 💙 Create and add button
                button = Button(
                    label=label,
                    emoji=emoji,
                    style=discord.ButtonStyle.primary,
                    custom_id=key,
                    disabled=(idx == 0),  # disable first button initially
                )
                button.callback = self.make_callback(key)
                self.add_item(button)

        except Exception as e:
            pretty_log(
                message=f"🔥 Error initializing SDFactionView for '{sub_cmd}': {e}",

            )

    def make_callback(self, key: str):
        async def callback(interaction: discord.Interaction):
            # 🔒 Restrict to command user only
            if interaction.user.id != self.user_id:
                await interaction.response.send_message(
                    "❌ This isn't your button!",
                    ephemeral=True,
                )
                return

            try:
                # 💙 Build faction embed dynamically
                embed = await build_sd_fa_embed(
                    guild=self.guild,
                    user_id=self.user_id,
                    sub_cmd=key,
                    user_display_name=interaction.user.display_name,
                )

                # 💙 Update button states dynamically
                for item in self.children:
                    if isinstance(item, Button):
                        item.disabled = item.custom_id == key

                await interaction.response.edit_message(embed=embed, view=self)

            except Exception as e:
                pretty_log(
                    message=f"🔥 Error updating faction view for '{key}': {e}",

                )
                await interaction.response.send_message(
                    "⚠️ Something went wrong while updating the faction.",
                    ephemeral=True,
                )

        return callback
