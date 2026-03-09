from typing import Literal

import discord
from discord import app_commands
from discord.ext import commands

from utils.autocomplete.pokemon_autocomplete import pokemon_autocomplete
from utils.functions.pokeapi_func import get_pokemon_stats
from utils.functions.pokemon_func import get_display_name
from utils.logs.debug_log import debug_enabled, debug_log, enable_debug
from utils.logs.pretty_log import pretty_log
from utils.visuals.get_pokemon_gifs import get_pokemon_gif
from utils.visuals.pretty_defer import pretty_defer
from utils.visuals.type_embed import (
    build_weakness_embed_from_input,
    get_type_embed_color,
)


class WeaknessChart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="weakness",
        description="Show the weakness chart for a Pokémon based on its types.",
    )
    @app_commands.autocomplete(pokemon=pokemon_autocomplete)
    @app_commands.describe(
        pokemon="The name of the Pokémon.",
    )
    async def weakness(self, interaction: discord.Interaction, pokemon: str):
        loader = await pretty_defer(
            interaction=interaction,
            content="Loading weakness chart...",
            ephemeral=False,
        )

        result = build_weakness_embed_from_input(pokemon)
        if result is None:
            await loader.edit(
                content=f"Could not find weakness information for '{pokemon}'."
            )
            return

        weakness_embed, _, _ = result
        await loader.success(content="", embed=weakness_embed)

    weakness.extras = {"category": "Public"}


async def setup(bot):
    await bot.add_cog(WeaknessChart(bot))

