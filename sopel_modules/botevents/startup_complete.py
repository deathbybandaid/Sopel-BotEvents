# coding=utf-8

from __future__ import unicode_literals, absolute_import, division, print_function

from sopel import module
from .botevents import *


def configure(config):
    pass


def setup(bot):

    while not check_bot_events(bot, bot.memory["bot_module_events"]["registered"]):
        pass

    set_bot_event(bot, "startup_complete")
    stderr("Module Events Logging Complete")
