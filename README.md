# Sopel-BotEvents

Sopel BotEvents is a poor mans way to create module load order dependencies

# This code is bad, and the author doesn't feel bad
Use at your own risk. Problems are not my fault™.

# Installation
````
git clone https://github.com/deathbybandaid/Sopel-BotEvents.git
cd Sopel-BotEvents
pip3 install .
````

# Reason behind the creation of this

Let's say you have 3 modules, module_a module_b and module_c

You want them all to run at bot startup. Typically this can be achieved with:

````
def setup(bot)
````

This method works great, if your setup procedure doesn't rely on the bot being connected to at least one channel on a server.
Your startup module might even need to use `bot.say`, which is not available before connection.

You then look into IRC events, and the closest one you can find to "bot startup" is event 001.


````
@sopel.module.event('001')
@sopel.module.rule('.*')
def module_a(bot, trigger):
````

You then begin to look at making your bot say a startup message, utilizing

````
for channel in bot.channels.keys():
  bot.say(message, channel)
````

But WAIT - bot.channels.keys() throws an error, as it's an empty list, so you find a solution

````
while not len(bot.channels.keys()) > 0:
  pass
time.sleep(1)
````

This alone is a perfectly good solution.

But what if you have multiple modules relying on this "connection" status?

What if you need your modules to wait for another module to be loaded?

If module_a relies on module_c and module_b relies on both a and c, you may need a system to keep them from running at the same time.

NOTE: obviously usage of this to make `a` rely on `b` and `b` rely on `a` will cause things to never load. That's called circular referencing, and only monsters do that.

NOTE: This only works on modules that utilize this framework. Obviously.


# Basic Usage

To make your module part of what qualifies as a complete startup, add to the top of your event,

````
startup_bot_event(bot, "mymodule")
````

To set your module as being loaded, place at the end of the function

````
set_bot_event(bot, "mymodule")
````

To make your module rely on other modules using this framework

````
while not check_bot_events(bot, ["module_b", "module_c"]):
      pass
````

The above line can also include some built in functionality such as:

`connected` The bot is in at least one channel

`startup_complete` all modules that registered that they should qualify for a complete startup are loaded


# Usage for a simple startup message when all tasks are loaded

````
#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division

# sopel imports
import sopel.module

from sopel_modules.botevents.botevents import *


@sopel.module.event('001')
@sopel.module.rule('.*')
@sopel.module.thread(True)
def bot_startup_dialogue(bot, trigger):

    while not check_bot_events(bot, ["startup_complete"]):
        pass

    for channel in bot.channels.keys():
      bot.say(bot.nick + " is online!", channel)
````
