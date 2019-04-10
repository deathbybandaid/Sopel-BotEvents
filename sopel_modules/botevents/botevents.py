# coding=utf8
"""Sopel-BotEvents

Sopel BotEvents is a poor mans way to create module load order dependencies
"""
from __future__ import unicode_literals, absolute_import, division, print_function

import sopel.module
from sopel.tools import stderr


def configure(config):
    pass


def setup(bot):

    stderr("Starting Module Events Logging")
    if "bot_module_events" not in bot.memory:
        bot.memory["bot_module_events"] = []


def list_bot_events(bot):
    if "bot_module_events" not in bot.memory:
        bot.memory["bot_module_events"] = []
    return bot.memory["bot_module_events"]


def check_bot_events(bot, listreq):

    if "bot_module_events" not in bot.memory:
        bot.memory["bot_module_events"] = []

    if not isinstance(listreq, list):
        listreq = [str(listreq)]

    for requirement in listreq:
        if requirement not in bot.memory["bot_module_events"]:
            return False
    return True


def set_bot_event(bot, addonreq):

    if not isinstance(addonreq, list):
        addonreq = [str(addonreq)]

    if "bot_module_events" not in bot.memory:
        bot.memory["bot_module_events"] = []

    bot.memory["bot_module_events"].extend(addonreq)
