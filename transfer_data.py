
import numpy as np
import matplotlib.pyplot as plt
import crocodile.toolbox as tb
import paramiko


class SSH(object):
    def __init__(self, hostname, username, ssh_key=None):
        self.ssh_key = ssh_key
        self.ssh = paramiko.SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.hostname = hostname
        self.username = username
        self.ssh.connect(hostname=hostname,
                         username=username,
                         port=22, key_filename=self.ssh_key.string)

    def copy_from_here(self, source, target=None):
        if target is None:
            # target = source  # works if source is relative.
            target = tb.P(source).parent.string  # works if source is relative.

        command = fr"""scp -r -i {self.ssh_key} {source} {self.username}@{self.hostname}:{target} """
        print(f"Executing command: {command}")
        tb.os.system(command)

    def copy_to_here(self, source, target=None):
        pass

    def execute(self, command):
        res = tb.L(self.ssh.exec_command(command))
        res = res.apply(lambda x: x.read().decode("utf-8"))
        res = tb.Struct(stdin=res[0], stdout=res[1], stderr=res[2])
        for key, val in res:
            print(key, f"\n{'='*30}\n", val)


if __name__ == '__main__':
    pass
