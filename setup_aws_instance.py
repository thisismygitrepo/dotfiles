
import crocodile.toolbox as tb
import transfer_data as td


inst = [dict(
    hostname="ec2-13-239-0-67.ap-southeast-2.compute.amazonaws.com",
    username="ubuntu",
    notes="t2.micro",
),
    dict(hostname="ec2-user@ec2-54-253-183-178.ap-southeast-2.compute.amazonaws.com",
         username="",
         notes="t2.micro-redhat")
]


def main(idx=0):
    """Copy my_private_files and dotfiles repo over to the remote machine."""
    idx = 0
    machine = tb.Struct(inst[idx])
    ssh = tb.P.home().joinpath(r"my_private_keys\aws\instances\aws_sydney_ec2.pem")
    client = td.SSH(hostname=machine.hostname, username=machine.username, ssh_key=ssh)

    client.copy_from_here(source=tb.P.home().joinpath(r"my_private_keys"), target=r"~")

    client.execute("mkdir code")
    zipped = tb.P.home().joinpath(r"code/dotfiles").zip()
    client.copy_from_here(zipped, "~/code")
    client.execute("cd ~/code; sudo apt install unzip; unzip dotfiles.zip; rm dotfiles.zip")
    zipped.delete(are_you_sure=True)

    client.copy_from_here(tb.P.cwd().joinpath("setup_linux.bash"), target="~")
    # client.execute("bash setup_linux.bash")  # there is interactive prompt


if __name__ == '__main__':
    pass
