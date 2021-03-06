
"""
This script Takes away all config files from the computer, place them in one directory
`dotfiles`, and create symlinks to those files from thier original locations.
"""
import crocodile.toolbox as tb
from crocodile.environment import DotFiles, get_shell_profiles, system, AppData, exe


def symlink(this: tb.P, to_this: tb.P, overwrite=True):
    """helper function. creates a symlink from `this` to `to_this`.
    What can go wrong?
    depending on this and to_this existence, one will be prioretized depending on overwrite value.
    True means this will potentially be overwritten
    False means to_this will potentially be overwittten."""
    if this.is_symlink(): this.delete(sure=True)  # delete if it exists as symblic link, not a concrete path.
    if this.exists():  # this is a problem. It will be resolved via `overwrite`
        if overwrite is True:  # it *can* be deleted, but let's look at target first.
            if to_this.exists(): this.delete(sure=True)  # this exists, to_this as well. to_this is prioritized.
            else: this.move(path=to_this)  # this exists, to_this doesn't. to_this is prioritized.
        elif overwrite is False:  # don't sacrefice this, sacrefice to_this.
            if to_this.exists(): this.move(path=to_this, overwrite=True)  # this exists, to_this as well, this is prioritized.   # now we are readly to make the link
            else: this.move(path=to_this)  # this exists, to_this doesn't, this is prioritized.
    else:  # this doesn't exist.
        if not to_this.exists(): to_this.touch()  # we have to touch it (file) or create it (folder)
    try: tb.P(this).symlink_to(to_this, verbose=True, overwrite=True)
    except Exception as ex: print(f"Failed at linking {this} ==> {to_this}.\nReason: {ex}")


def link_ssh(overwrite=True):
    path = tb.P.home().joinpath(".ssh")
    target = DotFiles.joinpath(".ssh")
    for item in target.search("*"):
        symlink(path.joinpath(item.name), item, overwrite=overwrite)


def link_aws(overwrite=True):
    path = tb.P.home().joinpath(".aws")
    target = DotFiles.joinpath("aws/.aws")
    for item in target.search("*"): symlink(path.joinpath(item.name), item, overwrite=overwrite)


def link_gitconfig(overwrite=True):
    for config in [".gitconfig"]: symlink(tb.P.home().joinpath(config), DotFiles.joinpath(f"settings/{config}"), overwrite=overwrite)


def link_pypi_creds(overwrite=True):
    symlink(tb.P.home().joinpath(".pypirc"), DotFiles.joinpath("creds/.pypirc"), overwrite=overwrite)


def link_powershell(overwrite=True):
    if system == "Linux": return None
    for profile_name, profile_path in get_shell_profiles(shell="pwsh").items():
        target = DotFiles.joinpath(f"shells/powershell/{profile_name}/{profile_path.name}")
        symlink(profile_path, target, overwrite=overwrite)


def link_windows_powershell(overwrite=True):
    if system == "Linux": return None
    for profile_name, profile_path in get_shell_profiles(shell="powershell").items():
        target = DotFiles.joinpath(f"shells/powershell/{profile_name}/{profile_path.name}")
        symlink(profile_path, target, overwrite=overwrite)


def link_ipython(overwrite=True):
    path = tb.P.home().joinpath(".ipython/profile_default/ipython_config.py")
    target = DotFiles.joinpath(f"shells/ipython/{path.name}")
    symlink(path, target, overwrite=overwrite)


def link_autostart(overwrite=True):
    file = AppData.joinpath("Microsoft/Windows/Start Menu/Programs/Startup").joinpath("startup_file.cmd")
    symlink(file, tb.P(r"~/code/dotfiles/jobs/windows/startup_file.cmd").expanduser(), overwrite=overwrite)


folder = {"Windows": "windows", "Linux": "linux"}[system]


def link_scripts(overwrite=True):
    symlink(tb.P.home().joinpath("scripts"), tb.P.home().joinpath(f"code/dotfiles/scripts/{folder}"), overwrite=overwrite)


def add_scripts_to_path():  # options to make croshell available: define in terminal profile, add to Path, or add to some folder that is already in path, e.g. env.WindowsApps or Scripts folder where python.exe resides.
    assert system == "Windows"
    tb.P.home().joinpath(f"code/dotfiles/scripts/{folder}/croshell.ps1").symlink_from(folder=exe.parent)  # thus, whenever ve is activated, croshell is available.
    addition = f'\n$env:Path += ";{tb.P.home().joinpath("code/dotfiles/scripts/windows")}"'
    tb.Terminal().run("$profile", shell="pwsh").as_path.modify_text(addition, addition, notfound_append=True)


def main():
    """create symlinks in default locations to `dotfiles` contents"""
    overwrite = True
    link_gitconfig(overwrite=overwrite)
    link_pypi_creds(overwrite=overwrite)
    link_ipython(overwrite=overwrite)
    link_powershell(overwrite=overwrite)
    link_windows_powershell(overwrite=overwrite)
    link_scripts(overwrite=overwrite)
    link_aws(overwrite=overwrite)
    link_ssh(overwrite=overwrite)
    # link_autostart(overwrite=overwrite)


if __name__ == '__main__':
    pass
