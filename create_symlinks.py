
"""
This script Takes away all config files from the computer, place them in one directory
`dotfiles`, and create symlinks to those files from thier original locations.
"""
import crocodile.toolbox as tb


dat = tb.P.home().joinpath("dotfiles")
# logger = tb.Log(file=False)


def retrieve_dotfiles():
    """Decrypts and brings a copy of `dotfiles` from OneDrive"""
    tb.P(tb.os.environ["ONEDRIVE"]).joinpath("AppData/dotfiles_encrypted.zip").decrypt(tb.P(input(f"path to key to decrypt keys folder (DONT'T use quotation marks nor raw prefix):")).unzip(delete=False, verbose=True).find()).unzip(op_path=tb.P.home(), delete=True, verbose=True)


def symlink(this, to_this):
    """helper function."""
    this = tb.P(this)
    try:
        this.symlink_to(to_this, verbose=True, delete=True)
    except Exception as ex:
        print(f"Failed at linking {this} ==> {to_this}.\nReason: {ex}")


class SSH:
    """

    """
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


def link_config():
    for config in [".gitconfig"]:
        symlink(tb.P.home().joinpath(config), dat.joinpath(f"settings/{config}"))


def link_crypto_source_of_truth():
    file = "crypto_source_of_truth.py"
    symlink(tb.P.home().joinpath(f"code/crypto/utils/{file}"),
            dat.joinpath(f"creds/{file}"))


def link_pypi_creds():
    symlink(tb.P.home().joinpath(".pypirc"), dat.joinpath("creds/.pypirc"))


def link_all_to_dotfiles():
    """create symlinks in default locations to `dotfiles` contents"""
    link_config()
    SSH().link()
    AWS().link()


if __name__ == '__main__':
    pass
