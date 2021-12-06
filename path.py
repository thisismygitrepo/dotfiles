
import crocodile.toolbox as tb


def temp_change_powershell(path, kind="append"):
    if kind == "append":
        # Append to the Path variable in the current window:
        command = fr'$env:Path += ";{path}"'
    elif kind == "prefix":
        # Prefix the Path variable in the current window:
        command = fr'$env:Path = "{path};" + $env:Path'
    elif kind == "replace":
        # Replace the Path variable in the current window (use with caution!):
        command = fr'$env:Path = "{path}"'
    else:
        raise KeyError
    return command


def permanet_change_powershell(path, which=["User", "Machine"][0]):
    backup = fr'$env:path >> {tb.P.tmpfile()}.path_backup;'
    command = fr'[Environment]::SetEnvironmentVariable("Path", $env:Path + ";{path}", "{which}")'
    return backup + command


if __name__ == '__main__':
    pass
