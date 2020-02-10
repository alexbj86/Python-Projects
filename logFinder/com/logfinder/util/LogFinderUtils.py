from configparser import ConfigParser


class LogFinderUtils(object):

    def readProperties(self, prop):
        config = ConfigParser()
       #with open(r'../../resources/config.properties') as f:
        item = config.read('../../resources/config.properties', encoding='utf-8-sig')
        env = config.items(prop)
        return env