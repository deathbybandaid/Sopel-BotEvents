# coding=utf-8

from __future__ import unicode_literals, absolute_import, division, print_function

from sopel import module
from .botevents import *

import time


def configure(config):
    pass


def setup(bot):

    while not len(bot.channels.keys()) > 0:
        pass
    time.sleep(1)
    stderr("channels attached")

    set_bot_event(bot, "connected")
