import json
from Dadabase.modules.data_management import read_data, remove_player_from_clan_data, CLANS_DATA_LOCATION, DATA_KEY_FOR_CONSOLE_PLAYERS


async def remove_console_player(interaction, brawlhalla_id):
    clan_data = read_data(CLANS_DATA_LOCATION, interaction.guild.id)
    brawlhalla_name = remove_player_from_clan_data(interaction, brawlhalla_id, clan_data, DATA_KEY_FOR_CONSOLE_PLAYERS)
    await interaction.response.send_message(brawlhalla_name + " was removed")
