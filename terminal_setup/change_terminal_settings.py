import crocodile.toolbox as tb

"""Not to be confused:
Windows Terminal & Windows Terminal Preview
The latter is the night release version of WT.
Windows PowerShell & PowerShell.
The latter is community developed and is available on all platforms.
Lastly, powershell has a preview version as well.
"""

# Grabbing Terminal Settings file:
path = tb.os.environ["LocalAppData"]
path = tb.P(path).joinpath(r"Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json")
path.copy(append=".orig." + tb.randstr())
dat = path.readit()

# Changing start up settings:
dat["startOnUserLogin"] = True
dat["launchMode"] = "fullscreen"
dat["focusFollowMouse"] = True
dat["copyOnSelect"] = True
dat["profiles"]["defaults"]["padding"] = "0"
dat["profiles"]["defaults"]["useAcrylic"] = False

# Adjusting profiles:
profs = tb.L(dat["profiles"]["list"])

# 1- Customizing Powershell========================================================
# as opposed to Windows Powershell
pwsh = dict(name="PowerShell",
            commandline="pwsh",
            hidden=False,
            guid="{" + f"2ced56a6-632d-4fcf-910a-703d{tb.randstr(length=6, upper=False, lower=False)}e8" + "}",
            font=dict(face="CaskaydiaCove Nerd Font"),  # because oh-my-posh uses glyphs from this font.
            )
if profs.filter(lambda x: x["name"] == "PowerShell").__len__() < 1: profs.append(pwsh)
dat["defaultProfile"] = pwsh["guid"]

# Adding IPyShell if it is not there.
# py_pr = tb.copy.deepcopy(pr)  # use it as a template for the new profile.
ipyshell = dict(name="ipyshell",
                guid="{" + f"2ced56a6-632d-4fcf-910a-703d{tb.randstr(length=6, upper=False, lower=False)}e8" + "}",
                commandline="powershell.exe -Command \"conda activate ve; ipython -i -c 'import crocodile.toolbox as tb'\"",
                startingDirectory=None,  # "%USERPROFILE%",   # None
                )
# startingDirectory = None means: inheret from parent process, which will is the default, which point to /System32
# Launching a new profile with ctr+shift+2 is equivalent to: wt --profile IPyShell -d . --new-tab

if profs.filter(lambda x: x["name"] == "ipyshell").__len__() < 1: profs.append(ipyshell)

# Add Ubunto if it is not there.
ubuntu = dict(name="Ubuntu",
              commandline="wsl -d Ubuntu --cd ~",
              hidden=False,
              guid="{" + f"2ced56a6-632d-4fcf-910a-703d{tb.randstr(length=6, upper=False, lower=False)}e8" + "}")
if profs.filter(lambda x: x["name"] == "Ubuntu").__len__() < 1: profs.append(ubuntu)

# Changing order of profiles:
tmp = [
    profs.filter(lambda x: x["name"] == "PowerShell")[0],  # 1. commandline = pwsh.exe
    profs.filter(lambda x: x["name"] == "IPyShell")[0],  # 2.
    profs.filter(lambda x: x["name"] == "Ubuntu")[0],  # 3.
    profs.filter(lambda x: x["name"] == "Windows PowerShell")[0],  # 4. name =  powershell.exe
    profs.filter(lambda x: x["name"] == "Command Prompt")[0],  # 5. name = cmd.exe
    # profs.filter(lambda x: x["name"] == "Azure Cloud Shell")[0]  # 6.
]
dat["profiles"]["list"] = tmp

dat.save_json(path)
