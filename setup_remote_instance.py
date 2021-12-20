"""
This is the first file that should you should to setup a new machine once you get SSH connection to it.

"""

import crocodile.toolbox as tb

inst = [
    # notes="t2.micro",
    dict(
        hostname="ec2-13-239-0-67.ap-southeast-2.compute.amazonaws.com",
        username="ubuntu",
        ssh=tb.P.home().joinpath(r"my_private_keys\aws\instances\aws_sydney_ec2.pem"),
    ),
    # notes="t2.micro-redhat"
    dict(hostname="ec2-54-253-183-178.ap-southeast-2.compute.amazonaws.com",
         username="ec2-user",
         ssh=tb.P.home().joinpath(r"my_private_keys\aws\instances\aws_sydney_ec2.pem")
         ),

    # "Google 32GB v8 machine, valid till 20th Jan"
    dict(hostname="34.87.239.6",
         username="alex_ssh_keys",
         ssh=None, )
]


def main(idx=0):
    """Copy my_private_files and dotfiles repo over to the remote machine."""
    idx = 0
    machine = tb.Struct(inst[idx])
    client = tb.meta.SSH(hostname=machine.hostname, username=machine.username, ssh_key=machine.ssh)

    client.copy_from_here(source="~/my_private_keys", encrypt=True)
    client.copy_from_here(source="~/code/dotfiles", compress=True)
    client.copy_from_here("./setup_linux.bash", target="~")
    # client.execute("bash setup_linux.bash")  # there is interactive prompt


if __name__ == '__main__':
    pass
