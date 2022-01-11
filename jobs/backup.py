
import crocodile.toolbox as tb

dat = tb.P.home().joinpath("dotfiles")


def backup_dotfiles(auto=True):
    """Encrypts and saves a copy of `dotfiles` to OneDrive"""
    if not auto:
        key = input(f"Pass key if you have an old one, or press enter to create a new one")
        key = None if key == "" else tb.P(key).find()
    else:
        key = dat.joinpath("creds/encrypted_files_key.bytes")
    # P("lastpass_export_2022_1_1.csv").encrypt(key="key.zip")
    # caveat: if there is more than onedrive account.
    dat.zip_n_encrypt(key=key, inplace=False, verbose=True).move(tb.P(tb.os.environ["ONEDRIVE"]).joinpath("AppData"),
                                                                 overwrite=True)


def retrieve_dotfiles(auto=True):
    """Decrypts and brings a copy of `dotfiles` from OneDrive"""
    if not auto:
        key = tb.P(input(f"path to key (DONT'T use quotation marks nor raw prefix):")).unzip(delete=False, verbose=True).find()
    else:
        key = dat.joinpath("creds/encrypted_files_key.bytes")
    dotfiles = tb.P(tb.os.environ["ONEDRIVE"]).joinpath("AppData/dotfiles_encrypted.zip").copy(folder="~")
    # make sure to avoid doing decryption in the storage site.
    dotfiles.decrypt(key=key).unzip(folder="~", inplace=True, verbose=True)


if __name__ == '__main__':
    pass
