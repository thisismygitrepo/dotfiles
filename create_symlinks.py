
"""
This script Takes away all config files from the computer, place them in one directory
`my_private_keys`, and create symlinks to those files from thier original locations.
"""
import crocodile.toolbox as tb


dat = tb.P.home().joinpath("my_private_keys")
# logger = tb.Log(file=False)


def backup_my_private_keys():
    """Encrypts and saves a copy of `my_private_keys` to OneDrive"""
    key = input(f"Pass key if you have an old one, or press enter to create a new one")
    key = None if key == "" else tb.P(key).find()
    pw_path, op_path = dat.zip_and_cipher(secret=key, delete=False, security="encrypt", verbose=True)
    op_path.move(tb.P(tb.os.environ["ONEDRIVE"]).joinpath("AppData"), overwrite=True)
    return pw_path


def retrieve_my_private_keys():
    """Decrypts and brings a copy of `my_private_keys` from OneDrive"""
    tb.P(tb.os.environ["ONEDRIVE"]).joinpath("AppData/my_private_keys_encrypted.zip").decrypt(tb.P(input(f"path to key to decrypt keys folder (DONT'T use quotation marks nor raw prefix):")).unzip(delete=False, verbose=True).find()).unzip(op_path=tb.P.home(), delete=True, verbose=True)


def symlink(this, to_this):
    """helper function."""
    this = tb.P(this)
    if this.exists():
        this.delete(are_you_sure=True)
    elif not this.parent.exists():
        this.parent.create()

    try:
        this.symlink_to(to_this)
        print(f" Succesfully linked {this} ==> {to_this}")
    except Exception as ex:
        print(f"Failed at linking {this} ==> {to_this}. Reason: {ex}")


class SSH:
    """"""
    def __init__(self, orig=tb.P.home().joinpath(".ssh"), new=dat.joinpath(".ssh")):
        self.orig = orig
        self.backup = new

    def extract(self):
        for item in self.orig.search("*"):
            item.move(self.backup)
        return self

    def link(self):
        for item in self.backup.search("*"):
            symlink(self.orig.joinpath(item.name), item)
        return self


class AWS(SSH):
    def __init__(self, orig=tb.P.home().joinpath(".aws"), new=dat.joinpath("aws/.aws")):
        super(AWS, self).__init__(orig, new)


def link_pypi_and_global_git_config():
    symlink(tb.P.home().joinpath(".pypirc"), dat.joinpath("creds/.pypirc"))
    symlink(tb.P.home().joinpath(".gitconfig"), dat.joinpath("settings/.gitconfig"))


def link_crypto_source_of_truth():
    symlink(tb.P.home().joinpath("code/crypto/utils/source_of_truth.py"),
            dat.joinpath("creds/crypto_source_of_truth.py"))


def main():
    """create symlinks in default locations to `my_private_keys` contents"""
    link_pypi_and_global_git_config()
    SSH().link()
    AWS().link()


if __name__ == '__main__':
    pass
