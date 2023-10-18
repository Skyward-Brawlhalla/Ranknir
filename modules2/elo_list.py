from modules2.get_elo import get_players_elo_1v1, get_players_elo_1v1_and_2v2
from modules2.get_players import get_server_players
from modules2.sort_elo import sort_elo
from modules2.embed import send_embeds, prepare_embeds_clan_mix_console, prepare_embeds_server
from data.server_data import Brawlhalla_NL
from modules2.get_players import get_console_players
from modules2.clan import get_clan_data


########################## CLAN & CONSOLE #########################
async def clan_console_mix_1v1_elo_list(clan, bot):
  # structure -> all_players_array = [[console_players], [clan1_players], [clan2_players], [clan3_players]]
  all_player_objects_array = []
  # Get Console Players
  console_players = get_console_players(clan)
  console_player_objects, _ = await get_players_elo_1v1_and_2v2(clan, console_players)
  all_player_objects_array.append(console_player_objects)
  # Get Clan
  clan_data_array = []
  for clan_id in clan.id_array:
    # Get Clan Data
    clan_data = await get_clan_data(clan_id)
    clan_data_array.append(clan_data)
    # Get Clan Players
    clan_players = clan_data['clan']
    clan_player_objects, _ = await get_players_elo_1v1_and_2v2(
      clan, clan_players)
    all_player_objects_array.append(clan_player_objects)
  # Restructure the array with all players
  all_player_objects_array_restructured = __fix_structure(
    all_player_objects_array)
  all_player_objects_array_sorted = sort_elo(
    clan, all_player_objects_array_restructured)
  embed_title, embed_array = prepare_embeds_clan_mix_console(
    clan,
    all_player_objects_array_sorted,
    clan_data_array,
    console_player_amount=len(console_players))
  await send_embeds(embed_title, embed_array, bot, clan, clan.channel_1v1_id)


async def clan_console_mix_2v2_elo_list(clan, bot):
  # structure -> all_players_array = [[console_players], [clan1_players], [clan2_players], [clan3_players]]
  all_team_objects_array = []
  # Get Console Players
  console_players = get_console_players(clan)
  _, console_team_objects = await get_players_elo_1v1_and_2v2(clan, console_players)
  all_team_objects_array.append(console_team_objects)
  # Get Clan
  clan_data_array = []
  for clan_id in clan.id_array:
    # Get Clan Data
    clan_data = await get_clan_data(clan_id)
    clan_data_array.append(clan_data)
    # Get Clan Players
    clan_players = clan_data['clan']
    _, clan_team_objects = await get_players_elo_1v1_and_2v2(
      clan, clan_players)
    all_team_objects_array.append(clan_team_objects)
  # Restructure the array with all players
  all_team_objects_array_restructured = __fix_structure(all_team_objects_array)
  all_team_objects_array_sorted = sort_elo(
    clan, all_team_objects_array_restructured)
  embed_title, embed_array = prepare_embeds_clan_mix_console(
    clan,
    all_team_objects_array_sorted,
    clan_data_array,
    console_player_amount=len(console_players))
  await send_embeds(embed_title, embed_array, bot, clan, clan.channel_2v2_id)


async def clan_console_mix_1v1_and_2v2_elo_list(clan, bot):
  all_player_objects_array = []
  all_team_objects_array = []
  # Get Console Players
  console_players = get_console_players(clan)
  console_player_objects, console_team_objects = await get_players_elo_1v1_and_2v2(clan, console_players)
  all_player_objects_array.append(console_player_objects)
  all_team_objects_array.append(console_team_objects)
  # Foreach Clan...
  clan_data_array = []
  for clan_id in clan.id_array:
    # Get Clan Data
    clan_data = await get_clan_data(clan_id)
    clan_data_array.append(clan_data)
    # Get Clan Players and Teams
    clan_players = clan_data['clan']
    clan_player_objects, clan_team_objects = await get_players_elo_1v1_and_2v2(
      clan, clan_players)
    all_player_objects_array.append(clan_player_objects)
    all_team_objects_array.append(clan_team_objects)
  # Restructure Players and Teams
  all_player_objects_array_restructured = __fix_structure(all_player_objects_array)
  all_team_objects_array_restructured = __fix_structure(all_team_objects_array)
  # Sort Players and Teams
  all_player_objects_array_sorted = sort_elo(clan, all_player_objects_array_restructured)
  all_team_objects_array_sorted = sort_elo(clan, all_team_objects_array_restructured)
  # Send 1v1 Elo List
  embed_title, embed_array = prepare_embeds_clan_mix_console(
    clan,
    all_player_objects_array_sorted,
    clan_data_array,
    console_player_amount=len(console_players))
  await send_embeds(embed_title, embed_array, bot, clan, clan.channel_1v1_id)
  # Send 2v2 Elo List
  embed_title, embed_array = prepare_embeds_clan_mix_console(
    clan,
    all_team_objects_array_sorted,
    clan_data_array,
    console_player_amount=len(console_players))
  await send_embeds(embed_title, embed_array, bot, clan, clan.channel_2v2_id)




############################### SERVER ##############################


async def server_1v1_elo_list(server, bot):
  print("Server 1v1 elo list for " + server.name)
  __try_update_data(server)
  brawlhalla_nl_players = get_server_players(server)

  all_players_array = await get_players_elo_1v1(brawlhalla_nl_players)
  all_players_sorted = sort_elo(server, all_players_array)
  embed_title, embed_array = prepare_embeds_server(server, all_players_sorted)
  await send_embeds(embed_title, embed_array, bot, server,
                    server.channel_1v1_id)


async def server_2v2_elo_list(server, bot):
  print("Server 2v2 elo list for " + server.name)
  __try_update_data(server)
  brawlhalla_nl_players = get_server_players(server)
  _, all_teams_array = await get_players_elo_1v1_and_2v2(
    server, brawlhalla_nl_players)
  all_teams_sorted = sort_elo(server, all_teams_array)
  embed_title, embed_array = prepare_embeds_server(server, all_teams_sorted)
  await send_embeds(embed_title, embed_array, bot, server,
                    server.channel_2v2_id)


async def server_1v1_and_2v2_elo_list(server, bot):
  print("Server 1v1 and 2v2 elo list for " + server.name)
  __try_update_data(server)
  brawlhalla_nl_players = get_server_players(server)

  all_players_array, all_teams_array = await get_players_elo_1v1_and_2v2(
    server, brawlhalla_nl_players)

  all_players_sorted = sort_elo(server, all_players_array)
  all_teams_sorted = sort_elo(server, all_teams_array)

  embed_title, embed_array = prepare_embeds_server(server, all_players_sorted)
  await send_embeds(embed_title, embed_array, bot, server,
                    server.channel_1v1_id)

  embed_title, embed_array = prepare_embeds_server(server, all_teams_sorted)
  await send_embeds(embed_title, embed_array, bot, server,
                    server.channel_2v2_id)


############################ USEFULL FUNCTIONS ##############################


def __try_update_data(server):
  print("updating data...")
  try:
    server.update_data()
  except:
    print("couldn't update data, make sure Dadabase is running")


def __fix_structure(all_players_array):
  # new structure -> restructured_player_array = [console players + clan1_players + clan2_players + clan3_players]
  restructured_player_array = []
  for player_array in all_players_array:
    for player in player_array:
      restructured_player_array.append(player)
  return restructured_player_array
