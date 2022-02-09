from HowFarBot import *
from HowFarBot.modules import ALL_MODULES
import importlib

for module_name in ALL_MODULES:
    importlib.import_module("HowFarBot.modules." + module_name)

if __name__ == '__main__':
    updater.start_polling()
    LOGGER.info("Bot running.")

    updater.idle()