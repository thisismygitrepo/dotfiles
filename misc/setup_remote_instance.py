"""
This is the first file that should you should to setup a new machine once you get SSH connection to it.

"""

import crocodile.toolbox as tb


def main():
    """Copy my_private_files and dotfiles repo over to the remote machine."""
    machine = tb.Struct(hostname="flask-server", username="alex", ssh_key=None)
    client = tb.meta.SSH(hostname=machine.hostname, username=machine.username, ssh_key=machine.ssh)
    client.copy_from_here(source="~/code/dotfiles", zip_n_encrypt=True)
    client.copy_from_here("./setup_linux.bash", target="~")
    # client.execute("bash setup_linux.bash")  # there is interactive prompt


if __name__ == '__main__':
    pass
