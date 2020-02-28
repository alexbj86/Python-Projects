import paramiko

from logFinder.com.logfinder.util.LogFinderUtils import LogFinderUtils


class LogFinderLogic(object):

    def __init__(self):
        self.ip_dict = {
            'Integrazione': {'FE': '10.82.53.14', 'BE': '10.82.53.10'},
            'Collaudo': {'FE': '10.82.53.133, 10.82.53.134', 'BE': '10.82.53.135'},
            'AM': {'FE': '10.82.53.141, 10.82.53.142', 'BE': '10.82.53.136'}
        }

    def connect_to_server(self, environment, server):
        # open ssh connection
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        host = self.ip_dict.get(environment).get(server)
        url = '/home/tomcat/liferay-portal-6.1.20-ee-ga2/apache-tomcat/logs/ibk;'
        if server == 'BE':
            url = '/home/tomcat/apache-tomcat/logs/ibk;'
        logFinderUtils = LogFinderUtils()
        username = logFinderUtils.readProperties('username')[0][1]
        keyFile = logFinderUtils.readProperties('keyFile')[0][1]
        return client, host, keyFile, url, username

    def get_list_files(self, clientCode, date, environment, server):
        client, host, keyFile, url, username = self.connect_to_server(environment, server)
        multiHost = host.split(",")
        dict_file = {}
        if len(multiHost) > 1:
            for h in multiHost:
                client.connect(hostname=h.strip(), username=username, key_filename=keyFile, port='22')
                (stdin, stdout, stderr) = client.exec_command("cd " + url + " grep -l '" + clientCode + "' " + date)
                dict_file[h] = stdout.readlines()
        else:
            client.connect(hostname=host, username=username, key_filename=keyFile, port='22')
            (stdin, stdout, stderr) = client.exec_command("cd " + url + " grep -l '" + clientCode + "' " + date)
            dict_file[host] = stdout.readlines()

        # closed ssh connection
        client.close()

        return dict_file

    def download_file(self, file, ip, local_dir_name):
        print("")
        # for i in list(self.ip_dict.values()):
        #     for j in i.values():
        #         if ip.strip() == j.strip():

    # client, host, keyFile, url, username = self.connect_to_server()
    # client.connect(hostname=host.strip(), username=username, key_filename=keyFile, port='22')
    # sftp = client.open_sftp()
    # sftp.get(url+'/'+file, local_dir_name)
    # sftp.close()
    # client.close()
