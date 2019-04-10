# coding=utf-8

from __future__ import unicode_literals, absolute_import, division, print_function

from sopel import module
from sopel.tools import stderr

from .botevents import *


def configure(config):
    pass


def setup(bot):

    startup_bot_event(bot, 'startup_start')
    while len(list_bot_events(bot, "startup")) > 1:
        pass

    set_bot_event(bot, "startup_complete")
    stderr("Module Events Logging Complete")
