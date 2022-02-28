

import crocodile.toolbox as tb
from crocodile.enviroment import OneDriveConsumer


onedrive = OneDriveConsumer
dat = tb.P.home().joinpath("dotfiles")


def main():
    """Decrypts and brings a copy of `dotfiles` from OneDrive"""
    key = dat.joinpath("creds/encrypted_files_key.bytes")
    if not key.exists():
        key = tb.P(input(f"path to key (DONT'T use quotation marks nor raw prefix):")).unzip(inplace=False, verbose=True).find()
    dotfiles = onedrive.joinpath("AppData/dotfiles_encrypted.zip").copy(folder="~")
    # make sure to avoid doing decryption in the storage site.
    dotfiles.decrypt(key=key, inplace=True).unzip(folder="~", inplace=True, verbose=True)
    print(" ========================= SUCCESSFULLY RETRIEVED ===============================")


if __name__ == '__main__':
    pass
