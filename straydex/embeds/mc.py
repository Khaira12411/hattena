# from utils.visuals.straydex.sd_mc_embed

import logging

import discord
from discord.ui import Button, View

from constants.aesthetic import Dividers
from straydex.config import SD_CONFIG
from straydex.desc.mc import *
from straydex.functions.main import (
    get_default_footer,
)

from utils.logs.debug_log import debug_enabled, debug_log, enable_debug
from utils.logs.pretty_log import pretty_log

"""enable_debug(f"{__name__}.build_sd_reg_mc_embed")
enable_debug(f"{__name__}.build_sd_golden_mc_embed")
enable_debug(f"{__name__}.build_sd_main_mc_embed")"""
logger = logging.getLogger(__name__)
# dex_number = int(getattr(WB_RegDex, boss_name)) + 1


async def build_sd_reg_mc_embed(
    guild: discord.Guild,
    user_id: str,
    sub_cmd: str,
    thumbnail_url: str,
    header_icon_url: str,
    whole_name: str,
    user_display_name: str,
):
    shrt_boss_name = sub_cmd
    reg_strat = getattr(SD_MC_REG_STRAT, shrt_boss_name)
    dex_num = getattr(SD_MC_DEX_NUM, shrt_boss_name)
    legendary_names = [
        "dia",  # Diancie (mythical/legendary)
        "laa",  # Latias
        "lao",  # Latios
        "mmx",  # Mewtwo X
        "mmy",  # Mewtwo Y
        "ray",  # Rayquaza
    ]
    superrare_names = [
        "ala",  # Alakazam
        "blz",  # Blaziken
        "gar",  # Garchomp
        "gav",  # Gardevoir
        "gen",  # Gengar
        "sal",  # Salamence
        "met",  # Metagross
        "luc",  # Lucario
        "tyr",  # Tyranitar
        "bla",  # Blastoise
        "chx",  # Charizard X
        "chy",  # Charizard Y
        "aer",  # Aerodactyl
        "ven",  # Venusaur
        "gal",  # Gallade
        "her",  # Heracross
        "sce",  # Sceptile
        "ste",  # Steelix
        "abs",  # Absol
        "swa",  # Swampert
        "dra",  # Dragonite
    ]
    rare_names = [
        "gya",  # Gyarados
        "abo",  # Abomasnow
        "alt",  # Altaria
        "amp",  # Ampharos
        "aud",  # Audino
        "ban",  # Banette
        "bee",  # Beedrill
        "cam",  # Camerupt
        "hou",  # Houndoom
        "kan",  # Kangaskhan
        "lop",  # Lopunny
        "man",  # Manectric
        "maw",  # Mawile
        "med",  # Medicham
        "pid",  # Pidgeot
        "pin",  # Pinsir
        "sci",  # Scizor
        "sha",  # Sharpedo
        "slo",  # Slowbro
        "vic",  # Victreebel
    ]

    rare_color = 16550924
    supperare_color = 16571396
    legendary_color = 10487800
    if shrt_boss_name in legendary_names:
        color = legendary_color
    elif shrt_boss_name in superrare_names:
        color = supperare_color
    else:
        color = rare_color

    mc_id = getattr(SD_MC_ID, shrt_boss_name, "N/A")
    npc_ids = getattr(SD_MC_NPC_IDS, shrt_boss_name, "N/A")
    top_line = f"**MC ID:** `{mc_id}`\n**NPC IDS:** `{npc_ids}`\n\n"
    desc = top_line + reg_strat
    embed = discord.Embed(description=desc, color=color)
    upper_name = whole_name.upper()
    header_name = f"MEGA {upper_name} #{dex_num}"

    embed.set_author(name=header_name, icon_url=header_icon_url)
    embed.set_thumbnail(url=thumbnail_url)
    embed.set_image(url=Dividers.SD_Alternate)
    footer_text = get_default_footer(user_display_name)

    embed.set_footer(text=footer_text, icon_url=guild.icon.url if guild.icon else None)

    return embed


async def build_sd_golden_mc_embed(
    guild: discord.Guild,
    user_id: str,
    sub_cmd: str,
    header_icon: str,
    whole_name: str,
    user_display_name: str,
):

    debug_log(
        f"build_sd_golden_mc_embed called with sub_cmd={sub_cmd}, user_id={user_id}, whole_name={whole_name}"
    )
    try:
        shrt_boss_name = sub_cmd
        strat = getattr(SD_MC_GOLD_STRAT, shrt_boss_name)
        debug_log(f"Fetched strat for {shrt_boss_name}: {strat}")
        dex_num = int(getattr(SD_MC_DEX_NUM, shrt_boss_name))
        golden_thumbnail = getattr(SD_MC_GOLD_THUMBNAIL, shrt_boss_name)
        golden_dex_num = dex_num + 2
        mc_id = getattr(SD_MC_ID, shrt_boss_name, "N/A")
        npc_ids = getattr(SD_MC_NPC_IDS, shrt_boss_name, "N/A")
        top_line = f"**MC ID:** `{mc_id}`\n**NPC IDS:** `{npc_ids}`\n\n"
        desc = top_line + (strat if strat is not None else "## Not available yet!")
        golden_color = 0xFDDC2B
        upper_name = whole_name.upper()
        header_name = f"GOLDEN MEGA {upper_name} #{golden_dex_num}"

        # Use default text if strat is None
        golden_strat = strat if strat is not None else "## Not available yet!"
        debug_log(f"golden_strat: {golden_strat}")

        # 🟦 Create embed
        try:
            embed = discord.Embed(description=desc, color=golden_color)
            debug_log(f"Embed created for {shrt_boss_name}")
            pretty_log(
                tag="info",
                label="🦭 MCStratView",
                message=f"💜 Embed created for {shrt_boss_name}",
            )
        except Exception as embed_err:
            debug_log(f"Failed to create embed: {embed_err}", highlight=True)
            pretty_log(
                tag="error",
                label="🦭 MCStratView",
                message=f"❌ Failed to create embed: {embed_err}",
            )
            raise embed_err

        # 🟦 Set author
        try:
            embed.set_author(name=header_name, icon_url=header_icon)
            debug_log(f"Set author for embed: {header_name}")
        except Exception as author_err:
            debug_log(f"Failed to set embed author: {author_err}", highlight=True)
            pretty_log(
                tag="error",
                label="🦭 MCStratView",
                message=f"❌ Failed to set embed author: {author_err}",
            )

        # 🟦 Set thumbnail if strat exists
        try:
            if strat is not None:
                embed.set_thumbnail(url=golden_thumbnail)
                debug_log(f"Set golden thumbnail: {golden_thumbnail}")
        except Exception as thumb_err:
            debug_log(f"Failed to set embed thumbnail: {thumb_err}", highlight=True)
            pretty_log(
                tag="error",
                label="🦭 MCStratView",
                message=f"❌ Failed to set embed thumbnail: {thumb_err}",
            )

        # 🟦 Set image and footer
        try:
            embed.set_image(url=Dividers.SD_Alternate)
            footer_text = get_default_footer(user_display_name)
            embed.set_footer(
                text=footer_text, icon_url=guild.icon.url if guild.icon else None
            )
            debug_log(f"Set image and footer for embed")
        except Exception as footer_err:
            debug_log(
                f"Failed to set embed image or footer: {footer_err}", highlight=True
            )
            pretty_log(
                tag="error",
                label="🦭 MCStratView",
                message=f"❌ Failed to set embed image or footer: {footer_err}",
            )

        return embed

    except Exception as e:
        debug_log(f"Unexpected error in build_sd_golden_mc_embed: {e}", highlight=True)
        pretty_log(
            tag="error",
            label="🦭 MCStratView",
            message=f"❌ Unexpected error in build_sd_golden_mc_embed: {e}",
        )
        return discord.Embed(description="Error building embed!", color=0xFF0000)


async def build_sd_main_mc_embed(
    guild: discord.Guild,
    user_id: str,
    sub_cmd: str,
    user_display_name: str,
):

    shrt_boss_name = sub_cmd
    whole_name = getattr(SD_MC_WHOLE_NAME, shrt_boss_name)
    golden_strat = getattr(SD_MC_GOLD_STRAT, shrt_boss_name)
    content = f"# STRAYDEX MEGA CHAMBER"
    thumbnail_url = (
        f"https://play.pokemonshowdown.com/sprites/xyani/{whole_name}-mega.gif"
    )
    header_icon_url = f"https://raw.githubusercontent.com/msikma/pokesprite/master/icons/pokemon/regular/{whole_name}-mega.png"

    # Always build reg_embed first
    reg_embed = await build_sd_reg_mc_embed(
        guild=guild,
        user_id=user_id,
        sub_cmd=sub_cmd,
        thumbnail_url=thumbnail_url,
        header_icon_url=header_icon_url,
        whole_name=whole_name,
        user_display_name=user_display_name,
    )

    # Handle special forms
    special_pokenames = ["mmx", "mmy", "chx", "chy"]
    if shrt_boss_name in special_pokenames:
        if shrt_boss_name in ["mmx", "chx"]:
            letter = "x"
        else:
            letter = "y"

        thumbnail_url = f"https://play.pokemonshowdown.com/sprites/xyani/{whole_name}-mega{letter}.gif"
        header_icon_url = f"https://raw.githubusercontent.com/msikma/pokesprite/master/icons/pokemon/regular/{whole_name}-mega-{letter}.png"

        # Rebuild reg_embed with the special form URLs
        reg_embed = await build_sd_reg_mc_embed(
            guild=guild,
            user_id=user_id,
            sub_cmd=sub_cmd,
            thumbnail_url=thumbnail_url,
            header_icon_url=header_icon_url,
            whole_name=whole_name,
            user_display_name=user_display_name,
        )

    if golden_strat is None:
        return reg_embed, content
    else:
        view = MCStrat(
            guild=guild,
            user_id=user_id,
            sub_cmd=sub_cmd,
            thumbnail_url=thumbnail_url,
            header_icon_url=header_icon_url,
            whole_name=whole_name,
            user_display_name=user_display_name,
        )
        return reg_embed, view, content


class MCStrat(View):

    def __init__(
        self,
        guild,
        user_id,
        sub_cmd,
        thumbnail_url,
        header_icon_url,
        whole_name,
        user_display_name,
    ):
        super().__init__(timeout=120)  # 🟦 2 minutes timeout
        self.guild = guild
        self.user_id = user_id
        self.sub_cmd = sub_cmd
        self.thumbnail_url = thumbnail_url
        self.header_icon_url = header_icon_url
        self.whole_name = whole_name
        self.user_display_name = user_display_name

        # 🟦 Start with Regular button disabled, Golden enabled
        self.regular.disabled = True
        self.golden.disabled = False
        # 🟦 Set emoji for Golden button dynamically
        golden_emoji = getattr(MC_GOLD_BUTTON_EMOJI, self.sub_cmd, None)
        if golden_emoji:
            self.golden.emoji = golden_emoji
        # Set for regular button dynamically if needed
        regular_emoji = getattr(MC_REGULAR_BUTTON_EMOJI, self.sub_cmd, None)
        if regular_emoji:
            self.regular.emoji = regular_emoji

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        # 🟦 Check if the user is allowed to press this button
        if interaction.user.id != self.user_id:
            try:
                await interaction.response.send_message(
                    "This button isn't for you!", ephemeral=True
                )
                # 📘 Pretty log for unauthorized click
                pretty_log(
                    tag="info",
                    label="🦭 MC Strat View",
                    message=f"💙 Unauthorized button press by {interaction.user} (ID: {interaction.user.id})",
                )
            except Exception as e:
                # 📕 Pretty log for ephemeral send failure
                pretty_log(
                    tag="error",
                    label="🦭 MC Strat View",
                    message=f"❌ Failed to send ephemeral in interaction_check: {e}",
                )
            return False
        return True

    @discord.ui.button(label="Regular", style=discord.ButtonStyle.secondary)
    async def regular(self, interaction: discord.Interaction, button: Button):
        # 📘 Pretty log for button press
        pretty_log(
            tag="info",
            label="🦭 MC Strat View",
            message=f"💙 Regular button pressed by {interaction.user} (ID: {interaction.user.id})",
        )
        try:
            embed = await build_sd_reg_mc_embed(
                guild=self.guild,
                user_id=self.user_id,
                sub_cmd=self.sub_cmd,
                thumbnail_url=self.thumbnail_url,
                header_icon_url=self.header_icon_url,
                whole_name=self.whole_name,
                user_display_name=self.user_display_name,
            )
            # 🟦 Update buttons: Regular disabled, Golden enabled
            button.disabled = True
            self.golden.disabled = False

            await interaction.response.edit_message(embed=embed, view=self)
            # 📘 Pretty log for successful update
            pretty_log(
                tag="info",
                label="🦭 MC Strat View",
                message=f"💜 Successfully updated embed for Regular button",
            )

        except Exception as e:
            # 📕 Pretty log for callback error
            pretty_log(
                tag="error",
                label="🦭 MC Strat View",
                message=f"❌ Error in Regular button callback: {e}",
            )
            try:
                await interaction.response.send_message(
                    "Something went wrong while processing your request.",
                    ephemeral=True,
                )
                # 📘 Pretty log for ephemeral error sent
                pretty_log(
                    tag="error",
                    label="🦭 MC Strat View",
                    message=f"💙 Ephemeral error message sent to {interaction.user} (ID: {interaction.user.id})",
                )
            except Exception as send_err:
                # 📕 Pretty log for failure sending ephemeral
                pretty_log(
                    tag="error",
                    label="🦭 MC Strat View",
                    message=f"❌ Failed to send ephemeral error in Regular button: {send_err}",
                )

    #

    @discord.ui.button(label="Golden", style=discord.ButtonStyle.secondary)
    async def golden(self, interaction: discord.Interaction, button: Button):
        # 📘 Pretty log: button pressed
        pretty_log(
            tag="info",
            label="🦭 MCStratView",
            message=f"💜 Golden button pressed by {interaction.user} (ID: {interaction.user.id})",
        )

        try:
            # 🟦 Build golden embed
            embed = await build_sd_golden_mc_embed(
                guild=self.guild,
                user_id=self.user_id,
                sub_cmd=self.sub_cmd,
                header_icon=self.header_icon_url,
                whole_name=self.whole_name,
                user_display_name=self.user_display_name,
            )
            pretty_log(
                tag="info",
                label="🦭 MCStratView",
                message="💜 Successfully built golden embed",
            )

            # 🟦 Update buttons
            button.disabled = True
            self.regular.disabled = False

            # 🟦 Try editing message with new embed
            try:
                await interaction.response.edit_message(embed=embed, view=self)
                pretty_log(
                    tag="info",
                    label="🦭 MCStratView",
                    message="💙 Successfully updated message with golden embed",
                )
            except Exception as edit_err:
                pretty_log(
                    tag="error",
                    label="🦭 MCStratView",
                    message=f"❌ Failed to edit message: {edit_err}",
                )
                # Use followup as fallback
                await interaction.followup.send(
                    "Failed to update the message with golden embed.",
                    ephemeral=True,
                )

        except Exception as e:
            # 📕 Outer callback error
            pretty_log(
                tag="error",
                label="🦭 MCStratView",
                message=f"❌ Error in Golden button callback: {e}",
            )
            # 🟦 Try sending ephemeral fallback
            try:
                await interaction.followup.send(
                    "Something went wrong while processing your request.",
                    ephemeral=True,
                )
                pretty_log(
                    tag="error",
                    label="🦭 MCStratView",
                    message=f"💜 Ephemeral error sent to {interaction.user} (ID: {interaction.user.id})",
                )
            except Exception as send_err:
                pretty_log(
                    tag="error",
                    label="🦭 MCStratView",
                    message=f"❌ Failed to send ephemeral error: {send_err}",
                )

    async def on_timeout(self):
        try:
            # 🟦 Disable all buttons after timeout
            for child in self.children:
                child.disabled = True
            # 📘 Pretty log for timeout
            pretty_log(
                tag="info",
                label="🦭 MC Strat View",
                message=f"💤 Buttons disabled due to timeout",
            )
            # 🟦 To edit the message after timeout, store self.message when sending
            # await self.message.edit(view=self)
        except Exception as e:
            # 📕 Pretty log for timeout edit error
            pretty_log(
                tag="error",
                label="🦭 MC Strat View",
                message=f"❌ Error during on_timeout editing message: {e}",
            )
