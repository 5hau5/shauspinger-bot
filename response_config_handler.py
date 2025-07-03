import random
import tomli as tomllib
import tomli_w
import settings

CONFIG_PATH_M = settings.RESPONSE_CONFIG
CONFIG_PATH_G = settings.GOOFY_RESPONSE_CONFIG

# with open(CONFIG_PATH_M, "rb") as f:
#     config_m = tomllib.load(f)

# with open(CONFIG_PATH_G, "rb") as f:
#     config_g = tomllib.load(f)

def get_config(main: bool):
    path = CONFIG_PATH_M if main else CONFIG_PATH_G   
    with open(path, "rb") as f:
        return tomllib.load(f)


def save_config(config, main: bool = False):
    path = CONFIG_PATH_M if main else CONFIG_PATH_G
    with open(path, "wb") as f:
        tomli_w.dump(config, f)

def pick_response(message_content: str = None, section: str = None, main: bool = False):
    config = get_config(main)

    if section:
        data = config.get(section, {})
        responses = data.get("responses", [])
        weights = data.get("weights", [])
        if responses and weights:
            return random.choices(responses, weights=weights, k=1)[0]
        return None

    if message_content:
        message_lower = message_content.lower()
        for sec, data in config.items():
            triggers = data.get("triggers", []) if not main else []
            if any(trigger in message_lower for trigger in triggers):
                responses = data.get("responses", [])
                weights = data.get("weights", [])

                if any(resp in message_content for resp in responses):
                    continue

                if responses and weights:
                    return random.choices(responses, weights=weights, k=1)[0]

    return None

def add_trigger(section: str, new_trigger: str, main: bool = False):
    config = get_config(main)
    if new_trigger not in config[section]["triggers"]:
        config[section]["triggers"].append(new_trigger)
        save_config(config, main)

def add_response(section: str, response: str, weight: int, comment: str = "—", main: bool = False):
    config = get_config(main)
    data = config.get(section, {})
    responses = data.get("responses", [])
    if any(resp in response for resp in responses):
        print("alrdy in the tml")
        return
    config[section]["responses"].append(response)
    config[section]["weights"].append(weight)

    if not main:
        config[section]["comments"].append(comment)
    save_config(config, main)

def delete_response_by_index(section: str, index: int, main: bool = False):
    config = get_config(main)
    if 0 <= index < len(config[section]["responses"]):
        del config[section]["responses"][index]
        del config[section]["weights"][index]
        if not main:
            del config[section]["comments"][index]
        save_config(config, main)

def edit_response(section: str, index: int, new_response=None, new_weight=None, new_comment=None, main: bool = False):
    config = get_config(main)
    if 0 <= index < len(config[section]["responses"]):
        if new_response not in (None, "", "''", '""'):
            config[section]["responses"][index] = new_response
        if new_weight not in (None, ""):
            config[section]["weights"][index] = new_weight
        if not main and new_comment not in (None, "", "''", '""'):
            config[section]["comments"][index] = new_comment
        save_config(config, main)



