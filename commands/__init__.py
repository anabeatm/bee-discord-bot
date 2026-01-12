from .hello import setup as hello_setup
from .userinfo import setup as userinfo_setup

def setup_commands(bot):
    hello_setup(bot)
    userinfo_setup(bot)