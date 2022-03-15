import crocodile.toolbox as tb
import crocodile.environment as env

"""
setup file for each shell can be found in $profile. The settings.json is the config file for Terminal.
"""


def install():
    # Step 1: download the required fonts that has all the glyphs and install them.
    folder = tb.P("https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/CascadiaCode.zip").download().unzip()
    txt = tb.P(__file__).with_name("install_fonts.ps1").read_text().replace(r".\fonts-to-be-installed", str(folder))
    file = tb.P.tmpfile(suffix=".ps1").write_text(txt)
    tb.subprocess.run(rf"powershell.exe -executionpolicy Bypass -nologo -noninteractive -File \"{file}\"")

    # Step 2: Install icons
    tb.Terminal().run("Install-Module -Name Terminal-Icons -Repository PSGallery", shell="powershell")

    # Step 3: install oh-my-posh
    tb.Terminal().run('winget install --name "Oh My Posh" --Id "JanDeDobbeleer.OhMyPosh --source winget', shell="powershell")

    # Step 4: change the profile of the terminal such that nerd font is chosen for your shell
    shell = {"powershell": "pwsh.exe", "Windows Powershell": "powershell.exe"}["powershell"].split(".exe")[0]
    from windows_terminal_setup.change_terminal_settings import TerminalSettings
    if shell == "pwsh":
        ts = TerminalSettings()
        ts.customize_powershell(nerd_font=True)
        ts.save_terminal_settings()
    else:
        raise NotImplementedError

    # Step 5: customize powershell profile such that it loads oh-my-posh and the terminal icons automatically.
    profile_path = tb.P(tb.Terminal().run("$profile", shell=shell).op.rstrip())
    theme_path = tb.P.home().joinpath(r"AppData\Local\Programs\oh-my-posh\themes").collapseuser()  # makes the profile work on any machine.
    txt = f"oh-my-posh --init --shell pwsh --config {theme_path}\\jandedobbeleer.omp.json | Invoke-Expression"
    profile_path.modify_text(txt="oh-my-posh", alt=txt, newline=True)
    profile_path.modify_text(txt="Import-Module -Name Terminal-Icons", alt="Import-Module -Name Terminal-Icons", newline=True)


def choose(name=""):
    """run this function to interactively choose a style
    Optionally, inpsect the themes of oh my posh and select one:
    """
    themes_path = tb.Terminal().run("$env:POSH_THEMES_PATH", shell='pwsh').as_path
    current_theme_path = tb.Terminal().run("$env:POSH_THEME", shell='pwsh').as_path

    if name == "manual":
        tb.P("https://ohmyposh.dev/docs/themes").start()
        # replace ~/jan... with full path to theme. use: start $profile
        name = input(f"A chrome tab with styles is opened, choose one and put its name here: [jandedobbeleer] ")
    if name == "show":
        tb.os.system("Get-PoshThemes")
        return ""
    if name == "": name = themes_path.search().apply(lambda x: x.trunk).sample()[0]
    print("Current Theme:", current_theme_path.trunk)
    print("New theme: ", name)
    profile_path = tb.Terminal().run("$profile", shell="pwsh").as_path
    profile_path.modify_text(txt=current_theme_path.trunk, alt=name, newline=False)


def add_autostart():
    file = env.AppData.joinpath("Microsoft/Windows/Start Menu/Programs/Startup").joinpath("startup_file.cmd")
    file.write_text(f"powershell.exe \"{tb.P.home().joinpath(r'scripts/start_terminal.ps1')}\"")


if __name__ == '__main__':
    pass
