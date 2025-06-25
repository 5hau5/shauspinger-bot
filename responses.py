import random


def respond(dict):
    choices, weights = zip(*dict.items())
    return random.choices(choices, weights=weights, k=1)[0]


get_pinged_responses_1 = {
    "no":10,
    "i disagree":5,
    "kys":1,
}

get_pinged_responses_2 = {
    'https://tenor.com/view/blue-archive-amd-hoshino-takanashi-hoshino-dancing-gif-10581432706103341722':1,
}

r6_ping_responses = {
    "https://cdn.discordapp.com/attachments/746415517350363176/1362732917247184946/yan.gif?ex=6803776d&is=680225ed&hm=296e35890565c0ef3bad94dc4feb62ba082140011fa9e06a5cdc3317a5bc747a&":2,
    'https://cdn.discordapp.com/attachments/738831293864738975/1229465125514383421/reac.gif?ex=662fc7a0&is=661d52a0&hm=665f85732c43985759fc8acbdc3a7d3a073abd94350d56d3d8d9d693083cd9cc&':2
}

not_a_number_responses = {
    "thats not a number retard":10,
    "thats definetly a number":2
}

goofy_aa_big_head_responses = {
    "balls":5,
    "yaa":4,
    "eeee":3,
    "wejbl;kjweqrbujolwe":2
}

#function ot add responsed within the bot


