
"""
This script Takes away all config files from the computer, place them in one directory
`my_private_keys`, and create symlinks to those files from thier original locations.
"""
import crocodile.toolbox as tb


dat = tb.P.home().joinpath("my_private_keys")
logger = tb.Log(file=False)


def backup_my_private_keys():
    logger.critical(f"Be wary of password saved in history. Do not run this in IPython.")
    key = input(f"Pass key if you have an old one, or press enter to create a new one")
    key = key if key != "" else None
    zipped = dat.zip()
    pw_path, op_path = zipped.encrypt(key=key)
    zipped.delete(are_you_sure=True)
    op_path.move(tb.P(tb.os.environ["ONEDRIVE"]).joinpath("AppData"), overwrite=True)
    final_path = pw_path.zip()
    pw_path.delete(are_you_sure=True)
    print(f"key saved @ {final_path.as_uri()}")
    return final_path


def retrieve_my_private_keys():
    path = input(f"path to key to decrypt keys folder (DONT'T use quotation marks nor raw prefix):")
    pw = tb.P(path)
    pw = pw.unzip().search("*")[0]
    _, dec_file = tb.P(tb.os.environ["ONEDRIVE"]).joinpath("AppData/my_private_keys_encrypted.zip").decrypt(pw)
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


def main():  # run all
    retrieve_my_private_keys()
    link_pypi_and_global_git_config()
    link_crypto_source_of_truth()
    SSH().link()


if __name__ == '__main__':
    retrieve_my_private_keys()
