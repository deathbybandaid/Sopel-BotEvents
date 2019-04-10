# coding=utf-8

from __future__ import unicode_literals, absolute_import, division, print_function

from sopel import module
from .botevents import *

import time


@module.event('001')
@module.rule('.*')
@module.thread(True)
def bot_startup_connected(bot, trigger):

    if check_bot_events(bot, ["connected"]):
        return
    startup_bot_event(bot, "connected")

    while not len(bot.channels.keys()) > 0:
        pass
    time.sleep(1)
    stderr("channels attached")

    set_bot_event(bot, "connected")
