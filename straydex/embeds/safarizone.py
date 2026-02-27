import logging

import discord
from discord.ui import Button, View

from constants.aesthetic import Dividers, Emojis
from straydex.config import SD_CONFIG
from straydex.desc.safarizone import SZ_DESC, SZ_Images
from straydex.functions.main import get_default_footer
from utils.logs.pretty_log import pretty_log

logger = logging.getLogger(__name__)
SAFARI_COLOR = 0x839705  # Green color for Safari Zone embeds

# ❀───────────────────────────────❀
#       💖  Safari Zone Embeds  💖
# ❀───────────────────────────────❀
# For !szi and szpe
async def build_sd_sz_main_info_embed(
    guild: discord.Guild,
    user_display_name: str,
    user_id: int,
):
    info_embed = build_sd_sub_info_embed(guild, user_display_name, "i")
    perks_embed = build_sd_sub_info_embed(guild, user_display_name, "pe")

    try:
        view = SafariZoneInfoView(guild, user_id, info_embed, perks_embed)
        return info_embed, view, None
    except Exception as e:
        pretty_log(
            tag="error",
            message=f"Error building Safari Zone main info embed: {e}",
            include_trace=True,
        )
        fallback_embed = discord.Embed(
            title="Safari Zone Info",
            description="An error occurred while loading the Safari Zone information. Please try again later.",
            color=SD_CONFIG.error_color,
        )
        return fallback_embed, None, None


def build_sd_sub_info_embed(guild: discord.Guild, user_display_name: str, sub: str):
    desc = getattr(SZ_DESC, sub)

    embed = discord.Embed(description=desc, color=SD_CONFIG.default_color)
    footer_text = get_default_footer(user_display_name)

    icon_url = guild.icon.url if guild.icon else None
    embed.set_footer(text=footer_text, icon_url=icon_url)

    embed.set_image(url=Dividers.SD_Alternate)
    embed.set_author(name="STRAYDEX", icon_url=SZ_Images.safari_zone_author_icon)
    return embed


class SafariZoneInfoView(View):
    def __init__(
        self,
        guild: discord.Guild,
        user_id: int,
        info_embed: discord.Embed,
        perks_embed: discord.Embed,
    ):
        super().__init__(timeout=300)
        self.guild = guild
        self.user_id = user_id
        self.info_embed = info_embed
        self.perks_embed = perks_embed
        self.current_embed = "info"

        self.update_button_states()

    def update_button_states(self):
        for child in self.children:
            if isinstance(child, Button):
                child.disabled = child.custom_id == self.current_embed

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.user_id:
            await interaction.response.send_message(
                "⚠️ Only the original requester can use these buttons.",
                ephemeral=True,
            )
            return False
        return True

    async def switch_embed(self, interaction: discord.Interaction, embed_name: str):
        try:
            if embed_name == "info":
                embed = self.info_embed
            elif embed_name == "perks":
                embed = self.perks_embed
            else:
                return

            self.current_embed = embed_name
            self.update_button_states()

            pretty_log(
                tag="info",
                message=f"[SZ VIEW] {interaction.user} switched to {embed_name.upper()}",
            )

            await interaction.response.edit_message(embed=embed, view=self)

        except Exception as e:
            pretty_log(
                tag="error",
                message=f"Error switching Safari Zone embed: {e}",
                include_trace=True,
            )
            await interaction.response.send_message(
                "❌ An error occurred while switching embeds. Please try again later.",
                ephemeral=True,
            )

    # ───────────── Buttons ─────────────
    @discord.ui.button(
        label="Info", style=discord.ButtonStyle.primary, custom_id="info"
    )
    async def info_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "info")

    @discord.ui.button(
        label="Perks", style=discord.ButtonStyle.secondary, custom_id="perks"
    )
    async def perks_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "perks")


# For !szse
async def build_sd_sz_secrets_main_embed(
    guild: discord.Guild,
    user_display_name: str,
    user_id: int,
):
    se1_embed = build_sd_sub_secret_embed(guild, user_display_name, "se1")
    se2_embed = build_sd_sub_secret_embed(guild, user_display_name, "se2")
    se3_embed = build_sd_sub_secret_embed(guild, user_display_name, "se3")
    se4_embed = build_sd_sub_secret_embed(guild, user_display_name, "se4")

    try:
        view = SafariZoneSecretsView(
            guild, user_id, se1_embed, se2_embed, se3_embed, se4_embed
        )
        return se1_embed, view, None
    except Exception as e:
        pretty_log(
            tag="error",
            message=f"Error building Safari Zone secrets main embed: {e}",
            include_trace=True,
        )
        fallback_embed = discord.Embed(
            title="Safari Zone Secrets",
            description="An error occurred while loading the Safari Zone secrets. Please try again later.",
            color=SD_CONFIG.error_color,
        )
        return fallback_embed, None, None


def build_sd_sub_secret_embed(guild: discord.Guild, user_display_name: str, sub: str):
    desc = getattr(SZ_DESC, sub)
    image_url = getattr(SZ_Images, sub)

    embed = discord.Embed(description=desc, color=SAFARI_COLOR)
    footer_text = get_default_footer(user_display_name)

    icon_url = guild.icon.url if guild.icon else None
    embed.set_footer(text=footer_text, icon_url=icon_url)

    embed.set_image(url=Dividers.SD_Alternate)
    embed.set_author(name="STRAYDEX", icon_url=SZ_Images.safari_zone_author_icon)
    embed.set_image(url=image_url)
    return embed

class SafariZoneSecretsView(View):
    def __init__(
        self,
        guild: discord.Guild,
        user_id: int,
        se1_embed: discord.Embed,
        se2_embed: discord.Embed,
        se3_embed: discord.Embed,
        se4_embed: discord.Embed,
    ):
        super().__init__(timeout=300)
        self.guild = guild
        self.user_id = user_id
        self.se1_embed = se1_embed
        self.se2_embed = se2_embed
        self.se3_embed = se3_embed
        self.se4_embed = se4_embed
        self.current_embed = "se1"

        self.update_button_states()
    def update_button_states(self):
        for child in self.children:
            if isinstance(child, Button):
                child.disabled = child.custom_id == self.current_embed

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.user_id:
            await interaction.response.send_message(
                "⚠️ Only the original requester can use these buttons.",
                ephemeral=True,
            )
            return False
        return True

    async def switch_embed(self, interaction: discord.Interaction, embed_name: str):
        try:
            if embed_name == "se1":
                embed = self.se1_embed
            elif embed_name == "se2":
                embed = self.se2_embed
            elif embed_name == "se3":
                embed = self.se3_embed
            elif embed_name == "se4":
                embed = self.se4_embed
            else:
                return

            self.current_embed = embed_name
            self.update_button_states()

            pretty_log(
                tag="info",
                message=f"[SZ SECRETS VIEW] {interaction.user} switched to {embed_name.upper()}",
            )

            await interaction.response.edit_message(embed=embed, view=self)

        except Exception as e:
            pretty_log(
                tag="error",
                message=f"Error switching Safari Zone secrets embed: {e}",
                include_trace=True,
            )
            await interaction.response.send_message(
                "❌ An error occurred while switching embeds. Please try again later.",
                ephemeral=True,
            )
    # ───────────── Buttons ─────────────
    @discord.ui.button(
        label="Secret 1", style=discord.ButtonStyle.secondary, custom_id="se1"
    )
    async def se1_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "se1")
    @discord.ui.button(
        label="Secret 2", style=discord.ButtonStyle.secondary, custom_id="se2"
    )
    async def se2_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "se2")
    @discord.ui.button(
        label="Secret 3", style=discord.ButtonStyle.secondary, custom_id="se3"
    )
    async def se3_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "se3")

    @discord.ui.button(
        label="Secret 4", style=discord.ButtonStyle.secondary, custom_id="se4"
    )
    async def se4_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "se4")
