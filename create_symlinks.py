
"""
This script Takes away all config files from the computer, place them in one directory
`my_private_keys`, and create symlinks to those files from thier original locations.
"""
import crocodile.toolbox as tb


dat = tb.P.home().joinpath("my_private_keys")
logger = tb.Log(file=False)


def backup_my_private_keys():
    logger.critical(f"Be wary of password saved in history. Do not run this in IPython.")
    if not input(f"Confirm? [y/n]") != "y": return None
    onedrive_path = tb.Terminal().run_command(fr"$env:ONEDRIVE").stdout.replace("\n", "")
    zipped = dat.zip()
    enc, pw = zipped.encrypt()
    zipped.delete(are_you_sure=True)
    target = tb.P(onedrive_path).joinpath("AppData")
    enc.move(target, replace=True)
    return pw


def retrieve_my_private_keys(pw):
    # onedrive_path = tb.Terminal().run_command(fr"$env:ONEDRIVE").stdout.replace("\n", "")
    onedrive_path = tb.os.environ["ONEDRIVE"]
    dec_file = tb.P(onedrive_path).joinpath("AppData/my_private_keys_encrypted.zip").decrypt(pw)
    dec_file.unzip(op_path=tb.P.home())
    dec_file.delete(are_you_sure=True)


def symlink(this, to_this):
    """helper function."""
    this = tb.P(this)
    if this.exists():
        this.delete(are_you_sure=True)
    this.symlink_to(to_this)
    logger.warning(f"{this} ==> {to_this}")


class SSH:
    def __init__(self, orig=tb.P.home().joinpath(".ssh"), new=dat.joinpath(".ssh")):
        self.orig = orig
        self.backup = new

    def extract(self):
        for item in self.orig.search("*"):
            item.move(self.orig.joinpath(item.name))

    def link(self):
        for item in self.backup.search("*"):
            symlink(self.orig.joinpath(item.name), item)


def link_pypi_and_global_git_config():
    symlink(tb.P.home().joinpath(".pypirc"), dat.joinpath("creds/.pypirc"))
    symlink(tb.P.home().joinpath(".gitconfig"), dat.joinpath("settings/.gitconfig"))


def link_crypto_source_of_truth():
    symlink(tb.P.home().joinpath("code/crypto/utils/source_of_truth.py"),
            dat.joinpath("creds/crypto_source_of_truth.py"))


def main(pw):  # run all
    retrieve_my_private_keys(pw)
    link_pypi_and_global_git_config()
    link_crypto_source_of_truth()
    SSH().link()


if __name__ == '__main__':
    pass
