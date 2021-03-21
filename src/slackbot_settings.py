import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.environ['SLACK_BOT_API_TOKEN']

DEFAULT_REPLY = "その言葉の意味を知りません"

PLUGINS = [
    'slackbot.plugins',
    'botmodule',
]