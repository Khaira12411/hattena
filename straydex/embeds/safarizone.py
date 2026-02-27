import logging

import discord
from discord.ui import Button, View

from constants.aesthetic import Dividers, Emojis
from straydex.config import SD_CONFIG
from straydex.functions.main import  get_default_footer
from straydex.desc.safarizone import SZ_DESC, SZ_Images

from utils.logs.pretty_log import pretty_log

logger = logging.getLogger(__name__)

async def build_sd_main_info_embed(
    guild: discord.Guild,
    user_display_name: str,
    user_id: int,
):
    pass

def build_sd_sub_info_embed(guild: discord.Guild, user_display_name: str, sub: str):
    dex_number = getattr(SZ_DESC, sub)
