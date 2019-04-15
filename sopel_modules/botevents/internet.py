# coding=utf-8

from __future__ import unicode_literals, absolute_import, division, print_function

from sopel import module
from sopel.tools import stderr
from .botevents import *

import socket
import threading


def setup(bot):

    threading.Thread(target=setup_thread, args=(bot,)).start()


def setup_thread(bot):
    while not internet(host="8.8.8.8", port=53, timeout=3):
        pass
    while "Sopel-BotEvents" not in bot.memory:
        pass
    set_bot_event(bot, "internet")


def internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as e:
        return False
