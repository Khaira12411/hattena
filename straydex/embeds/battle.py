import discord
from discord.ui import Button, View

from constants.aesthetic import Dividers
from straydex.config import SD_CONFIG
from straydex.desc import sd_battle_dict
from utils.logs.pretty_log import pretty_log
from straydex.functions.main import (
    remove_line_from_desc,
    get_default_footer,
)


# 💙────────────────────────────────────────────
#   ✨ Build Straydex Battle Embed
# 💙────────────────────────────────────────────
async def build_sd_battle_embed(
    guild: discord.Guild,
    user_display_name: str,
    sub_cmd: str,
    user_id: int,
    text: str,
    button_label: str,
    thumbnail_url: str = None,
    button_emoji: str = None,
):
    # 🎨 Embed styling
    color = SD_CONFIG.default_color
    image_url = Dividers.SD_Alternate

    # 🏗️ Create the base embed
    embed = discord.Embed(description=text, color=color)
    embed.set_author(name="STRAYDEX: BATTLE")

    # 🖼️ Thumbnail (if provided)
    embed.set_thumbnail(url=thumbnail_url)

    # 🐾 Footer setup
    footer_text = get_default_footer(user_display_name)
    embed.set_footer(text=footer_text, icon_url=guild.icon.url if guild.icon else None)

    # 🌈 Decorative divider image
    embed.set_image(url=image_url)

    return embed


# 💙────────────────────────────────────────────
#   🎀 Build Straydex Main Battle Embed
# 💙────────────────────────────────────────────
async def build_sd_main_battle_embed(
    guild: discord.Guild,
    user_display_name: str,
    sub_cmd: str,
    user_id: int,
    text: str,
    button_label: str,
    thumbnail_url: str = None,
    button_emoji: str = None,
):
    #print(sub_cmd)
    # 📦 Reuse the standard battle embed builder
    embed = await build_sd_battle_embed(
        guild=guild,
        user_display_name=user_display_name,
        sub_cmd=sub_cmd,
        user_id=user_id,
        text=text,
        button_label=button_label,
        thumbnail_url=thumbnail_url,
        button_emoji=button_emoji,
    )
    view = SDBattleView(guild=guild, base_key=sub_cmd, user_id=user_id)

    return embed, view, None


class SDBattleView(View):
    def __init__(self, guild: discord.Guild, base_key: str, user_id: int):
        super().__init__(timeout=None)
        self.guild = guild
        self.base_key = base_key
        self.user_id = user_id

        try:
            # 💙 Build all variant keys (e.g., cba, cba2, cba3...)
            self.variant_keys = sorted(
                [k for k in sd_battle_dict if k.startswith(base_key)],
                key=lambda k: (len(k), k),  # ensures 'cba' before 'cba2'
            )

            # 💙 Add a button for each variant
            for idx, key in enumerate(self.variant_keys):
                data = sd_battle_dict[key]
                button = Button(
                    label=data["button_label"],
                    emoji=data["button_emoji"],
                    style=discord.ButtonStyle.secondary,
                    custom_id=key,
                    disabled=(idx == 0),  # disable the first button initially
                )
                button.callback = self.make_callback(key)
                self.add_item(button)

        except Exception as e:
            pretty_log(
                message=f"🔥 Error initializing SDBattleView for '{base_key}': {e}",
            )

    def make_callback(self, key: str):
        async def callback(interaction: discord.Interaction):
            # 🔒 Restrict to command user only
            if interaction.user.id != self.user_id:
                await interaction.response.send_message(
                    "❌ This isn't your battle! (only the original commander can press these 💪)",
                    ephemeral=True,
                )
                return

            try:
                # 💙 Update embed to reflect selected variant
                data = sd_battle_dict[key]

                embed = await build_sd_battle_embed(
                    guild=self.guild,
                    user_display_name=interaction.user.display_name,
                    sub_cmd=key,
                    user_id=self.user_id,
                    text=data["desc"],
                    button_label=data["button_label"],
                    thumbnail_url=data["thumbnail_url"],
                    button_emoji=data["button_emoji"],
                )

                # 💙 Update button states
                for item in self.children:
                    if isinstance(item, Button):
                        item.disabled = item.custom_id == key

                await interaction.response.edit_message(embed=embed, view=self)

            except Exception as e:
                pretty_log(
                    message=f"🔥 Error updating battle view for '{key}': {e}",
                )
                await interaction.response.send_message(
                    "⚠️ Oops! Something went wrong while updating the battle.",
                    ephemeral=True,
                )

        return callback
        return callback
