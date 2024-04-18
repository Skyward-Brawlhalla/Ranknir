import json
from Dadabase.classes.Account import Account
from Dadabase.modules.data_management import read_data, CLANS_DATA_LOCATION


async def add_console_player(interaction, bh_id, bh_name):
    if __validate_id(bh_id):
        account = __create_account(bh_id, bh_name)
        data = read_data(CLANS_DATA_LOCATION, interaction.guild.id)
        __add_ps4_player(interaction, account, data)
        await interaction.response.send_message(bh_name + ' was added')
    else:
        await interaction.response.send_message(str(bh_id) + " is not a valid brawlhalla_id")


def __add_ps4_player(interaction, account, data):
    data['ps4_players'].append(account.__dict__)
    with open(CLANS_DATA_LOCATION + str(interaction.guild.id) + '.json', 'w') as file:
        json.dump(data, file, indent=4)


def __create_account(brawlhalla_id, brawlhalla_name):
    account = Account(brawlhalla_id, brawlhalla_name)
    return account

def __validate_id(id):
    if isinstance(id, int):
        return True
    else:
        return False
