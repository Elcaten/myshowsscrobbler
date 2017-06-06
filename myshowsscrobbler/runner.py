import os
import appdirs

settingsfolder = appdirs.user_data_dir(__name__, __name__)
settingsfile = os.path.join(settingsfolder, "settings.json")