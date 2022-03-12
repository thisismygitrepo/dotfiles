

import crocodile.toolbox as tb
import crocodile.enviroment as env

"""
setup file for each shell can be found in $profile. The settings.json is the config file for Terminal.
"""


def install():
    # Step 1: download the required fonts that has all the glyphs and install them.
    folder = tb.P("https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/CascadiaCode.zip").download().unzip()
    txt = tb.P(__file__).with_name("install_fonts.ps1").read_text().replace(r".\fonts-to-be-installed", str(folder))
    file = tb.P.tmpfile(suffix=".ps1").write_text(txt)
    tb.subprocess.run(rf"powershell.exe -executionpolicy Bypass -nologo -noninteractive -File \"{file}\"")

    # Step 2: change the profile of the terminal such that nerd font is chosen for powershell
    from windows_terminal_setup.change_terminal_settings import TerminalSettings
    ts = TerminalSettings()
    ts.customize_powershell(nerd_font=True)
    ts.save_terminal_settings()

    # Step 2.5 Install icons
    tb.Terminal().run("Install-Module -Name Terminal-Icons -Repository PSGallery", shell="powershell")

    # Step 3: install oh-my-posh
    tb.Terminal().run('winget install --name "Oh My Posh" --Id "JanDeDobbeleer.OhMyPosh --source winget', shell="powershell")

    # Step 4: customize powershell profile such that it loads oh-my-posh and the terminal icons automatically.
    # use this if you want to customize Windows Powershell instead of powershell:  console=powershell
    profile_path = tb.P(tb.Terminal().run("$profile", shell="pwsh").op.rstrip())
    theme_path = tb.P.home().joinpath(r"AppData\Local\Programs\oh-my-posh\themes")
    txt = f"oh-my-posh --init --shell pwsh --config {theme_path}\\jandedobbeleer.omp.json | Invoke-Expression"
    profile_path.modify_text(txt="oh-my-posh", alt=txt, newline=True)
    profile_path.append_text("\nImport-Module -Name Terminal-Icons")
    # see also an eviroment profile called current theme of oh my posh


def choose():
    """run this function to interactively choose a style
    Optionally, inpsect the themes of oh my posh and select one:
    """
    tb.P("https://ohmyposh.dev/docs/themes").start()
    # replace ~/jan... with full path to theme. use: start $profile
    name = input(f"A chrome tab with styles is opened, choose one and put its name here: [jandedobbeleer] ")
    name = name or "jandedobbeleer"
    path = tb.P(tb.Terminal().run("$profile", shell="pwsh").op.rstrip())
    # or tb.os.environ["POSH_THEME"] (only available in pwsh shell, not in cmd)
    theme_path = tb.P(tb.Terminal().run("$env:POSH_THEME", shell='pwsh').op.rstrip())
    path.modify_text(txt=theme_path.str, alt=theme_path.with_trunk(name).str, newline=False)
    print(f"Done. Use `.$profile` to force opened terminals to reload profile or restart powershell.")


def add_autostart():
    file = env.AppData.joinpath("Microsoft/Windows/Start Menu/Programs/Startup").joinpath("startup_file.cmd")
    file.write_text(f"powershell.exe \"{tb.P.home().joinpath(r'scripts/terminal.ps1')}\"")


if __name__ == '__main__':
    pass
