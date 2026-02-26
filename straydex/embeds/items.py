import discord
from discord.ui import Button, View

from constants.aesthetic import Dividers
from straydex.config import SD_CONFIG
from utils.logs.pretty_log import pretty_log

CANT_BE_HELD_ITEM_LIST = [
    "shinycharm",
    "amuletcoin",
    "expcharm",
    "expshare",
    "dowsingmachine",
    "itemring",
    "scanner",
    "largepack",
    "pokeradar",
    "scubagear",

]
def add_can_be_held_info(text: str, item_name:str) -> str:
    """Appends a note about the item being holdable if not already present."""
    held_line = ("- ✅ Yes\n- `;team give <item> <mon>`")

    if "**CAN BE HELD BY POKEMON?**" not in text:
        if item_name not in CANT_BE_HELD_ITEM_LIST:
            text += f"\n\n**CAN BE HELD BY POKEMON?**\n{held_line}"
        else:
            text += "\n\n**CAN BE HELD BY POKEMON?**\n- ❌ No"
    return text


async def build_sd_item_embed(
    guild: discord.Guild,
    main_cmd: str,
    text: str,
    user_display_name: str,
    image_url: str = None,
):
    from straydex.AR.h import it_sub

    author_text = "STRAYDEX: ITEM"
    footer_text = "Type !it to view the complete item list."
    pretty_log("debug", f"Building item embed for {main_cmd} with text length {len(text)}")
    text = add_can_be_held_info(text, main_cmd)

    embed = discord.Embed(description=text, color=SD_CONFIG.default_color)
    embed.set_image(url=Dividers.SD_Alternate)

    if image_url:
        embed.set_thumbnail(url=image_url)
    embed.set_footer(text=footer_text, icon_url=guild.icon.url)
    embed.set_author(name=author_text)

    return embed


async def build_sd_main_item_embed(
    guild: discord.Guild,
    user_display_name: str,
    user_id: int,
    image_url: str = None,
    text: str = None,
):
    from straydex.desc.h import SD_MAIN_DESC, SD_MAIN_IMAGES

    from .generic import build_sd_main_embed

    general_item_embed = await build_sd_main_embed(
        guild=guild,
        main_cmd="it",
        text=SD_MAIN_DESC.it,
        user_display_name=user_display_name,
        image_url=SD_MAIN_IMAGES.Items,
    )

    battle_item_embed = await build_sd_main_embed(
        guild=guild,
        main_cmd="it",
        text=SD_MAIN_DESC.it_two,
        user_display_name=user_display_name,
        image_url=SD_MAIN_IMAGES.BATTLE_ITEMS,
    )

    evolution_item_embed = await build_sd_main_embed(
        guild=guild,
        main_cmd="it",
        text=SD_MAIN_DESC.it_three,
        user_display_name=user_display_name,
        image_url=SD_MAIN_IMAGES.EVOI,
    )

    view = ItemListView(
        guild=guild,
        user_id=user_id,
        general_item_embed=general_item_embed,
        battle_item_embed=battle_item_embed,
        evolution_item_embed=evolution_item_embed,
    )
    return general_item_embed, view, None


# 🟦────────────────────────────────────────────
#       ItemListView (Fixed)
# 🟦────────────────────────────────────────────
class ItemListView(View):
    def __init__(
        self,
        guild,
        user_id,
        general_item_embed,
        battle_item_embed,
        evolution_item_embed,
    ):
        super().__init__(timeout=300)  # 5 min timeout
        self.guild = guild
        self.user_id = user_id
        self.general_item_embed = general_item_embed
        self.battle_item_embed = battle_item_embed
        self.evolution_item_embed = evolution_item_embed
        self.current_embed = "General"
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
                    if child.label == "General":
                        child.disabled = embed_name == "General"
                    elif child.label == "Battle":
                        child.disabled = embed_name == "Battle"
                    elif child.label == "Evolution":
                        child.disabled = embed_name == "Evolution"

            # Then edit the message with the new embed and updated buttons
            if embed_name == "General":
                await interaction.response.edit_message(
                    embed=self.general_item_embed, view=self
                )
            elif embed_name == "Battle":
                await interaction.response.edit_message(
                    embed=self.battle_item_embed, view=self
                )
            elif embed_name == "Evolution":
                await interaction.response.edit_message(
                    embed=self.evolution_item_embed, view=self
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
    @discord.ui.button(
        label="General", style=discord.ButtonStyle.primary, disabled=True
    )
    async def general_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "General")

    @discord.ui.button(label="Battle", style=discord.ButtonStyle.secondary)
    async def battle_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "Battle")

    @discord.ui.button(label="Evolution", style=discord.ButtonStyle.secondary)
    async def evolution_button(self, interaction: discord.Interaction, button: Button):
        await self.switch_embed(interaction, "Evolution")
