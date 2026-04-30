import discord
from discord.ui import Button, View

from straydex.config import SD_CONFIG
from straydex.desc.wb import *
from straydex.functions.main import (
    get_default_footer,
)
from constants.aesthetic import Dividers, Emojis
from utils.logs.pretty_log import pretty_log

wb_map["alc"]
shiny_thumbnail_icon_link = "https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/shiny/charizard-gmax.png"


def wb_consistent_strat(guild: discord.Guild, boss_name: str, user_display_name: str):

    full_boss_name = wb_map[boss_name]
    thumbnail_icon_link = f"https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/regular/{full_boss_name}-gmax.png"
    dex_number = getattr(WB_RegDex, boss_name)
    image_url = getattr(WBRegImage, full_boss_name)

    header_icon_url = getattr(WB_RegHeaderIcon, boss_name)
    header_text = f"GIGANTAMAX-{full_boss_name.upper()} #{dex_number}"

    if boss_name == "uss":
        thumbnail_icon_link = f"https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/regular/urshifu-gmax.png"
        header_text = f"GIGANTAMAX-URSHIFU-SINGLESTRIKE #{dex_number}"
        strat = WB_ConsitentStrat.uss

    elif boss_name == "urs":
        thumbnail_icon_link = f"https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/regular/urshifu-rapid-strike-gmax.png"
        header_text = f"GIGANTAMAX-URSHIFU-RAPIDSTRIKE #{dex_number}"
        strat = WB_ConsitentStrat.mewtwo_strat

    elif boss_name == "gen":
        strat = WB_ConsitentStrat.gengar_strat

    elif boss_name == "eet":
        thumbnail_icon_link = "https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/regular/eternatus-eternamax.png"
        strat = WB_ConsitentStrat.mewtwo_strat
        header_text = f"ETERNAMAX-ETERNATUS #{dex_number}"

    elif boss_name == "gri":
        strat = WB_ConsitentStrat.gri
    elif boss_name in ["mel", "cop", "dur", "cor"]:
        strat = WB_ConsitentStrat.steel_type_strat
    elif boss_name == "orb":
        strat = WB_ConsitentStrat.incineroar

    else:
        strat = WB_ConsitentStrat.mewtwo_strat

    color = getattr(WBColors, full_boss_name)
    embed = discord.Embed(description=strat, color=color)
    embed.set_thumbnail(url=thumbnail_icon_link)
    embed.set_author(name=header_text, icon_url=header_icon_url)
    embed.set_image(url=image_url)
    footer_text = get_default_footer(user_display_name)
    embed.set_footer(text=footer_text, icon_url=guild.icon.url if guild.icon else None)
    return embed


def wb_mvp_strat(guild: discord.Guild, boss_name: str, user_display_name: str):

    full_boss_name = wb_map[boss_name]
    thumbnail_icon_link = f"https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/shiny/{full_boss_name}-gmax.png"
    dex_number = int(getattr(WB_RegDex, boss_name)) + 1
    image_url = getattr(WBShinyImage, full_boss_name)

    header_icon_url = getattr(WB_ShinyHeaderIcon, boss_name)
    header_text = f"SHINY GIGANTAMAX-{full_boss_name.upper()} #{dex_number}"

    if boss_name == "uss":
        thumbnail_icon_link = f"https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/shiny/urshifu-gmax.png"
        header_text = f"SHINY GIGANTAMAX-URSHIFU-SINGLESTRIKE #{dex_number}"
        strat = WB_MVPStrat.uss

    # MMY METRONOME FOR URS AND GRI
    elif boss_name == "urs":
        thumbnail_icon_link = f"https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/shiny/urshifu-rapid-strike-gmax.png"
        header_text = f"SHINY GIGANTAMAX-URSHIFU-RAPIDSTRIKE #{dex_number}"
        strat = WB_MVPStrat.necorzma_ultra

    elif boss_name == "gri":
        strat = WB_MVPStrat.zac_crowned

    elif boss_name == "coa":
        strat = WB_MVPStrat.coa

    elif boss_name == "eet":
        thumbnail_icon_link = "https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/shiny/eternatus-eternamax.png"
        strat = WB_MVPStrat.necorzma_ultra
        header_text = f"SHINY ETERNAMAX-ETERNATUS #{dex_number}"

    elif boss_name in ["mel", "cop", "dur", "cor"]:
        strat = WB_MVPStrat.braviary

    elif boss_name in ("orb", "hat"):
        strat = WB_MVPStrat.incineroar

    elif boss_name in ("app", "fla"):
        strat = WB_MVPStrat.glalie

    elif boss_name in ("cen", "cha", "but"):
        strat = WB_MVPStrat.shuckle

    elif boss_name in ("ven", "mac", "gen", "gab", "tox"):
        strat = WB_MVPStrat.necorzma_ultra

    else:
        strat = WB_MVPStrat.mmy
    color = WBColors.Shiny
    embed = discord.Embed(description=strat, color=color)
    embed.set_thumbnail(url=thumbnail_icon_link)
    embed.set_author(name=header_text, icon_url=header_icon_url)
    embed.set_image(url=image_url)
    footer_text = get_default_footer(user_display_name)
    embed.set_footer(text=footer_text, icon_url=guild.icon.url if guild.icon else None)
    return embed


class WBStratView(View):
    def __init__(self, guild, boss_name, user_display_name, author_id):
        super().__init__(timeout=120)  # 2 minutes timeout
        self.guild = guild
        self.boss_name = boss_name
        self.user_display_name = user_display_name
        self.author_id = author_id

        # Get emojis dynamically
        try:
            consistency_emoji = getattr(WB_REGEMOJI, boss_name)
            mvp_emoji = getattr(WB_SHINYEMOJI, boss_name)
        except AttributeError:
            consistency_emoji = None
            mvp_emoji = None
            pretty_log(
                tag="error",
                message=f"Emojis not found for boss '{boss_name}'.",
            )

        # Create buttons
        self.consistency_button = Button(
            label="Consistency",
            style=discord.ButtonStyle.secondary,
            emoji=consistency_emoji,
            disabled=True,  # Start with Consistency active
        )
        self.mvp_button = Button(
            label="MVP",
            style=discord.ButtonStyle.secondary,
            emoji=mvp_emoji,
            disabled=False,
        )

        # Assign callbacks
        self.consistency_button.callback = self.consistency_callback
        self.mvp_button.callback = self.mvp_callback

        # Add buttons to view
        self.add_item(self.consistency_button)
        self.add_item(self.mvp_button)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.author_id:
            try:
                await interaction.response.send_message(
                    "This button isn't for you!", ephemeral=True
                )
            except Exception as e:

                pretty_log(
                    tag="error",
                    message=f"Failed to send ephemeral message to user {interaction.user.name}",
                )
            return False
        return True

    async def consistency_callback(self, interaction: discord.Interaction):
        try:
            embed = wb_consistent_strat(
                guild=self.guild,
                boss_name=self.boss_name,
                user_display_name=self.user_display_name,
            )
            # Update button states
            self.consistency_button.disabled = True
            self.mvp_button.disabled = False

            await interaction.response.edit_message(embed=embed, view=self)
        except Exception as e:
            pretty_log(
                tag="error",
                message=f"Error in Consistency button callback for user {interaction.user.name}: {e}",
            )
            try:
                await interaction.response.send_message(
                    "Something went wrong while processing your request.",
                    ephemeral=True,
                )
            except Exception as send_err:
                pretty_log(
                    tag="error",
                    message=f"Failed to send error message to user {interaction.user.name}: {send_err}",
                )

    async def mvp_callback(self, interaction: discord.Interaction):
        try:
            embed = wb_mvp_strat(
                guild=self.guild,
                boss_name=self.boss_name,
                user_display_name=self.user_display_name,
            )
            # Update button states
            self.mvp_button.disabled = True
            self.consistency_button.disabled = False

            await interaction.response.edit_message(embed=embed, view=self)
        except Exception as e:
            pretty_log(
                tag="error",
                message=f"Error in MVP button callback for user {interaction.user.name}: {e}",
            )
            try:
                await interaction.response.send_message(
                    "Something went wrong while processing your request.",
                    ephemeral=True,
                )
            except Exception as send_err:
                pretty_log(
                    tag="error",
                    message=f"Failed to send error message to user {interaction.user.name}: {send_err}",
                )

    async def on_timeout(self):
        try:
            # Disable all buttons after timeout
            for child in self.children:
                child.disabled = True
            # To edit the message after timeout, store reference to message when sending
            # e.g., self.message = sent_message
            # await self.message.edit(view=self)
        except Exception as e:
            pretty_log(
                tag="error",
                message=f"Error during view timeout handling: {e}",
            )


async def build_sd_wb_embed(
    guild: discord.Guild, boss_name: str, user_display_name: str, user_id: int
):
    # Example embed creation for World Boss info
    embed = wb_consistent_strat(
        guild=guild, boss_name=boss_name, user_display_name=user_display_name
    )
    view = WBStratView(
        guild=guild,
        boss_name=boss_name,
        user_display_name=user_display_name,
        author_id=user_id,
    )  # pass user_id so you can restrict button presses
    wb_content = "# STRAYDEX: WORLD BOSS"
    return embed, view, wb_content


async def build_sd_wb_sketch_embed(
    guild: discord.Guild, boss_name: str, user_display_name: str, user_id: int
):
    #
    desc = "# WORLD BOSS: SKETCH IDS"
    embed = discord.Embed(description=desc, color=SD_CONFIG.default_color)
    embed.add_field(
        name=f"{Emojis.purple_arrow} For Smeargle 1",
        value=";b user 797775586038513674",
        inline=False,
    )
    embed.add_field(
        name=f"{Emojis.purple_arrow} For Smeargle 2",
        value=";b user 788960681814261850",
        inline=False,
    )
    info = f"""
**Smeargle 1 Team:**
- Psyduck - `Simple-Beam`
- Jolteon - `Fake-Tears` `Eerie-Impulse`
- Ninetales - `Baton-Pass`
**Smeargle 2 Team:**
- Igglybuff - `Role-Play`
- Arrokuda - `Focus-Energy` `Acupressure`
- Ninetales - `Baton-Pass`

**Notes:**
- After the Pokemon uses the move you need, press Sketch.
- You can only sketch once per battle, so you will need to finish the battle or forfeit. (If you haven't trained Smeargle's EVs then forfeit so you don't mess up Evs or turn off your exp share `;t disable expshare`)
- Buy the Sketch move again. In the next battle, use another Pokemon to knock out the Pokemon whose move you already sketched, then just swap to Smeargle and use Sketch on the next move that you want.
- For Jolteon and Arrokuda, you have to wait until it uses the move you want before you press Sketch.
- You need to have two of these for the strategy: Smeargle, Shiny Smeargle, or Golden Smeargle.
- Credits to OS for this guide."""

    embed.add_field(name=f"{Emojis.info} Info", value=info, inline=False)
    footer_text = get_default_footer(user_display_name)
    embed.set_footer(text=footer_text, icon_url=guild.icon.url if guild.icon else None)
    thumbnail_url = "https://graphics.tppcrpg.net/xy/golden/235M.gif"

    embed.set_thumbnail(url=thumbnail_url)
    embed.set_image(url=Dividers.SD_Alternate)
    embed.set_author(name="STRAYDEX")
    view = WBSKETCHVIEW(
        guild=guild, user_id=user_id, embed=embed
    )  # pass user_id so you can restrict button presses
    return embed, view, None


class WBSKETCHVIEW(View):
    def __init__(self, guild, user_id, embed):
        super().__init__(timeout=120)  # 2 minutes timeout
        self.guild = guild
        self.user_id = user_id
        self.embed = embed
        self.iphone_copy = False

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        """Restrict button presses to the original user."""
        if interaction.user.id != self.user_id:
            await interaction.response.send_message(
                "⚠️ Only the original user can use these buttons.", ephemeral=True
            )
            return False
        return True

    @discord.ui.button(
        label="Toggle Iphone Copy",
        style=discord.ButtonStyle.secondary,
        emoji=Emojis.toggle,
    )
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

        # Update embed fields if current view is Levels
        embed = self.embed.copy()
        for i, field in enumerate(embed.fields):
            if "Smeargle 1" in field.name or "Smeargle 2" in field.name:
                embed.set_field_at(
                    i,
                    name=field.name,
                    value=toggle_backticks(field.value, self.iphone_copy),
                    inline=field.inline,
                )
        self.trl_embed = embed
        await interaction.response.edit_message(embed=self.trl_embed, view=self)
