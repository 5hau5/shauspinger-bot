import random
import tomli as tomllib
import tomli_w
import settings

CONFIG_PATH = settings.RESPONSE_CONFIG

with open(CONFIG_PATH, "rb") as f:
    config = tomllib.load(f)

def save_config():
    with open(CONFIG_PATH, "wb") as f:
        tomli_w.dump(config, f)


def pick_response(message_content: str = None, section: str = None):
    # If a section is given directly
    if section:
        data = config.get(section, {})
        responses = data.get("responses", [])
        weights = data.get("weights", [])
        if responses and weights:
            return random.choices(responses, weights=weights, k=1)[0]
        return None

    # Otherwise, use trigger matching
    if message_content:
        message_lower = message_content.lower()
        for sec, data in config.items():
            triggers = data.get("triggers", [])
            if any(trigger in message_lower for trigger in triggers):
                responses = data.get("responses", [])
                weights = data.get("weights", [])
                if responses and weights:
                    return random.choices(responses, weights=weights, k=1)[0]

    return None


def add_trigger(section, new_trigger):
    if new_trigger not in config[section]["triggers"]:
        config[section]["triggers"].append(new_trigger)
        save_config()

def delete_trigger(section, trigger):
    if trigger in config[section]["triggers"]:
        config[section]["triggers"].remove(trigger)
        save_config()

def add_response(section, response, weight, comment="—"):
    config[section]["responses"].append(response)
    config[section]["weights"].append(weight)
    config[section]["comments"].append(comment)
    save_config()


def delete_response_by_index(section, index):
    if 0 <= index < len(config[section]["responses"]):
        del config[section]["responses"][index]
        del config[section]["weights"][index]
        del config[section]["comments"][index]
        save_config()

def edit_response(section, index, new_response, new_weight, new_comment):
    if 0 <= index < len(config[section]["responses"]):
        config[section]["responses"][index] = new_response
        config[section]["weights"][index] = new_weight
        config[section]["comments"][index] = new_comment
        save_config()


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

sex_responses = {
    'https://cdn.discordapp.com/attachments/738831293864738975/1229998157941833758/segs-arona.gif?ex=6631b80d&is=661f430d&hm=08dce8539c48abe0a9ccbefb101cd9309fff33148e35b546facda55cbf4fae2e&':10,

}

#function ot add responsed within the bot
#change the link to be in resorses


