import discord
from discord.ui import Button, View

from constants.aesthetic import Dividers, Emojis
from straydex.config import SD_CONFIG
from straydex.desc import PS_DESC, PS_EMOJIS, SD_MAIN_IMAGES
from straydex.functions.main import get_default_footer
from utils.logs.pretty_log import pretty_log

PS_CONTENT = f" # STRAYDEX POWER STATION"
# ❀───────────────────────────────❀
#       💖  Power Station Embeds  💖
# ❀───────────────────────────────❀
async def build_sd_ps_main_info_embed(
    guild: discord.Guild,
    user_display_name: str,
    user_id: int,
):
    info_embed = build_sd_ps_info_embed(guild, user_display_name, "i")
    rewards_embed = build_sd_ps_info_embed(guild, user_display_name, "rewards")

    try:
        view = PowerStationInfoView(guild, user_id, info_embed, rewards_embed)
        return info_embed, view, PS_CONTENT
    except Exception as e:
        pretty_log(
            tag="error",
            message=f"Error building Power Station main info embed: {e}",
            include_trace=True,
        )
        fallback_embed = discord.Embed(
            title="Power Station Info",
            description="An error occurred while loading the Power Station information. Please try again later.",
            color=SD_CONFIG.error_color,
        )
        return fallback_embed, None, None

def build_sd_ps_info_embed(guild: discord.Guild, user_display_name: str, sub: str):
    desc = getattr(PS_DESC, sub)
    embed = discord.Embed(description=desc, color=SD_CONFIG.default_color)
    footer_text = get_default_footer(user_display_name)

    icon_url = guild.icon.url if guild.icon else None
    embed.set_footer(text=footer_text, icon_url=icon_url)
    image_url = Dividers.SD_Alternate
    if sub == "i":
        image_url = SD_MAIN_IMAGES.POWERSTATION
    embed.set_image(url=image_url)
    embed.set_author(name="STRAYDEX")
    return embed

class PowerStationInfoView(View):
    def __init__(
        self,
        guild: discord.Guild,
        user_id: int,
        info_embed: discord.Embed,
        rewards_embed: discord.Embed,
    ):
        super().__init__(timeout=None)
        self.guild = guild
        self.user_id = user_id
        self.info_embed = info_embed
        self.rewards_embed = rewards_embed
        self.current_embed = "i"  # Track which embed is currently displayed

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

    async def switch_embed(self, interaction: discord.Interaction, target_embed: str):
        try:
            # Update state before editing the message so the correct button is disabled
            self.current_embed = target_embed
            self.update_button_states()
            if target_embed == "i":
                await interaction.response.edit_message(embed=self.info_embed, view=self)
            elif target_embed == "rewards":
                await interaction.response.edit_message(embed=self.rewards_embed, view=self)
        except Exception as e:
            pretty_log(
                tag="error",
                message=f"Error switching Power Station embed: {e}",
                include_trace=True,
            )
            await interaction.response.send_message(
                "❌ An error occurred while switching the information. Please try again later.",
                ephemeral=True,
            )

    # Buttons for switching between info and rewards
    @discord.ui.button(
        label="Info",
        style=discord.ButtonStyle.secondary,
        custom_id="i",
        emoji=PS_EMOJIS.i,
    )
    async def info_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "i")

    @discord.ui.button(label="Rewards", style=discord.ButtonStyle.secondary, custom_id="rewards", emoji=PS_EMOJIS.rewards)
    async def rewards_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "rewards")


# ❀───────────────────────────────❀
#       💖  Power Station Strat Embed  💖
# ❀───────────────────────────────❀
async def build_sd_ps_main_strat_embed(
    guild: discord.Guild,
    user_display_name: str,
    user_id: int,
):
    strat_one_embed = build_sd_ps_info_embed(guild, user_display_name, "s")
    strat_two_embed = build_sd_ps_info_embed(guild, user_display_name, "strat_two")

    try:
        view = PowerStationStratView(guild, user_id, strat_one_embed, strat_two_embed)
        return strat_one_embed, view, PS_CONTENT
    except Exception as e:
        pretty_log(
            tag="error",
            message=f"Error building Power Station main info embed: {e}",
            include_trace=True,
        )
        fallback_embed = discord.Embed(
            title="Power Station Info",
            description="An error occurred while loading the Power Station information. Please try again later.",
            color=SD_CONFIG.error_color,
        )
        return fallback_embed, None, None

class PowerStationStratView(View):
    def __init__(
        self,
        guild: discord.Guild,
        user_id: int,
        strat_one_embed: discord.Embed,
        strat_two_embed: discord.Embed,
    ):
        super().__init__(timeout=None)
        self.guild = guild
        self.user_id = user_id
        self.strat_one_embed = strat_one_embed
        self.strat_two_embed = strat_two_embed
        self.current_embed = "s"  # Track which embed is currently displayed

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

    async def switch_embed(self, interaction: discord.Interaction, target_embed: str):
        try:
            # Update state before editing the message so the correct button is disabled
            self.current_embed = target_embed
            self.update_button_states()
            if target_embed == "s":
                await interaction.response.edit_message(embed=self.strat_one_embed, view=self)
            elif target_embed == "strat_two":
                await interaction.response.edit_message(embed=self.strat_two_embed, view=self)
        except Exception as e:
            pretty_log(
                tag="error",
                message=f"Error switching Power Station strat embed: {e}",
                include_trace=True,
            )
            await interaction.response.send_message(
                "❌ An error occurred while switching the strategy information. Please try again later.",
                ephemeral=True,
            )
    # Buttons for switching between strat one and strat two
    @discord.ui.button(
        label="Strat 1",
        style=discord.ButtonStyle.secondary,
        custom_id="s",
        emoji=Emojis.battle,
    )
    async def strat_one_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "s")

    @discord.ui.button(label="Strat 2", style=discord.ButtonStyle.secondary, custom_id="strat_two", emoji=Emojis.battle)
    async def strat_two_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "strat_two")
