
import crocodile.toolbox as tb


dat = tb.P.home().joinpath("my_private_keys")


class SSH:
    def __init__(self, orig=tb.P.home().joinpath(".ssh"), new=dat.joinpath(".ssh")):
        self.orig = orig
        self.backup = new

    def extract(self):
        for item in self.orig.search("*"):
            item.move(self.orig.joinpath(item.name))

    def link(self):
        for item in self.backup.search("*"):
            self.orig.joinpath(item.name).symlink_to(item)


if __name__ == '__main__':
    pass
