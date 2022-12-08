from secrets import get_keys
import os
import discord
from discord.ext import commands
from modules.keep_alive import keep_alive
from modules.embed import send_embeds2, prepare_embeds_new
from modules.sort_elo import sort_elo_1v1, sort_2v2_elo
#from modules.wait import wait
#from modules.turn import get_turn, next_turn
from modules.turn import reset_turn
from modules.clan import get_clans_data
from classes.clan import Clan

#TODO FIX PREAPRE EMBEDS

Skyward = Clan("NO ACCESS", 976552050953437194, ['84648'], 0x289fb4, 'https://cdn.discordapp.com/attachments/841405262023884820/841405879496212530/Skyward-1.png')

lnsomnia_clan_id, Parasomnia_clan_id, Hypnosia_clan_id = '1919781', '1927502', '2022800'
lnsomnia = Clan(988484998799716423, 1006780905131614280, [lnsomnia_clan_id, Parasomnia_clan_id, Hypnosia_clan_id] , 0x301834, "https://cdn.discordapp.com/attachments/967468594285924382/1006783742179823646/Insomnia_Logo_Concept_Purple.png")

Pandation_clan_id, Pandace_clan_id, Panhalla_clan_id, PanhaIIa_clan_id = '1702413', '1868949', '1709279', '1722822'
Pandation = Clan(990292557386899527, 1016402549491912794, [Pandation_clan_id, Pandace_clan_id, Panhalla_clan_id, PanhaIIa_clan_id], 0x212226, "https://media.discordapp.net/attachments/958131738503155714/958141534455337031/standard.gif")


Dair = Clan("NO ACCESS", 1029669276363280414, ['1357965'], 0x349feb,        'https://cdn.discordapp.com/attachments/994165604602880031/1024740143015399424/unknown.png')

Cybers_clan_id, Cybers_II_clan_id, Xybers_clan_id = '1983079', '1983274', '2041304'
Cybers = Clan(1039202472536834108, 1039202527398334514, [Cybers_clan_id, Cybers_II_clan_id, Xybers_clan_id], 0xD10000, " ")

Cherimoya = Clan(1042189651118674010, "N/A", ['2024340'], 0x19eb8f, " ")

# Testing
wanak1n_clan_id, test2_clan_id, test3_clan_id = '1363653', '2021161', '2023962'
test_clan = Clan(973594560368373820, 973594560368373820, [wanak1n_clan_id, test2_clan_id, test3_clan_id], 0xD10000, " ")

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['r', 'R'], intents=intents)
turn = 8

@bot.event
async def on_ready():
    # I'm back online!
    print(f'We have logged in as {bot.user}')
    skyward_log_channel_id = bot.get_channel(973594560368373820)
    await skyward_log_channel_id.send("I'm back online!")

    # main, send 1v1 / 2v2 elo list
    while True:
        #turn = get_turn()
        global turn
        print("current turn: " + str(turn))
        if turn == 0:
            await main_2v2_crazy(Dair, sorting_method="current")
        elif turn == 1:
            await main_1v1_crazy(Pandation, sorting_method="peak")
        elif turn == 2:
            await main_2v2_crazy(Pandation, sorting_method="peak")
        elif turn == 3:
            await main_2v2_crazy(lnsomnia, sorting_method="peak")
        elif turn == 4:
            await main_1v1_crazy(lnsomnia, sorting_method="peak")
        elif turn == 21:
            await main_2v2_crazy(test_clan, sorting_method="current")
        elif turn == 5:
            await main_1v1_crazy(Cybers, sorting_method="peak")
        elif turn == 6:
            await main_2v2_crazy(Cybers, sorting_method="current")
        elif turn == 7:
          await main_2v2_crazy(Skyward, sorting_method="current")
        elif turn == 8:
            await main_1v1_crazy(Cherimoya, sorting_method="peak")
            reset_turn()
        turn += 1
        if turn > 8:
            turn = 0
        #next_turn()
        #wait(300)

async def main_1v1_crazy(clan, sorting_method):

  # get players elo sorted
  names, current_ratings, peak_ratings = sort_elo_1v1(clan.id_array, sorting_method)
  print(names)

  # get clans
  clans_data = get_clans_data(clan.id_array)

  # prep embeds
  embed2, embed_array = prepare_embeds_new(clans_data , names, current_ratings, peak_ratings, clan.color)
  
  await send_embeds2(embed2, embed_array, bot=bot, channel_id=clan.channel_1v1_id, clan_image=clan.image)

  # clear arrays
  names.clear()
  current_ratings.clear()
  peak_ratings.clear()

async def main_2v2_crazy(clan, sorting_method):

  # get players elo sorted
  names, current_ratings, peak_ratings = sort_2v2_elo(clan.id_array, sorting_method)

  # get clans
  clans = get_clans_data(clan.id_array)

  # prep embeds
  embed2, embed_array = prepare_embeds_new(clans, names, current_ratings, peak_ratings, clan.color)

  await send_embeds2(embed2, embed_array, bot=bot, channel_id=clan.channel_1v1_id, clan_image=clan.image)
  
  # clear arrays
  names.clear()
  current_ratings.clear()
  peak_ratings.clear()

#keep_alive()
bot.run(os.environ["BOT_KEY"])
