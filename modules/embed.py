import discord
from modules.wait import wait

PURGE_LIMIT = 12 # CHANGE THIS ONE BACK TO 12 BEFORE LAUNCH


# Public
async def send_embeds2(embed2, embed_array, bot, channel_id, clan_image):
    channel = bot.get_channel(channel_id)
    print('channel')
    print(channel)

    # Remove last FEW messages in channel
    await channel.purge(limit=PURGE_LIMIT) # CHANGE TO 12
    # Send Image
    try:
        await channel.send(clan_image)
        print("sent 1")
    except:
        print('NO IMAGE PROVIDED')

    # Send Embed 2
    await channel.send(embed=embed2)
    print("sent 2")

    num = 3
    for embed in embed_array:
        # Send Embed (if possible)
        if len(embed.description) > 0:
            await channel.send(embed=embed)
            print('sent ' + str(num))
            wait(0.5)
        num += 1


def prepare_embeds_new(clan_repl, clan_array, players_sorted, console_player_amount):
  if clan_repl.format == 'A': 
    embed2, embed_array = __prepare_embeds_A(clan_repl, clan_array, players_sorted, console_player_amount)
  elif clan_repl.format == 'B':
    embed2, embed_array = __prepare_embeds_B(clan_repl, clan_array, players_sorted, console_player_amount)
  return embed2, embed_array

def prepare_embeds_new_server(server, names, current_ratings, peak_ratings,
                              clan_color):

    print('start preparing embeds')

    embed2 = discord.Embed(title=server.name, color=server.color)

    # Variables
    embed_array = []
    global rank
    rank = 1
    count = 0
    embed = discord.Embed(description="", color=server.color)

    # Format Embeds
    print(len(names))
    for (name, current, peak) in zip(names, current_ratings, peak_ratings):
        if count == 0:
            embed = discord.Embed(description="", color=server.color)
        if count <= 20:
            embed.description += "**" + \
                str(rank) + ". " + name + "**: current: **" + str(current) + "** peak: **" + str(peak) + '**\n'
        rank += 1
        count += 1
        if count == 21:
            embed_array.append(embed)
            count = 0
    embed_array.append(embed)
    return embed2, embed_array


# Private
def __add_title(clan_array, embed2):
    if len(clan_array) == 1:
        embed2.title += clan_array[0]['clan_name']
        return embed2
    if len(clan_array) > 1:
        # Title
        count = 0
        for clan in clan_array:
            if count == 0:
                embed2.title += clan['clan_name']
            else:
                embed2.title += " & " + clan_array[count]['clan_name']
            count += 1
        return embed2


def __add_member_count(clan_array, embed2, console_player_amount):
    embed2.description += "\n\n"
    if len(clan_array) == 1:
        embed2.description = '**Member Count\n**'
        embed2.description += "Total: " + str(len(clan_array[0]['clan']) + console_player_amount)
        return embed2
    if len(clan_array) > 1:
        embed2.description += '**Member Count\n**'
        count = 0
        total_member_count = 0
        for clan in clan_array:
            member_count = len(clan['clan'])
            total_member_count += member_count
            if count == 0:
                embed2.description += clan['clan_name'] + ": " + str(
                    member_count)
            else:
                embed2.description += "\n" + clan_array[count][
                    'clan_name'] + ": " + str(member_count)
            count += 1
        if console_player_amount > 0:
            embed2.description += "\n" + "Console: " + str(console_player_amount)

        i = 0
        while i < count:
            #total_xp += int(clan_array[i]['clan_xp'])
            i += 1
        embed2.description += "\nTotal: " + str(total_member_count + console_player_amount)
        #embed2.description += "\n\n"
        return embed2


def __add_xp(clan_array, embed2):
    embed2.description += "\n\n"  
    if len(clan_array) == 1:
        embed2.description += '**Clan XP\n**'
        embed2.description += "Total: " + str(clan_array[0]['clan_xp'])
        return embed2
    if len(clan_array) > 1:

        # Description - Member Count (Make optional)
        embed2.description += '**Clan XP\n**'
        count = 0
        total_xp = 0
        for clan in clan_array:
            clan_xp = int(clan['clan_xp'])
            total_xp += clan_xp
            if count == 0:
                embed2.description += clan['clan_name'] + ": " + str(clan_xp)
            else:
                embed2.description += "\n" + clan_array[count][
                    'clan_name'] + ": " + str(clan_xp)
            count += 1

        i = 0
        while i < count:
            #total_xp += int(clan_array[i]['clan_xp'])
            i += 1
        embed2.description += "\nTotal: " + str(total_xp)
        #embed2.description += "\n\n"
        return embed2

def __prepare_embeds_A(clan_repl, clan_array, players_sorted, console_player_amount):
    print('start preparing embeds - Format A')
    names, current_ratings, peak_ratings = players_sorted[0], players_sorted[
        1], players_sorted[2]

    # OPTIONAL ADD ONS
    embed2 = discord.Embed(title='', description='', color=clan_repl.color)
    embed2 = __add_title(clan_array, embed2)
    if clan_repl.member_count == 'show':
      embed2 = __add_member_count(clan_array, embed2, console_player_amount)
    if clan_repl.xp == 'show':
      embed2 = __add_xp(clan_array, embed2)

    # Variables
    embed_array = []
    global rank
    rank = 1
    count = 0
    embed = discord.Embed(description="", color=clan_repl.color)

    # Format Embeds
    for (name, current, peak) in zip(names, current_ratings, peak_ratings):
        if count == 21:
            embed_array.append(embed)
            count = 0
        if count == 0:
            embed = discord.Embed(description="", color=clan_repl.color)
        if count <= 20:
            embed.description += "**" + \
                str(rank) + ". " + name + "**: current: **" + str(current) + "** peak: **" + str(peak) + '**\n'
        rank += 1
        count += 1
    embed_array.append(embed)
  
    return embed2, embed_array
def __prepare_embeds_B(clan_repl, clan_array, players_sorted, console_player_amount):
    print('start preparing embeds - Format B')
    names, current_ratings, peak_ratings = players_sorted[0], players_sorted[
        1], players_sorted[2]

    # OPTIONAL ADD ONS
    embed2 = discord.Embed(title='', description='', color=clan_repl.color)
    embed2 = __add_title(clan_array, embed2)
    if clan_repl.member_count == 'show':
      embed2 = __add_member_count(clan_array, embed2, console_player_amount)
    if clan_repl.xp == 'show':
      embed2 = __add_xp(clan_array, embed2)

    # Variables
    embed_array = []
    global rank
    rank = 1
    count = 0
    embed = discord.Embed(description="```js\n", color=clan_repl.color)

    # Format Embeds
    for (name, current, peak) in zip(names, current_ratings, peak_ratings):
        if count == 21:
            embed.description += "```"
            embed_array.append(embed)
            count = 0
        if count == 0:
            embed = discord.Embed(description="```", color=clan_repl.color)
        if count <= 20:
            if rank <10:
                embed.description += "" + \
                    "0" + str(rank) + ") " + name + ": current: " + str(current) + " peak: " + str(peak) + '\n'
            else:
                embed.description += "" + \
                    str(rank) + ") " + name + ": current: " + str(current) + " peak: " + str(peak) + '\n'
        rank += 1
        count += 1
        
    embed.description += "```"
    embed_array.append(embed)
  
    return embed2, embed_array