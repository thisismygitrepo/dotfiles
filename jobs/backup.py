
import crocodile.toolbox as tb

dat = tb.P.home().joinpath("dotfiles")


def backup_dotfiles():
    """Encrypts and saves a copy of `dotfiles` to OneDrive"""
    key = dat.joinpath("creds/encrypted_files_key.bytes")
    if not key.exists():
        # key = input(f"Pass key if you have an old one, or press enter to create a new one")
        key = tb.P.home().joinpath("Downloads/key.zip").unzip(inplace=False, verbose=True).find()
    # P("lastpass_export_2022_1_1.csv").encrypt(key="key.zip")
    # caveat: if there is more than onedrive account.
    dat.zip_n_encrypt(key=key, inplace=False, verbose=True).move(tb.P(tb.os.environ["ONEDRIVE"]).joinpath("AppData"),
                                                                 overwrite=True)
    key.delete(sure=True)
    print(" ========================= SUCCESSFULLY BACKEDYP ===============================")


def retrieve_dotfiles():
    """Decrypts and brings a copy of `dotfiles` from OneDrive"""
    key = dat.joinpath("creds/encrypted_files_key.bytes")
    if not key.exists():
        key = tb.P(input(f"path to key (DONT'T use quotation marks nor raw prefix):")).unzip(inplace=False, verbose=True).find()
    dotfiles = tb.P(tb.os.environ["ONEDRIVE"]).joinpath("AppData/dotfiles_encrypted.zip").copy(folder="~")
    # make sure to avoid doing decryption in the storage site.
    dotfiles.decrypt(key=key, inplace=True).unzip(folder="~", inplace=True, verbose=True)
    print(" ========================= SUCCESSFULLY RETRIEVED ===============================")


if __name__ == '__main__':
    pass
