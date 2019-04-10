# coding=utf-8

from __future__ import unicode_literals, absolute_import, division, print_function

from sopel import module
from sopel.tools import stderr

from .botevents import *


@module.event('001')
@module.rule('.*')
def bot_startup_complete(bot, trigger):

    while not check_bot_startup(bot):
        pass

    set_bot_event(bot, "startup_complete")
    stderr("[Sopel-BotEvents] Module Events Logging Complete")
