
import crocodile.toolbox as tb


def backup_dotfiles():
    """Encrypts and saves a copy of `dotfiles` to OneDrive"""
    key = input(f"Pass key if you have an old one, or press enter to create a new one")
    key = None if key == "" else tb.P(key).find()
    # P("lastpass_export_2022_1_1.csv").encrypt(key="key.zip")
    dat = tb.P.home().joinpath("dotfiles")
    pw_path, op_path = dat.zip_and_cipher(key=key, delete=False, verbose=True)
    op_path.move(tb.P(tb.os.environ["ONEDRIVE"]).joinpath("AppData"), overwrite=True)
    return pw_path


if __name__ == '__main__':
    pass
