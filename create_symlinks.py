
import crocodile.toolbox as tb


dat = tb.P.home().joinpath("my_private_keys")


def symlink(this, to_this):
    this = tb.P(this)
    if this.exists():
        this.delete(are_you_sure=True)
    this.symlink_to(to_this)
    print(f"{this} ==> {to_this}")


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
    link_pypi_and_global_git_config()
    SSH().link()


if __name__ == '__main__':
    pass
