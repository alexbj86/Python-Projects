import paramiko

from logFinder.com.logfinder.util.LogFinderUtils import LogFinderUtils


class LogFinderLogic(object):

    def __init__(self):
        self.ip_dict = {
            'Integrazione': {'FE': '10.82.53.14', 'BE': '10.82.53.10'},
            'Collaudo': {'FE': '10.82.53.133, 10.82.53.134', 'BE': '10.82.53.135'},
            'AM': {'FE': '10.82.53.141, 10.82.53.142', 'BE': '10.82.53.136'}
        }

    def connect_to_server(self, environment, fe_be):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            host = self.ip_dict.get(environment).get(fe_be)
            logFinderUtils = LogFinderUtils()
            username = logFinderUtils.readProperties('username')[0][1]
            keyFile = logFinderUtils.readProperties('keyFile')[0][1]
            client.connect(hostname=host, username=username, key_filename=keyFile, port='22')
            print("Connesso")
        except Exception as e:
            print(e)
