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
    if "Sopel-BotEvents" not in bot.memory:
        stderr("[Sopel-BotEvents] Starting Module Events Logging")
        bot.memory["Sopel-BotEvents"] = {"loaded": [], "startup": []}


def list_bot_events(bot, list_type):
    return bot.memory["Sopel-BotEvents"][list_type]


def check_bot_events(bot, listreq):
    if not isinstance(listreq, list):
        listreq = [str(listreq)]
    for requirement in listreq:
        if requirement not in bot.memory["Sopel-BotEvents"]["loaded"]:
            return False
    return True


def set_bot_event(bot, addonreq):
    if not isinstance(addonreq, list):
        addonreq = [str(addonreq)]

    bot.memory["Sopel-BotEvents"]["loaded"].extend(addonreq)


def startup_bot_event(bot, addonreq):
    if not isinstance(addonreq, list):
        addonreq = [str(addonreq)]

    bot.memory["Sopel-BotEvents"]["startup"].extend(addonreq)


def check_bot_startup(bot):
    for startupitem in bot.memory["Sopel-BotEvents"]["startup"]:
        if startupitem not in bot.memory["Sopel-BotEvents"]["loaded"]:
            return False
    return True
