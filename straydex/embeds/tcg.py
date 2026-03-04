import logging

import discord
from discord.ui import Button, View

from constants.aesthetic import Dividers, Emojis
from straydex.config import SD_CONFIG
from straydex.functions.main import get_default_footer
from utils.logs.pretty_log import pretty_log
from straydex.desc import TCG_DESC, TCG_EMOJIS, SD_MAIN_IMAGES

# ❀───────────────────────────────❀
#       💖  TCG Embeds  💖
# ❀───────────────────────────────❀
async def build_sd_tcg_main_info_embed(
    guild: discord.Guild,
    user_display_name: str,
    user_id: int,
):
    info_embed = build_sd_tcg_info_embed(guild, user_display_name, "info")
    commands_embed = build_sd_tcg_info_embed(guild, user_display_name, "commands")
    items_embed = build_sd_tcg_info_embed(guild, user_display_name, "items")
    quality_embed = build_sd_tcg_info_embed(guild, user_display_name, "quality_conditions")
    trading_embed = build_sd_tcg_info_embed(guild, user_display_name, "trading")
    market_embed = build_sd_tcg_info_embed(guild, user_display_name, "market")

    try:
        view = TCGInfoView(
            guild,
            user_id,
            info_embed,
            commands_embed,
            items_embed,
            quality_embed,
            trading_embed,
            market_embed,
        )
        return info_embed, view, None
    except Exception as e:
        pretty_log(
            tag="error",
            message=f"Error building TCG main info embed: {e}",
            include_trace=True,
        )
        fallback_embed = discord.Embed(
            title="TCG Info",
            description="An error occurred while loading the TCG information. Please try again later.",
            color=SD_CONFIG.error_color,
        )
        return fallback_embed, None, None

def build_sd_tcg_info_embed(guild: discord.Guild, user_display_name: str, sub: str):
    desc = getattr(TCG_DESC, sub)
    embed = discord.Embed(description=desc, color=SD_CONFIG.default_color)
    footer_text = get_default_footer(user_display_name)

    icon_url = guild.icon.url if guild.icon else None
    embed.set_footer(text=footer_text, icon_url=icon_url)
    image_url = Dividers.SD_Alternate
    if sub == "info":
        image_url = SD_MAIN_IMAGES.TCG

    embed.set_image(url=image_url)
    embed.set_author(name="STRAYDEX",)
    return embed


class TCGInfoView(View):
    def __init__(
        self,
        guild: discord.Guild,
        user_id: int,
        info_embed: discord.Embed,
        commands_embed: discord.Embed,
        items_embed: discord.Embed,
        quality_embed: discord.Embed,
        trading_embed: discord.Embed,
        market_embed: discord.Embed,
    ):
        super().__init__()
        self.guild = guild
        self.user_id = user_id
        self.info_embed = info_embed
        self.commands_embed = commands_embed
        self.items_embed = items_embed
        self.quality_embed = quality_embed
        self.trading_embed = trading_embed
        self.market_embed = market_embed
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
            elif embed_name == "commands":
                embed = self.commands_embed
            elif embed_name == "items":
                embed = self.items_embed
            elif embed_name == "quality_conditions":
                embed = self.quality_embed
            elif embed_name == "trading":
                embed = self.trading_embed
            elif embed_name == "market":
                embed = self.market_embed
            else:
                return

            self.current_embed = embed_name
            self.update_button_states()
            pretty_log(
                tag="info",
                message=f"[TCG INFO VIEW] {interaction.user} switched to {embed_name.upper()}",
            )
            await interaction.response.edit_message(embed=embed, view=self)
        except Exception as e:
            pretty_log(
                tag="error",
                message=f"Error in TCGInfoView.switch_embed: {e}",
                include_trace=True,
            )
            await interaction.response.send_message(
                "⚠️ An error occurred while switching embeds. Please try again later.",
                ephemeral=True,
            )

    # ───────────── Buttons ─────────────
    @discord.ui.button(
        label="Info",
        style=discord.ButtonStyle.secondary,
        custom_id="info",
        emoji=TCG_EMOJIS.info,
        row=0,
    )
    async def info_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "info")

    @discord.ui.button(
        label="Commands",
        style=discord.ButtonStyle.secondary,
        custom_id="commands",
        emoji=TCG_EMOJIS.commands,
        row=0,
    )
    async def commands_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "commands")

    @discord.ui.button(
        label="Quality/Conditions",
        style=discord.ButtonStyle.secondary,
        custom_id="quality_conditions",
        emoji=TCG_EMOJIS.quality_conditions,
        row=0,
    )
    async def quality_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "quality_conditions")

    @discord.ui.button(
        label="Items",
        style=discord.ButtonStyle.secondary,
        custom_id="items",
        emoji=TCG_EMOJIS.items,
        row=1,
    )
    async def items_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "items")

    @discord.ui.button(
        label="Trading",
        style=discord.ButtonStyle.secondary,
        custom_id="trading",
        emoji=TCG_EMOJIS.trading,
        row=1,
    )
    async def trading_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "trading")

    @discord.ui.button(
        label="Market",
        style=discord.ButtonStyle.secondary,
        custom_id="market",
        emoji=TCG_EMOJIS.market,
        row=1,
    )
    async def market_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "market")
