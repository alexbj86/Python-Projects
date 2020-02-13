import os
from configparser import ConfigParser


class LogFinderUtils(object):

    def readProperties(self, prop):
        config = ConfigParser()
        path = os.path.join(os.getcwd(), 'python/logfinder/resources/config.properties')
        config.read(path, encoding='utf-8-sig')
        env = config.items(prop)
        return env
