import discord
from straydex.config import SD_CONFIG
from straydex.functions.main import (
    remove_line_from_desc,
    send_sd_logs,
    get_default_footer,
)
from discord.ui import Button, View
from straydex.desc.wb import *
from utils.logs.pretty_log import pretty_log

wb_map["alc"]
shiny_thumbnail_icon_link = "https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/shiny/charizard-gmax.png"


def wb_consistent_strat(guild: discord.Guild, boss_name: str, user_display_name: str):

    full_boss_name = wb_map[boss_name]
    thumbnail_icon_link = f"https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/regular/{full_boss_name}-gmax.png"
    dex_number = getattr(WB_RegDex, boss_name)
    image_url = getattr(WBRegImage, full_boss_name)

    header_icon_url = getattr(WB_RegHeaderIcon, boss_name)
    header_text = f"GMAX {full_boss_name.upper()} #{dex_number}"

    if boss_name == "uss":
        thumbnail_icon_link = f"https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/regular/urshifu-gmax.png"
        header_text = f"GMAX URSHIFU SINGLE STRIKE #{dex_number}"
        strat = WB_ConsitentStrat.uss

    if boss_name == "urs":
        thumbnail_icon_link = f"https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/regular/urshifu-rapid-strike-gmax.png"
        header_text = f"GMAX URSHIFU RAPID STRIKE #{dex_number}"

    if boss_name == "eet":
        thumbnail_icon_link = "https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/regular/eternatus-eternamax.png"

    if boss_name == "gri":
        strat = getattr(WB_ConsitentStrat, boss_name)
    else:
        strat = WB_ConsitentStrat.mewtwo_strat
    color = getattr(WBColors, full_boss_name)
    embed = discord.Embed(description=strat, color=color)
    embed.set_thumbnail(url=thumbnail_icon_link)
    embed.set_author(name=header_text, icon_url=header_icon_url)
    embed.set_image(url=image_url)
    footer_text = get_default_footer(user_display_name)
    embed.set_footer(text=footer_text, icon_url=guild.icon.url)
    return embed


def wb_mvp_strat(guild: discord.Guild, boss_name: str, user_display_name: str):

    full_boss_name = wb_map[boss_name]
    thumbnail_icon_link = f"https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/shiny/{full_boss_name}-gmax.png"
    dex_number = int(getattr(WB_RegDex, boss_name)) + 1
    image_url = getattr(WBShinyImage, full_boss_name)

    header_icon_url = getattr(WB_ShinyHeaderIcon, boss_name)
    header_text = f"SHINY GMAX {full_boss_name.upper()} #{dex_number}"

    if boss_name == "uss":
        thumbnail_icon_link = f"https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/shiny/urshifu-gmax.png"
        header_text = f"SHINY GMAX URSHIFU SINGLE STRIKE #{dex_number}"
        strat = WB_MVPStrat.necorzma_ultra

    # MMY METRONOME FOR URS AND GRI
    if boss_name == "urs":
        thumbnail_icon_link = f"https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/shiny/urshifu-rapid-strike-gmax.png"
        header_text = f"SHINY GMAX URSHIFU RAPID STRIKE #{dex_number}"
        strat = WB_MVPStrat.necorzma_ultra

    if boss_name == "gri":
        strat = WB_MVPStrat.mmy_metronome

    if boss_name == "uss":
        strat = WB_MVPStrat.mmy_metronome

    if boss_name == "coa":
        strat = WB_MVPStrat.inteleon

    if boss_name == "eet":
        thumbnail_icon_link = "https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/shiny/eternatus-eternamax.png"
        strat = WB_MVPStrat.necorzma_ultra

    if boss_name in ("cor", "cop", "orb"):
        strat = WB_MVPStrat.incineroar

    if boss_name in ("ven", "mac", "gen", "gab", "tox"):
        strat = WB_MVPStrat.necorzma_ultra

    else:
        strat = WB_MVPStrat.mmy
    color = WBColors.Shiny
    embed = discord.Embed(description=strat, color=color)
    embed.set_thumbnail(url=thumbnail_icon_link)
    embed.set_author(name=header_text, icon_url=header_icon_url)
    embed.set_image(url=image_url)
    footer_text = get_default_footer(user_display_name)
    embed.set_footer(text=footer_text, icon_url=guild.icon.url)
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
