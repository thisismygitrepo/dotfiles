
"""

"""

import crocodile.toolbox as tb


class Env:
    class PowerShell:

        @staticmethod
        def temp_path(path, kind="append"):
            """Source: https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.2"""
            if kind == "append":  # Append to the Path variable in the current window:
                command = fr'$env:Path += ";{path}"'
            elif kind == "prefix":  # Prefix the Path variable in the current window:
                command = fr'$env:Path = "{path};" + $env:Path'
            elif kind == "replace":  # Replace the Path variable in the current window (use with caution!):
                command = fr'$env:Path = "{path}"'
            else: raise KeyError
            return command

        @staticmethod
        def permanet_path(path, which=["User", "Machine"][0]):
            backup = fr'$env:path >> {tb.P.tmpfile()}.path_backup;'
            command = fr'[Environment]::SetEnvironmentVariable("Path", $env:Path + ";{path}", "{which}")'
            return backup + command


if __name__ == '__main__':
    tb.os.system("ls")
