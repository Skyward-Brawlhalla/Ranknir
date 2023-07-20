from classes.Xos import Xos
import requests
import time
import json

# VARIABLES
API_WAIT_TIME = 10
lilly_clan_id = '864398'
poopy_blender_clan_id = '1923622'

# METHODS


def fetch_clan(clan_id):
    time.sleep(API_WAIT_TIME)  # 0.10 might be possible
    print(clan_id)
    json_object = requests.get(
        "https://api.brawlhalla.com/clan/" + str(clan_id) + "/?api_key=" + Xos().environ[0])
    return json.loads(json_object.content)


def fetch_player_ranked_stats(brawlhalla_id):
    time.sleep(API_WAIT_TIME)
    json_object = requests.get("https://api.brawlhalla.com/player/" +
                               str(brawlhalla_id) + "/ranked?api_key="+Xos().environ[0])
    return json.loads(json_object.content)


def fetch_console_players(id):
    json_object = requests.get(
        "http://game-node01.jetstax.com:27046//get_ps4_players/api_key="+Xos().environ[3]+'?id=' + str(id))
    data = json.loads(json_object.content)
    return data['ps4_players']
# test api
# https://api.brawlhalla.com/player/7364605/ranked?api_key=
# https://api.brawlhalla.com/clan/84648/?api_key=
