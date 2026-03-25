import discord
from discord.ui import Button, View

from constants.aesthetic import *
from straydex.config import SD_CONFIG
from straydex.desc.battle_frontier import *
from straydex.functions.main import get_default_footer
from utils.logs.pretty_log import pretty_log

abbrv_map = {
    "pal": "palace",
    "are": "arena",
    "tow": "tower",
    "pik": "pike",
    "dom": "dome",
    "pyr": "pyramid",
}


async def build_sd_bf_main_info_embed(
    guild: discord.Guild, user_display_name: str, sub_cmd: str
):

    abbrv = abbrv_map.get(sub_cmd, sub_cmd)
    desc = getattr(BF_DESC, abbrv)
    author_image_url = getattr(BF_AUTHOR_IMAGE_URL, abbrv)
    thumbnail_url = getattr(BF_THUMBNAIL, abbrv)
    image_url = getattr(BF_IMAGE_URL, abbrv)
    embed = discord.Embed(description=desc, color=SD_CONFIG.default_color)
    footer_text = get_default_footer(user_display_name)
    icon_url = guild.icon.url if guild.icon else None
    embed.set_footer(text=footer_text, icon_url=icon_url)
    embed.set_image(url=image_url)
    embed.set_thumbnail(url=thumbnail_url)
    embed.set_author(name="STRAYDEX", icon_url=author_image_url)
    content = f" # STRAYDEX BATTLE FRONTIER"
    return embed, content


def build_sd_battle_pyramid_item_info_embed(
    guild: discord.Guild,
    user_display_name: str,
):
    items_abv = "pyramid_2"
    main_pyramid = "pyramid"
    desc = getattr(BF_DESC, items_abv)
    author_image_url = getattr(BF_AUTHOR_IMAGE_URL, main_pyramid)
    thumbnail_url = getattr(BF_THUMBNAIL, main_pyramid)
    image_url = getattr(BF_IMAGE_URL, main_pyramid)
    embed = discord.Embed(description=desc, color=SD_CONFIG.default_color)
    footer_text = get_default_footer(user_display_name)
    icon_url = guild.icon.url if guild.icon else None
    embed.set_footer(text=footer_text, icon_url=icon_url)
    embed.set_image(url=image_url)
    embed.set_thumbnail(url=thumbnail_url)
    embed.set_author(name="STRAYDEX", icon_url=author_image_url)
    content = f" # STRAYDEX BATTLE FRONTIER"
    return embed, content


async def build_sd_main_pyramid_info_embed(
    guild: discord.Guild, user_display_name: str, user_id: int, sub_cmd: str
):
    content = f" # STRAYDEX BATTLE FRONTIER"
    guide_embed, _ = await build_sd_bf_main_info_embed(guild, user_display_name, "pyr")
    items_embed, _ = build_sd_battle_pyramid_item_info_embed(guild, user_display_name)
    try:
        view = SD_PYRAMID(
            guild=guild,
            user_id=user_id,
            guide_embed=guide_embed,
            items_embed=items_embed,
        )
        return guide_embed, view, content
    except Exception as e:
        pretty_log(
            tag="error",
            message=f"Error building Battle Pyramid main embed: {e}",
            include_trace=True,
        )
        fallback_embed = discord.Embed(
            title="Battle Pyramid",
            description="An error occurred while loading the Battle Pyramid information. Please try again later.",
            color=SD_CONFIG.error_color,
        )
        return fallback_embed, None, content


class SD_PYRAMID(View):
    def __init__(
        self,
        guild: discord.Guild,
        user_id: int,
        guide_embed: discord.Embed,
        items_embed: discord.Embed,
    ):
        super().__init__(timeout=300)
        self.guild = guild
        self.user_id = user_id
        self.guide_embed = guide_embed
        self.items_embed = items_embed
        self.current_embed = "guide"

        self.update_button_states()

    def update_button_states(self):
        for child in self.children:
            if isinstance(child, Button):
                child.disabled = child.custom_id == self.current_embed

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.user_id:
            await interaction.response.send_message(
                "⚠️ Only the original user can use these buttons.",
                ephemeral=True,
            )
            return False
        return True

    async def switch_embed(self, interaction: discord.Interaction, embed_name: str):
        try:
            if embed_name == "guide":
                embed = self.guide_embed
            elif embed_name == "items":
                embed = self.items_embed
            else:
                return

            self.current_embed = embed_name
            self.update_button_states()
            await interaction.response.edit_message(embed=embed, view=self)
        except Exception as e:
            pretty_log(message=f"Error switching embed: {e}", tag="error")

    # ───────────── Buttons ─────────────
    @discord.ui.button(
        label="Guide",
        style=discord.ButtonStyle.secondary,
        custom_id="guide",
        emoji=Emojis.battle,
    )
    async def guide_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "guide")

    @discord.ui.button(
        label="Items",
        style=discord.ButtonStyle.secondary,
        custom_id="items",
        emoji=Emojis.purple_bag,
    )
    async def items_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "items")
