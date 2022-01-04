
import crocodile.toolbox as tb
from uuid import uuid4

"""
Not to be confused:
Windows Terminal & Windows Terminal Preview
The latter is the night release version of WT.
Windows PowerShell & PowerShell.
The latter is community developed and is available on all platforms.
Lastly, powershell has a preview version as well.
"""


def read_terminal_sttings():
    # Grabbing Terminal Settings file:
    path = tb.os.environ["LocalAppData"]
    path = tb.P(path).joinpath(r"Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json")
    path.copy(append=".orig." + tb.randstr())
    dat = path.readit()
    profs = tb.L(dat["profiles"]["list"])
    return path, dat, profs


def update_default_settings(dat):
    # Changing start up settings:
    dat["startOnUserLogin"] = True
    dat["launchMode"] = "fullscreen"
    dat["focusFollowMouse"] = True
    dat["copyOnSelect"] = True
    dat["profiles"]["defaults"]["padding"] = "0"
    dat["profiles"]["defaults"]["useAcrylic"] = False


def customize_powershell(profs, dat):
    # 1- Customizing Powershell========================================================
    # as opposed to Windows Powershell
    pwsh = dict(name="PowerShell",
                commandline="pwsh",
                hidden=False,
                guid="{" + str(uuid4()) + "}",
                font=dict(face="CaskaydiaCove Nerd Font"),  # because oh-my-posh uses glyphs from this font.
                )
    if (res := profs.filter(lambda x: x["name"] == "PowerShell")).__len__() < 1:
        profs.append(pwsh)
    else:
        res[0].update(pwsh)
    dat["defaultProfile"] = pwsh["guid"]


def add_ipyshell(profs):
    # Adding ipyshell if it is not there.
    # py_pr = tb.copy.deepcopy(pr)  # use it as a template for the new profile.
    activate = input("How do you activate python on this machine from Powershell? "
                     "ex1: conda activate ve; "
                     "ex2: ~/envs/ve/Scripts/Activate.ps1\n")
    ipyshell = dict(name="ipyshell",
                    guid="{" + str(uuid4()) + "}",

                    commandline=f"powershell.exe -Command \"{activate}ipython -i -c 'from crocodile.toolbox import *'\"",
                    startingDirectory=None,  # "%USERPROFILE%",   # None
                    )
    # startingDirectory = None means: inheret from parent process, which will is the default, which point to /System32
    # Launching a new profile with ctr+shift+2 is equivalent to: wt --profile ipyshell -d . --new-tab
    if profs.filter(lambda x: x["name"] == "ipyshell").__len__() < 1: profs.append(ipyshell)


def add_ubuntu(profs):
    # Add Ubunto if it is not there.
    ubuntu = dict(name="Ubuntu",
                  commandline="wsl -d Ubuntu --cd ~",
                  hidden=False,
                  guid="{" + str(uuid4()) + "}")
    if profs.filter(lambda x: x["name"] == "Ubuntu").__len__() < 1: profs.append(ubuntu)


def standardize_profiles_order(profs):
    # Changing order of profiles:
    tmp = [
        profs.filter(lambda x: x["name"] == "PowerShell")[0],  # 1. commandline = pwsh.exe
        profs.filter(lambda x: x["name"] == "ipyshell")[0],  # 2.
        profs.filter(lambda x: x["name"] == "Ubuntu")[0],  # 3.
        profs.filter(lambda x: x["name"] == "Windows PowerShell")[0],  # 4. name =  powershell.exe
        profs.filter(lambda x: x["name"] == "Command Prompt")[0],  # 5. name = cmd.exe
        # profs.filter(lambda x: x["name"] == "Azure Cloud Shell")[0]  # 6.
    ]
    return tmp


def main():
    path, dat, profs = read_terminal_sttings()
    update_default_settings(dat)
    customize_powershell(profs, dat)
    add_ipyshell(profs)
    add_ubuntu(profs)
    standardize_profiles_order(profs)
    dat["defaultProfile"] = profs.filter(lambda x: x["name"] == "PowerShell")[0]["guid"]
    dat["profiles"]["list"] = standardize_profiles_order(profs)
    dat.save_json(path)


if __name__ == '__main__':
    pass
