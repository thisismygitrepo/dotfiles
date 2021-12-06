

import crocodile.toolbox as tb
"""Not to be confused:
Windows Terminal & Windows Terminal Preview
The latter is the night release version of WT.
Windows PowerShell & PowerShell.
The latter is community developed and is available on all platforms.
"""

path = tb.Terminal().run_command("$env:LocalAppData").stdout[:-1]
path = tb.P(path).joinpath(r"Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json")
dat = path.readit()

dat["startOnUserLogin"] = True
dat["launchMode"] = "fullscreen"
dat["focusFollowMouse"] = True
dat["copyOnSelect"] = False
dat["profiles"]["defaults"]["padding"] = "0"
dat["profiles"]["defaults"]["useAcrylic"] = True
profs = tb.L(dat["profiles"]["list"])

# Customizing Powershell
pr = profs.filter(lambda x: x["name"] == "PowerShell")[0]
# profs.list.remove(pr)  # to change its location to the top
dat["defaultProfile"] = pr["guid"]
pr["font"]["face"] = "CaskaydiaCove Nerd Font Mono"

# Adding IPythonShell
py_pr = tb.copy.deepcopy(pr)  # use it as a template for the new profile.
py_pr["name"] = "IPythonShell"
py_pr["guid"] = "{" + f"2ced56a6-632d-4fcf-910a-703d{tb.randstr(length=6, uppercase=False, lowercase=False)}e8" + "}"
# pr["startingDirectory"] = "%CURRENTPATH%"  # as opposed to "%USERPROFILE%"
py_pr["commandline"] = "powershell.exe -Command \"conda activate ve; ipython -i -c 'import crocodile.toolbox as tb'\""
profs.append(py_pr)

dat.save_json(path)
