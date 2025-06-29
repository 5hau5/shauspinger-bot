import os
from dotenv import load_dotenv
from logging.config import dictConfig
import logging
import pathlib
import discord


load_dotenv()
DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")

PREFIX = "//"
VERSION = os.getenv("VERSION")

BASE_DIR = pathlib.Path(__file__).parent
CMDS_DIR = BASE_DIR / "commands"
COGS_DIR = BASE_DIR / "cogs"
RESOURCE_DIR = BASE_DIR / "resources"
GOOFY_RESPONSE_CONFIG = "goofy_responses.toml"
RESPONSE_CONFIG = "responses.toml"

GUILDS_ID = discord.Object(id=int(os.getenv("GUILD")))
MAIN_CHANNEL_ID = int(os.getenv("MAIN_CHANNEL"))
THE_SHAUS_ID = int(os.getenv("SHAUS_ID"))
MILO_ID = int(os.getenv("MILO_ID"))

HYDRUS_API_KEY = os.getenv("HYDRUS_API_KEY")
HYDRUS_API_URL = "http://127.0.0.1:45869"

LOGGING_CONFIG = {
    "version":1,
    "disabled_existing_Loggers":False,
    "formatters":{
        "verbose":{
            "format":"%(levelname)-10s - %(acstime)s - %(module)-15s : %(message)s"
        },
        "standard":{
            "format":"%(levelname)-10s - %(name)-15s : %(message)s"
        }
    },
    "handlers":{
        "console":{
            "level": "DEBUG",
            'class': "logging.StreamHandler",
            'formatter':"standard"
        },
        "console2":{
            "level": "WARNING",
            'class': "logging.StreamHandler",
            'formatter':"standard"
        },
        "file":{
            "level": "INFO",
            'class': "logging.FileHandler",
            'filename': "logs/infos.log",
            'mode': "w"
        }
    },
    "loggers":{
        "bot":{
            "handlers": ['console'],
            "level": "INFO",
            "propogate": False
        },
        "discord":{
            "handlers": ['console2', "file"],
            "level": "INFO",
            "propogate": False
        }
    }
}

ROLE_IDS = {
    "Rainbow Six Siege" : 738831293588045889,
    "Battlefield 1" : 1221754627419017247,
}


dictConfig(LOGGING_CONFIG)