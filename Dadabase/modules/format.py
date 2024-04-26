import re


def format_embed_list(data, key):
    msg = ''
    for index, brawlhalla_account in enumerate(data[key], 1):
        msg += f"{index}. **id:** {brawlhalla_account['brawlhalla_id']}, **name:** {brawlhalla_account['brawlhalla_name']}\n"
    return msg



def format_color(color:str):
    def __check_hex_string(s):
        return re.match(r'^0x[a-fA-F0-9]{6}$', s) is not None
    def __check_hex_string_without_hashtag(s):
        return re.match(r'^0x[a-fA-F0-9]{6}$', s) is not None
    def __check_hex_color(s):
        return len(s) == 7 and s.startswith("#")

    if __check_hex_string(color):
        return color
    elif __check_hex_color(color):
        return "0x" + color[1:]
    elif __check_hex_string_without_hashtag(color):
        return "0x" + color[0:]
    else:
        return None
