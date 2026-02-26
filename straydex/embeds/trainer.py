import logging

import discord
from discord.ui import Button, View

from constants.aesthetic import Dividers, Emojis
from straydex.config import SD_CONFIG
from straydex.desc import SD_TR_DESC
from straydex.functions.main import (
    get_default_footer,
    remove_line_from_desc,
    send_sd_logs,
)
from utils.logs.pretty_log import pretty_log

logger = logging.getLogger(__name__)


async def build_sd_main_trainer_embed(
    guild: discord.Guild,
    user_display_name: str,
    user_id: int,
):
    trl_embed = await build_sd_trl_embed(
        guild=guild,
        user_display_name=user_display_name,
        user_id=user_id,
    )
    tre_embed = await build_sd_tre_embed(
        guild=guild,
        user_display_name=user_display_name,
        user_id=user_id,
    )
    tref_embed = await build_sd_tref_embed(
        guild=guild,
        user_display_name=user_display_name,
        user_id=user_id,
    )
    view = TrainerInfoView(
        guild=guild,
        user_id=user_id,
        tref_embed=tref_embed,
        trl_embed=trl_embed,
        tre_embed=tre_embed,
    )
    return trl_embed, view, None


async def build_sd_tre_embed(
    guild: discord.Guild,
    user_display_name: str,
    user_id: int,
):
    desc = "# TRAINERS: EV ACCOUNTS"
    embed = discord.Embed(description=desc, color=SD_CONFIG.default_color)

    embed.add_field(name="💜 For HP", value=";b user 785324709871878154", inline=False)
    embed.add_field(name="💜 For ATT", value=";b user 869722020240293898", inline=False)
    embed.add_field(name="💜 For SPA", value=";b user 496199171330539530", inline=False)
    embed.add_field(name="💜 For DEF", value=";b user 763621487852519474", inline=False)
    embed.add_field(name="💜 For SPD", value=";b user 797773956546560041", inline=False)
    embed.add_field(name="💜 For SPE", value=";b user 383068074242211840", inline=False)

    embed.add_field(
        name=f"{Emojis.blue_sparkles} Battle NPC EV Yields (Gyms, Elite Four, Champions, and Basic, Boss, and Master Challenges) Made by Zoroark",
        value=f"{Emojis.blue_arrow} [Link here](https://docs.google.com/spreadsheets/d/1Z__y2kf0EXct2XUmCzcj6e6Fe_9lENQqLjPFbMs98aA/edit?usp=sharing)",
        inline=False,
    )

    footer_text = get_default_footer(user_display_name)
    embed.set_footer(text=footer_text, icon_url=guild.icon.url)
    embed.set_thumbnail(url=SD_CONFIG.default_thumbnail)
    embed.set_image(url=Dividers.SD_Alternate)
    embed.set_author(name="STRAYDEX")
    return embed


async def build_sd_trl_embed(
    guild: discord.Guild,
    user_display_name: str,
    user_id: int,
):
    desc = "# TRAINERS: TRAINING IDS"
    embed = discord.Embed(description=desc, color=SD_CONFIG.default_color)

    embed.add_field(
        name=f"{Emojis.blue_arrow}  For lvl 1 to 55",
        value=";b user 675725560470831125",
        inline=False,
    )
    embed.add_field(
        name=f"{Emojis.blue_arrow}  For lvl 56 to 100",
        value=";b user 508692505810698241",
        inline=False,
    )
    embed.add_field(
        name=f"{Emojis.blue_pawprint}  Recommended Mons and Moves",
        value=(f"> {Emojis.blue_star}  Marshadow + Close-Combat\n"),
        inline=False,
    )
    embed.add_field(
        name=f"{Emojis.blue_flower}  Instructions",
        value=(
            f"""__ Without EXP Share__
> - Let the pokemon that you are going to level up knock LVL 1 Chansey/ LVL 100 Blissey, using any physical or figthing move.
> - Switch to Marshadow then spam Close-Combat
__With EXP Share__
> - Using Marshadow/Slaking spam Close-Combat
__Remember to EV train your mons before leveling them up__"""
        ),
        inline=False,
    )

    embed.set_author(name="STRAYDEX")
    footer_text = get_default_footer(user_display_name)
    embed.set_footer(text=footer_text, icon_url=guild.icon.url)
    embed.set_thumbnail(url=SD_CONFIG.default_thumbnail)
    embed.set_image(url=Dividers.SD_Alternate)
    return embed


async def build_sd_tref_embed(
    guild: discord.Guild,
    user_display_name: str,
    user_id: int,
):
    desc = SD_TR_DESC.tref
    embed = discord.Embed(description=desc, color=SD_CONFIG.default_color)

    footer_text = get_default_footer(user_display_name)
    embed.set_footer(text=footer_text, icon_url=guild.icon.url)
    embed.set_thumbnail(url=SD_CONFIG.default_thumbnail)
    embed.set_image(url=Dividers.SD_Alternate)
    embed.set_author(name="STRAYDEX")
    return embed


# 🟦────────────────────────────────────────────
#       TrainerInfoView (Fixed)
# 🟦────────────────────────────────────────────


class TrainerInfoView(View):
    def __init__(self, guild, user_id, trl_embed, tre_embed, tref_embed):
        super().__init__(timeout=300)  # 5 min timeout
        self.guild = guild
        self.user_id = user_id
        self.trl_embed = trl_embed
        self.tre_embed = tre_embed
        self.tref_embed = tref_embed
        self.current_embed = "Levels"
        self.iphone_copy = (
            False  # False = Android (no backticks), True = iPhone (with backticks)
        )

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        """Restrict button presses to the original user."""
        if interaction.user.id != self.user_id:
            await interaction.response.send_message(
                "⚠️ Only the original requester can use these buttons.", ephemeral=True
            )
            return False
        return True

    #
    async def switch_embed(self, interaction: discord.Interaction, embed_name: str):
        """Handle switching embeds safely and update button states."""
        try:
            # Update button states first
            for child in self.children:
                if isinstance(child, Button):
                    if child.label == "Levels":
                        child.disabled = embed_name == "Levels"
                    elif child.label == "EV Training":
                        child.disabled = embed_name == "EV Training"
                    elif child.label == "EV Reset":
                        child.disabled = embed_name == "EV Reset"

            # Then edit the message with the new embed and updated buttons
            if embed_name == "Levels":
                await interaction.response.edit_message(embed=self.trl_embed, view=self)
            elif embed_name == "EV Training":
                await interaction.response.edit_message(embed=self.tre_embed, view=self)
            elif embed_name == "EV Reset":
                await interaction.response.edit_message(
                    embed=self.tref_embed, view=self
                )

            self.current_embed = embed_name

        except Exception as e:
            pretty_log("error", f"TrainerInfoView button error: {e}")
            try:
                await interaction.response.send_message(
                    "❌ An error occurred while switching tabs.", ephemeral=True
                )
            except:
                pass

    # ───────────── Buttons ─────────────
    @discord.ui.button(label="Levels", style=discord.ButtonStyle.primary, disabled=True)
    async def levels_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "Levels")

    @discord.ui.button(label="EV Training", style=discord.ButtonStyle.secondary)
    async def ev_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "EV Training")

    @discord.ui.button(label="EV Reset", style=discord.ButtonStyle.secondary)
    async def ev_reset_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "EV Reset")

    @discord.ui.button(label="Toggle Iphone Copy", style=discord.ButtonStyle.secondary)
    async def toggle_iphone_copy(
        self, interaction: discord.Interaction, button: Button
    ):
        # Toggle the copy mode
        self.iphone_copy = not self.iphone_copy
        # Update button label to reflect the NEXT toggle
        button.label = (
            "Toggle Android Copy" if self.iphone_copy else "Toggle Iphone Copy"
        )

        # Helper to add or remove backticks
        def toggle_backticks(text, add):
            if add:
                if not text.strip().startswith("`"):
                    return f"`{text.strip()}`"
                return text
            else:
                return text.replace("`", "")

        # Update trl_embed fields if current view is Levels
        if self.current_embed == "Levels":
            embed = self.trl_embed.copy()
            for i, field in enumerate(embed.fields):
                if "For lvl 1 to 55" in field.name or "For lvl 56 to 100" in field.name:
                    embed.set_field_at(
                        i,
                        name=field.name,
                        value=toggle_backticks(field.value, self.iphone_copy),
                        inline=field.inline,
                    )
            self.trl_embed = embed
            await interaction.response.edit_message(embed=self.trl_embed, view=self)
        # Update tre_embed fields if current view is EV Training
        elif self.current_embed == "EV Training":
            embed = self.tre_embed.copy()
            for i, field in enumerate(embed.fields):
                if field.name.startswith("💜 For"):
                    embed.set_field_at(
                        i,
                        name=field.name,
                        value=toggle_backticks(field.value, self.iphone_copy),
                        inline=field.inline,
                    )
            self.tre_embed = embed
            await interaction.response.edit_message(embed=self.tre_embed, view=self)
        else:
            await interaction.response.send_message(
                "Toggle only works for Levels or EV Training views.", ephemeral=True
            )
