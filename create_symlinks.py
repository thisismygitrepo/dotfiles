
"""
This script Takes away all config files from the computer, place them in one directory
`dotfiles`, and create symlinks to those files from thier original locations.
"""
import crocodile.toolbox as tb
import platform

dat = tb.P.home().joinpath("dotfiles")
tm = tb.Terminal()
# logger = tb.Log(file=False)


def symlink(this: tb.P, to_this: tb.P, overwrite=True):
    """helper function. creates a symlink from `this` to `to_this`.
    What can go wrong?
    depending on this and to_this existence, one will be prioretized depending on overwrite value.
    True means this will potentially be overwritten
    False means to_this will potentially be overwittten."""
    if this.is_symlink(): this.delete(sure=True)  # delete if it exists as symblic link, not a concrete path.

    if this.exists():  # this is a problem. It will be resolved via `overwrite`
        if overwrite is True:  # it *can* be deleted, but let's look at target first.
            if to_this.exists():  # this exists, to_this as well. to_this is prioritized.
                this.delete(sure=True)
            else:  # this exists, to_this doesn't. to_this is prioritized.
                this.move(path=to_this)
        elif overwrite is False:  # don't sacrefice this, sacrefice to_this.
            if to_this.exists():  # this exists, to_this as well, this is prioritized.
                this.move(path=to_this, overwrite=True)  # now we are readly to make the link
            else:  # this exists, to_this doesn't, this is prioritized.
                this.move(path=to_this)
    else:  # this doesn't exist.
        if not to_this.exists():  # we have to touch it (file) or create it (folder)
            to_this.touch()

    try:
        tb.P(this).symlink_to(to_this, verbose=True, overwrite=True)
    except Exception as ex:
        print(f"Failed at linking {this} ==> {to_this}.\nReason: {ex}")


def link_ssh(overwrite=True):
    path = tb.P.home().joinpath(".ssh")
    target = dat.joinpath(".ssh")
    for item in target.search("*"):
        symlink(path.joinpath(item.name), item, overwrite=overwrite)


def link_aws(overwrite=True):
    path = tb.P.home().joinpath(".aws")
    target = dat.joinpath("aws/.aws")
    for item in target.search("*"):
        symlink(path.joinpath(item.name), item, overwrite=overwrite)


def link_gitconfig():
    for config in [".gitconfig"]:
        symlink(tb.P.home().joinpath(config), dat.joinpath(f"settings/{config}"))


def link_scripts():
    folder = {"Windows": "windows", "Linux": "linux"}[platform.system()]
    symlink(tb.P.home().joinpath("scripts"), tb.P.home().joinpath(f"code/dotfiles/scripts/{folder}"))


def link_pypi_creds():
    symlink(tb.P.home().joinpath(".pypirc"), dat.joinpath("creds/.pypirc"))


def link_powershell(overwrite=True):
    path = tb.P(tm.run("$PROFILE.CurrentUserCurrentHost", shell="pwsh").op.split("\n")[0])
    target = dat.joinpath(f"shells/powershell/CurrentUserCurrentHost/{path.name}")
    symlink(path, target, overwrite=overwrite)

    path = tb.P(tm.run("$PROFILE.CurrentUserAllHosts", shell="pwsh").op.split("\n")[0])
    target = dat.joinpath(f"shells/powershell/CurrentUserAllHosts/{path.name}")
    symlink(path, target, overwrite=overwrite)

    path = tb.P(tm.run("$PROFILE.AllUsersCurrentHost", shell="pwsh").op.split("\n")[0])
    target = dat.joinpath(f"shells/powershell/AllUsersCurrentHost/{path.name}")
    symlink(path, target, overwrite=overwrite)

    path = tb.P(tm.run("$PROFILE.AllUsersAllHosts", shell="pwsh").op.split("\n")[0])
    target = dat.joinpath(f"shells/powershell/AllUsersAllHosts/{path.name}")
    symlink(path, target, overwrite=overwrite)


def link_windows_powershell(overwrite=True):
    path = tb.P(tm.run("$PROFILE.CurrentUserCurrentHost", shell="powershell").op.split("\n")[0])
    target = dat.joinpath(f"shells/windows_powershell/CurrentUserCurrentHost/{path.name}")
    symlink(path, target, overwrite=overwrite)

    path = tb.P(tm.run("$PROFILE.CurrentUserAllHosts", shell="powershell").op.split("\n")[0])
    target = dat.joinpath(f"shells/windows_powershell/CurrentUserAllHosts/{path.name}")
    symlink(path, target, overwrite=overwrite)

    path = tb.P(tm.run("$PROFILE.AllUsersCurrentHost", shell="powershell").op.split("\n")[0])
    target = dat.joinpath(f"shells/windows_powershell/AllUsersCurrentHost/{path.name}")
    symlink(path, target, overwrite=overwrite)

    path = tb.P(tm.run("$PROFILE.AllUsersAllHosts", shell="powershell").op.split("\n")[0])
    target = dat.joinpath(f"shells/windows_powershell/AllUsersAllHosts/{path.name}")
    symlink(path, target, overwrite=overwrite)


def link_ipython(overwrite=True):
    path = tb.P.home().joinpath(".ipython/profile_default/ipython_config.py")
    target = dat.joinpath(f"shells/ipython/{path.name}")
    symlink(path, target, overwrite=overwrite)


def main():
    """create symlinks in default locations to `dotfiles` contents"""
    link_gitconfig()
    link_pypi_creds()
    link_ipython()
    link_powershell()
    link_windows_powershell()
    link_scripts()
    link_aws()
    link_ssh()


if __name__ == '__main__':
    pass
