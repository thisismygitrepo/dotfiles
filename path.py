
"""
Manage Windows enviroment path from Python.

Linux tips: https://superuser.com/questions/176783/what-is-the-difference-between-executing-a-bash-script-vs-sourcing-it
Windows tips https://devblogs.microsoft.com/scripting/understanding-the-six-powershell-profiles/
http://www.p-nand-q.com/download/gtools/pathed.html

linux:
a=b for one program
export a=2  for one shell session and its child processes (Win set a=1)
"""

import crocodile.toolbox as tb
# see: `gci env:` for all enviroment variables OR (set) (linux printenv)
# see: `$env:Path` for Path variables.


def temp_change_powershell(path, kind="append"):
    if kind == "append":  # Append to the Path variable in the current window:
        command = fr'$env:Path += ";{path}"'
    elif kind == "prefix":  # Prefix the Path variable in the current window:
        command = fr'$env:Path = "{path};" + $env:Path'
    elif kind == "replace":  # Replace the Path variable in the current window (use with caution!):
        command = fr'$env:Path = "{path}"'
    else: raise KeyError
    return command


def permanet_change_powershell(path, which=["User", "Machine"][0]):
    backup = fr'$env:path >> {tb.P.tmpfile()}.path_backup;'
    command = fr'[Environment]::SetEnvironmentVariable("Path", $env:Path + ";{path}", "{which}")'
    return backup + command


if __name__ == '__main__':
    tb.os.system("ls")
