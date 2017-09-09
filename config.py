import logging
import os

BOT_LOG_LEVEL = logging.DEBUG
BASE_DIR = "/app"

BACKEND = 'Telgram'
BOT_EXTRA_BACKEND_DIR = "/app/backend"
print(BOT_EXTRA_BACKEND_DIR)

bot_token = os.getenv('bot_token')

BOT_IDENTITY = {
        # Required
        'token': bot_token,
}

CHATROOM_PRESENCE = ()
BOT_PREFIX = '/'

# The location where all of Err's data should be stored. Make sure to set
# this to a directory that is writable by the user running the bot.
BOT_DATA_DIR = "/tmp"

### Repos and plugins config.

# Set this to change from where errbot gets its installable plugin list.
# By default it gets the index from errbot.io which is a file generated by tools/plugin-gen.py.
# BOT_PLUGIN_INDEXES = 'http://version.errbot.io/repos.json'
#
# You can also specify a local file:
# BOT_PLUGIN_INDEXES = 'tools/repos.json'
#
# Or a list. note: if some plugins exists in 2 lists, only the first hit will be taken into account.
# BOT_PLUGIN_INDEXES = ('/data/repos.json', 'https://my.private.tld/errbot/myrepos.json')

# Set this to a directory on your system where you want to load extra
# plugins from, which is useful mostly if you want to develop a plugin
# locally before publishing it. Note that you can specify only a single
# directory, however you are free to create subdirectories with multiple
# plugins inside this directory.
BOT_EXTRA_PLUGIN_DIR = "/app/plugins"
print(BOT_EXTRA_PLUGIN_DIR)

# The location of the log file. If you set this to None, then logging will
# happen to console only.
BOT_LOG_FILE = None

##########################################################################
# Account and chatroom (MUC) configuration                               #
##########################################################################


# Set the admins of your bot. Only these users will have access
# to the admin-only commands.
#
# Unix-style glob patterns are supported, so 'gbin@localhost'
# would be considered an admin if setting '*@localhost'.

