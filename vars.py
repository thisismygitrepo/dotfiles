
"""
Variables:
There exist enviroment variables and then there are shell variables. Distinciton in mind is due.
A shell variable is abailable in that shell session and other programs are not aware of it.
An enviroment variable is abailable to all programs running on the machine.

Shell variables can live for the lifetime of the shell itself, unless they are reloaded again from
the configuration script. Enviroment variables live forever, unless explicitly removed.

Enviroment variables can only be strings. Shell variables can be anything.

Path, is a special enviroment variable. It contains directories that will be searched when looking
for executables. If you have an executable, it is not recommended to put its path as an inviroment variable.
Otherwise, you need to give it a name and then explicitly launch it with, .e.g `start $julia`
The correct way to do it is to add its directory to its Path.

Acecss enviroemtn variable:
    Linux: `env`
    Windows: dir env: OR gci env:  where both gci and dir are aliases in PS for Get-ChildItem

Thus, PATH, being special, but not so much different from any other enviroment variables is acessed this way:
    Linxu: $PATH (in linux, there is no distinction between enviroment and shell variable access, both use $name)
    Windows: $env:Path (Windows separates enviroment variables from shell by prefix $env:name vs $name )

PAckage that I did not realize whats the point of them
https://github.com/theskumar/python-dotenv
https://pypi.org/project/python-decouple/
https://github.com/sloria/environs

"""

import crocodile.toolbox as tb
import platform


machine = platform.system()


class ShellVar:
    @staticmethod
    def set(key, val):
        if machine == "Windows":
            return f"set {key} {val}"
        elif machine == "Linux":
            return f"{key} = {val}"

    @staticmethod
    def get(key):
        return f"${key}"  # works in powershell and bash
    # in windows cmd `%key%`


class EnvVar:
    @staticmethod
    def set(key, val):
        if machine == "Windows":
            return f"setx {key} {val}"  # WARNING: setx limits val to 1024q
        elif machine == "Linux":
            return f"export {key} = {val}"  # this is shell command. in csh: `setenv key val`
        else:
            raise NotImplementedError

    @staticmethod
    def get(key):
        return f"${key}"  # works in powershell and bash
    # in windows cmd `%key%`


class Env:
    @staticmethod
    def temp_path(path, kind="append"):
        if machine == "Windows":
            """Source: https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.2"""
            if kind == "append":  # Append to the Path variable in the current window:
                command = fr'$env:Path += ";{path}"'
            elif kind == "prefix":  # Prefix the Path variable in the current window:
                command = fr'$env:Path = "{path};" + $env:Path'
            elif kind == "replace":  # Replace the Path variable in the current window (use with caution!):
                command = fr'$env:Path = "{path}"'
            else: raise KeyError
            return command
        else: return f'export PATH="{path}:$PATH"'

    @staticmethod
    def permanet_path(path, which=["User", "Machine"][0]):
        if machine == "Windows":
            # AVOID THIS AND OPT TO SAVE IT IN $profile.
            backup = fr'$env:path >> {tb.P.tmpfile()}.path_backup;'
            command = fr'[Environment]::SetEnvironmentVariable("Path", $env:Path + ";{path}", "{which}")'
            return backup + command

        else:
            tb.P.home().joinpath(".bashrc").append_text(f"export PATH='{path}:$PATH'")


if __name__ == '__main__':
    tb.os.system("ls")
