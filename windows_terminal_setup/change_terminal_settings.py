
import crocodile.toolbox as tb
import crocodile.environment as env
from uuid import uuid4

"""
Not to be confused:
* Windows Terminal & Windows Terminal Preview: The latter is the night release version of WT.
* Windows PowerShell & PowerShell: The latter is community developed and is available on all platforms.
* Windows Powershell comes preinstalled with the system, Powershell must be installed separately.
* Lastly, powershell has a preview version as well.

All settings are available on GitHub: https://aka.ms/terminal-profiles-schema
"""


assert env.system == 'Windows', 'This script is only for Windows.'


class TerminalSettings(object):
    def __init__(self):
        # Grabbing Terminal Settings file:
        self.path = env.LocalAppData.joinpath(r"Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json")
        self.path.copy(append=".orig." + tb.randstr())
        self.dat = self.path.readit()
        self.profs = tb.L(self.dat["profiles"]["list"])

    def save_terminal_settings(self):
        self.dat["profiles"]["list"] = list(self.profs)
        self.dat.save_json(self.path)

    # ========================= Terminal Settings =========================================
    def update_default_settings(self):
        # Changing start up settings:
        self.dat["startOnUserLogin"] = True
        self.dat["launchMode"] = "fullscreen"
        self.dat["theme"] = "system"
        self.dat["focusFollowMouse"] = True
        self.dat["copyOnSelect"] = True
        self.dat["profiles"]["defaults"]["padding"] = "0"
        self.dat["profiles"]["defaults"]["useAcrylic"] = False

    # 1- Customizing Powershell========================================================
    # as opposed to Windows Powershell
    def customize_powershell(self, nerd_font=False):
        pwsh = dict(name="PowerShell",
                    commandline="pwsh",
                    hidden=False,
                    # guid="{" + str(uuid4()) + "}",  # WT doesn't accept any GUID to identify pwsh
                    startingDirectory="%USERPROFILE%",  # "%USERPROFILE%",   # None: inherent from parent process.
                    )
        if nerd_font: pwsh["font"] = dict(face="CaskaydiaCove Nerd Font")  # because oh-my-posh uses glyphs from this font.
        for idx, item in enumerate(self.profs):
            if item["name"] == "PowerShell":
                self.profs[idx].update(pwsh)
                break
        else: print(f"Couldn't customize powershell because profile not found, try to install it first.")

    def make_powershell_default_profile(self):
        for profile in self.profs:
            if profile["name"] == "PowerShell":
                self.dat["defaultProfile"] = profile["guid"]
                print("Powershell is now the default profile.")
                break
        else: print("Powershell profile was not found in the list of profile and therefore was not made the deafult.")

    def add_croshell(self):
        # Adding croshell if it is not there.
        # py_pr = tb.copy.deepcopy(pr)  # use it as a template for the new profile.
        croshell = dict(name="croshell",
                        guid="{" + str(uuid4()) + "}",
                        # commandline=f"powershell.exe -Command \"{activate} ipython -i -c 'from crocodile.toolbox import *'\"",
                        commandline=f'powershell.exe -Command "~/code/dotfiles/scripts/windows/croshell.ps1"',
                        startingDirectory="%USERPROFILE%",  # "%USERPROFILE%",   # None: inherent from parent process.
                        )
        # startingDirectory = None means: inheret from parent process, which will is the default, which point to /System32
        # Launching a new profile with ctr+shift+2 is equivalent to: wt --profile croshell -d . --new-tab
        for profile in self.profs:
            if profile["name"] == "croshell":
                profile.update(croshell)
                break
        else: self.profs.append(croshell)

    def add_ubuntu(self):
        # Add Ubunto if it is not there.
        ubuntu = dict(name="Ubuntu",
                      commandline="wsl -d Ubuntu --cd ~",
                      hidden=False,
                      guid="{" + str(uuid4()) + "}",
                      startingDirectory="%USERPROFILE%",  # "%USERPROFILE%",   # None: inherent from parent process.
                      )
        if self.profs.filter(lambda x: x["name"] == "Ubuntu").__len__() < 1: self.profs.append(ubuntu)

    def standardize_profiles_order(self):
        # Changing order of profiles:
        others = []
        pwsh = croshell = ubuntu = wpwsh = cmd = azure = None
        for profile in self.profs:
            name = profile["name"]
            if name == "PowerShell": pwsh = profile
            elif name == "croshell": croshell = profile
            elif name == "Ubuntu": ubuntu = profile
            elif name == "Windows PowerShell": wpwsh = profile
            elif name == "Command Prompt": cmd = profile
            elif name == "Azure Cloud Shell": azure = profile
            else: others.append(profile)
        self.profs = [item for item in [pwsh, croshell, ubuntu, wpwsh, cmd, azure] + others if item is not None]


def main():
    ts = TerminalSettings()
    ts.update_default_settings()
    ts.customize_powershell()
    ts.make_powershell_default_profile()
    ts.add_croshell()
    ts.add_ubuntu()
    ts.standardize_profiles_order()
    ts.save_terminal_settings()


if __name__ == '__main__':
    pass
