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
    if "bot_module_events" not in bot.memory:
        stderr("[Sopel-BotEvents] Starting Module Events Logging")
        bot.memory["bot_module_events"] = {"loaded": [], "startup": []}


def list_bot_events(bot, list_type):
    if "bot_module_events" not in bot.memory:
        bot.memory["bot_module_events"] = {"loaded": [], "startup": []}
    return bot.memory["bot_module_events"][list_type]


def check_bot_events(bot, listreq):
    if "bot_module_events" not in bot.memory:
        bot.memory["bot_module_events"] = {"loaded": [], "startup": []}

    if not isinstance(listreq, list):
        listreq = [str(listreq)]

    for requirement in listreq:
        if requirement not in bot.memory["bot_module_events"]["loaded"]:
            return False
    return True


def set_bot_event(bot, addonreq):
    if "bot_module_events" not in bot.memory:
        bot.memory["bot_module_events"] = {"loaded": [], "startup": []}

    if not isinstance(addonreq, list):
        addonreq = [str(addonreq)]

    bot.memory["bot_module_events"]["loaded"].extend(addonreq)


def startup_bot_event(bot, addonreq):
    if "bot_module_events" not in bot.memory:
        bot.memory["bot_module_events"] = {"loaded": [], "startup": []}

    if not isinstance(addonreq, list):
        addonreq = [str(addonreq)]

    bot.memory["bot_module_events"]["startup"].extend(addonreq)


def check_bot_startup(bot):

    if "bot_module_events" not in bot.memory:
        bot.memory["bot_module_events"] = {"loaded": [], "startup": []}

    for startupitem in bot.memory["bot_module_events"]["startup"]:
        if startupitem not in bot.memory["bot_module_events"]["loaded"]:
            return False
    return True
