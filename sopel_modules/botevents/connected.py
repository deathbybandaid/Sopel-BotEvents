# coding=utf-8

from __future__ import unicode_literals, absolute_import, division, print_function

from sopel import module
from .botevents import *

import time


@sopel.module.event('001')
@sopel.module.rule('.*')
@sopel.module.thread(True)
def bot_startup_connection(bot):

    startup_bot_event(bot, "connected")

    while not bot.users or not bot.users.contains(bot.nick):
        pass

    while not len(bot.channels.keys()) > 0:
        pass
    time.sleep(1)
    stderr("[Sopel-BotEvents] channels attached")

    set_bot_event(bot, "connected")
