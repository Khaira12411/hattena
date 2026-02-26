import logging

import discord
from discord.ui import Button, View
from straydex.functions.main import (
    remove_line_from_desc,
    send_sd_logs,
    get_default_footer,
)
from utils.logs.pretty_log import pretty_log
from straydex.desc.patreon import SD_PAT_DICT
async def build_sd_patreon_embed(
    guild: discord.Guild,
    user_display_name: str,
    patreon: str,
    user_id: int,
):

    desc = SD_PAT_DICT[patreon]["desc"]
    emoji = SD_PAT_DICT[patreon]["emoji"]
    color = SD_PAT_DICT[patreon]["color"]
    thumbnail = SD_PAT_DICT[patreon]["thumbnail"]

    embed = discord.Embed(description=desc, color=color)
    embed.set_author(name="STRAYDEX")
    embed.set_thumbnail(url=thumbnail)
    footer_text = get_default_footer(user_display_name)
    embed.set_footer(text=footer_text, icon_url=guild.icon.url)

    return embed


async def build_sd_main_patreon_embed(
    guild: discord.Guild,
    user_display_name: str,
    patreon: str,
    user_id: int,
):
    embed = await build_sd_patreon_embed(
        guild=guild,
        user_display_name=user_display_name,
        patreon=patreon,
        user_id=user_id,
    )
    view = PatreonRarityView(
        guild=guild,
        user_display_name=user_display_name,
        patreon_dict=SD_PAT_DICT,
        current_rarity="COMMON",
        user_id=user_id,
    )
    return embed, view, None


class PatreonRarityView(View):
    def __init__(
        self, guild, user_display_name, patreon_dict, user_id, current_rarity="COMMON"
    ):
        super().__init__(timeout=None)  # persistent view 🌸
        self.guild = guild
        self.user_display_name = user_display_name
        self.patreon_dict = patreon_dict
        self.current_rarity = current_rarity
        self.user_id = user_id

        # [💜 INIT] Build all rarity buttons dynamically from SD_PAT_DICT
        pretty_log(
            "view",
            f"Initializing PatreonRarityView for {user_display_name} (Current rarity: {current_rarity})",

        )

        for rarity in self.patreon_dict.keys():
            self.add_item(self.make_button(rarity))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        """Ensure only the intended user can interact with these buttons."""
        if interaction.user.id != self.user_id:
            try:
                await interaction.response.send_message(
                    "This button isn't for you! 💢", ephemeral=True
                )
                # [🤍 DENY] User attempted to press another’s button
                pretty_log(
                    "warn",
                    f"{interaction.user} tried to press {self.user_display_name}'s Patreon rarity button",

                )
            except Exception as e:
                pretty_log(
                    "error",
                    f"Failed to send ephemeral message in interaction_check: {e}",

                )
            return False
        return True

    def make_button(self, rarity):
        """Create a rarity selection button with proper emoji & state."""
        button = Button(
            emoji=self.patreon_dict[rarity]["emoji"],
            style=discord.ButtonStyle.secondary,
            custom_id=f"patreon_rarity_{rarity}",
            disabled=(rarity == self.current_rarity),  # Disable if already selected
        )

        async def callback(interaction: discord.Interaction):
            try:
                # [💙 CHANGE] User switched their Patreon rarity
                pretty_log(
                    "event",
                    f"{interaction.user} switched rarity to {rarity}",

                )

                self.current_rarity = rarity
                embed = await build_sd_patreon_embed(
                    self.guild, self.user_display_name, rarity, self.user_id
                )

                # Rebuild the buttons so the correct one is disabled
                self.clear_items()
                for r in self.patreon_dict.keys():
                    self.add_item(self.make_button(r))

                await interaction.response.edit_message(embed=embed, view=self)

            except Exception as e:
                pretty_log(
                    "error",
                    f"Error in PatreonRarityView button callback for {rarity}: {e}",

                )
                # Try to notify the user about the error nicely
                try:
                    await interaction.response.send_message(
                        "An error occurred while switching rarity. Please try again later.",
                        ephemeral=True,
                    )
                except Exception:
                    pass  # ignore further errors

        button.callback = callback
        return button
