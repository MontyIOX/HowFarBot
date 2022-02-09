import logging
import sys

import telegram.ext as tg

from telegram import Update
from telegram.ext import CallbackContext

from HowFarBot.config import BOT_TOKEN, E_MAIL


# Enable logging
logging.basicConfig(
    #filename="./howfarbot.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
LOGGER = logging.getLogger(__name__)

# Check python Version
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error("You MUST have a python version of at least 3.6! Bot quitting.")
    quit(1)

if not E_MAIL:
    LOGGER.warning("No Email provided for Nominatim API, it is recommended to add one.")

# Create updater
updater = tg.Updater(BOT_TOKEN, use_context=True)
# Create dispatcher
dispatcher = updater.dispatcher
bot = dispatcher.bot