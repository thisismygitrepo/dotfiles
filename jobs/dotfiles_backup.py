
import crocodile.toolbox as tb
from crocodile.enviroment import OneDriveConsumer, OneDriveExe


onedrive = OneDriveConsumer
dat = tb.P.home().joinpath("dotfiles")


def main():
    """Encrypts and saves a copy of `dotfiles` to OneDrive"""
    key = dat.joinpath("creds/encrypted_files_key.bytes")
    downloaded_key_from_lastpass = False
    if not key.exists():
        # key = input(f"Pass key if you have an old one, or press enter to create a new one")
        key = tb.P.home().joinpath("Downloads/key.zip").unzip(inplace=False, verbose=True).find()
        downloaded_key_from_lastpass = True
    # P("lastpass_export_2022_1_1.csv").encrypt(key="key.zip")
    # caveat: if there is more than onedrive account.
    dat.zip_n_encrypt(key=key, inplace=False, verbose=True).move(folder=onedrive.joinpath("AppData"), overwrite=True)
    if downloaded_key_from_lastpass: key.delete(sure=True)
    print(" ========================= SUCCESSFULLY BACKEDUP ===============================")
    OneDriveExe()


if __name__ == '__main__':
    pass
