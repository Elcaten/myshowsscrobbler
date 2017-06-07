import os
import appdirs
from configparser import ConfigParser

class Settings:
    '''Application settings manager'''
    def __init__(self):
        settingsfolder = appdirs.user_data_dir("myshowsscrobbler", "myshowsscrobbler")
        self.__settingsfilepath__ = os.path.join(settingsfolder, "settings.ini")
        if not os.path.exists(settingsfolder):
            os.makedirs(self.__settingsfilepath__, exist_ok=True)
        if not os.path.exists(self.__settingsfilepath__):
            with open(self.__settingsfilepath__, "w") as configfile:
                configfile.write("[SETTINGS]")
        self.config = ConfigParser()

    def get(self, name):
        '''Gets application setting'''
        self.config.read(self.__settingsfilepath__)
        return self.config.get("SETTINGS", name)

    def set(self, name, value):
        '''Sets application setting'''
        self.config.read(self.__settingsfilepath__)
        self.config.set("SETTINGS", name, value)
        with open(self.__settingsfilepath__, 'w') as configfile:
            self.config.write(configfile)

