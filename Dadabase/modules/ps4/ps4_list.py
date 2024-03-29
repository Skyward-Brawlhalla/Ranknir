from Dadabase.modules.ps4.ps4_data import load_data
import discord


async def ps4_list(ctx):
    data = load_data(ctx.guild.id)
    msg = __format_msg(data)
    embed = __create_embed(msg)
    await ctx.channel.send(embed=embed)


def __format_msg(data):
    msg = ''
    count = 1
    for entry in data['ps4_players']:
        msg += str(count) + '. ' + '**id:** ' + \
            entry['brawlhalla_id'] + ', **name**: ' + \
            entry['brawlhalla_name'] + '\n'
        count += 1
    return msg


def __create_embed(msg):
    return discord.Embed(title="Console Players", description="The following players will be added to the leaderboard manually. To add another run: `d!ps4add id nickname`. To remove one run: `d!ps4rm id`\n" + msg, color=0x00ff00)
