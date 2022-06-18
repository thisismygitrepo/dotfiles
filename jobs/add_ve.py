
import crocodile.toolbox as tb


def add_ve(ssh, ve_name="ve", py_version="310"):
    scripts = tb.P.cwd().parent.joinpath("setup_fancy_shell.ps1").read_text().split(f"# {'3'}")


if __name__ == '__main__':
    pass
