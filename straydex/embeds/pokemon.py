import logging

import discord
from discord.ui import Button, View

from straydex.config import SD_CONFIG
from straydex.desc.pokemon import *
from straydex.functions.main import get_default_footer
from utils.logs.pretty_log import pretty_log
from utils.visuals.type_embed import build_weakness_embed_from_input

no_weakness_embed_list = [
    "deb",
    "nor",
    "set",
    "wor",
    "deb2",
    "nor2",
    "set2",
    "wor2",
    "nor3",
    "set3",
    "nor4",
    "arc4",
    "nor5",
]
pokemon_map = {
    "mew": "mew",
    "nec": "necrozma",
    "cor": "gigantamax-corviknight",
    "ete": "eternamax-eternatus",
    "gro": "groudon",
    "hat": "gigantamax-hatterene",
    "kyo": "kyogre",
    "inc": "incineroar",
    "lao": "latios",
    "met": "metagross",
    "ray": "rayquaza",
    "tyr": "tyranitar",
    "yve": "yveltal",
    "sol": "solgaleo",
    "zek": "zekrom",
    "res": "reshiram",
    "lug": "lugia",
    "gar": "gardevoir",
    "xer": "xerneas",
    "gir": "giratina",
    "arc": "arceus",
    "zac": "zacian",
    "pal": "palkia",
    "dia": "dialga",
    "kyu": "kyurem",
    "arc2": "arceus-fairy",
    "zac2": "zacian-crowned",
    "pal2": "palkia-origin",
    "mew2": "mewtwo",
    "nec2": "necrozma-dawnwings",
    "dia2": "dialga-origin",
    "kyu3": "kyurem-white",
    "arc3": "arceus-steel",
    "mew3": "mega-mewtwo-x",
    "mew4": "mega-mewtwo-y",
    "nec3": "necrozma-duskmane",
    "kyu2": "kyurem-black",
}


async def build_sd_po_embed(
    guild: discord.Guild,
    user_id: str,
    sub_cmd: str,
    user_display_name: str,
):
    # [💙 DEFAULTS] ─────────────────────────────────────
    color = SD_CONFIG.default_color
    footer_text = get_default_footer(user_display_name)
    footer_icon = guild.icon.url if guild.icon else None
    header_text = "STRAYDEX"

    # [🤍 FETCH VALUES] ─────────────────────────────────
    desc = getattr(SD_PO_DESC, sub_cmd, None)
    full_name = pokemon_map.get(sub_cmd, sub_cmd)

    if sub_cmd not in no_weakness_embed_list:
        # Add WEAKNESS CHART section with blockquote style and blank lines exactly as screenshot
        _, weakness_desc, _ = build_weakness_embed_from_input(full_name)
        if weakness_desc:
            # All lines in a single >>> blockquote, blank lines between groups
            weakness_block = "**__WEAKNESS CHART__**\n>>> " + "\n\n".join(weakness_desc)
            desc = f"{desc}\n\n{weakness_block}" if desc else weakness_block

    thumbnail_url = getattr(SD_PO_THUMBNAIL, sub_cmd, None)
    image_url = getattr(SD_PO_IMAGE_URL, sub_cmd, None)

    # [💜 BUILD EMBED] ──────────────────────────────────
    embed = discord.Embed(description=desc or "", color=color)

    # [💙 FOOTER SETUP] ─────────────────────────────────
    if footer_icon:
        embed.set_footer(text=footer_text, icon_url=footer_icon)
    else:
        embed.set_footer(text=footer_text)

    # [🤍 AUTHOR HEADER] ────────────────────────────────
    embed.set_author(name=header_text)

    # [💜 CONDITIONAL THUMBNAIL] ────────────────────────
    if thumbnail_url and thumbnail_url.lower() != "none":
        embed.set_thumbnail(url=thumbnail_url)

    # [💙 CONDITIONAL IMAGE] ────────────────────────────
    if image_url and image_url.lower() != "none":
        embed.set_image(url=image_url)

    return embed


async def build_sd_po_main_embed(
    guild: discord.Guild,
    user_id: str,
    sub_cmd: str,
    user_display_name: str,
):
    embed = await build_sd_po_embed(
        guild=guild,
        user_id=user_id,
        sub_cmd=sub_cmd,
        user_display_name=user_display_name,
    )

    view = SDPokemonView(guild=guild, sub_cmd=sub_cmd, user_id=user_id)

    return embed, view, None


class SDPokemonView(View):
    def __init__(self, guild: discord.Guild, sub_cmd: str, user_id: int):
        super().__init__(timeout=None)
        self.guild = guild
        self.sub_cmd = sub_cmd
        self.user_id = user_id

        #
        try:
            # 💙 Determine main faction (strips trailing numbers)
            PO_SUB_VARIANTS = [
                "deb",
                "deb2",
                "nor",
                "nor2",
                "nor3",
                "nor4",
                "nor5",
                "set",
                "set2",
                "set3",
                "zac",
                "zac2",
                "pal",
                "pal2",
                "mew",
                "mew2",
                "mew3",
                "mew4",
                "nec",
                "nec2",
                "nec3",
                "nec4",
                "dia",
                "dia2",
                "kyu",
                "kyu2",
                "kyu3",
                "wor",
                "wor2",
                "arc",
                "arc2",
                "arc3",
                "arc4",
            ]

            # 💙 Get all variant keys for this faction, sorted so base comes first
            self.variant_keys = sorted(
                [k for k in PO_SUB_VARIANTS if k.startswith(sub_cmd)],
                key=lambda k: (len(k), k),
            )

            # 💙 Add buttons for each variant safely
            for idx, key in enumerate(self.variant_keys):

                # ✅ Fetch label, default to "Unknown" if missing
                label = getattr(SD_PO_BUTTON_LABELS, key, None)

                # 💙 Create and add button
                button = Button(
                    label=label,
                    style=discord.ButtonStyle.secondary,
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
                embed = await build_sd_po_embed(
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
