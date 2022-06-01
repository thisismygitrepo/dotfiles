
import crocodile.toolbox as tb

"""
setup file for each shell can be found in $profile. The settings.json is the config file for Terminal.
"""


def install():
    import crocodile.environment as env

    # Step 1: download the required fonts that has all the glyphs and install them.
    folder = tb.P("https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/CascadiaCode.zip").download().unzip()
    txt = tb.P(__file__).with_name("install_fonts.ps1").read_text().replace(r".\fonts-to-be-installed", str(folder))
    file = tb.P.tmpfile(suffix=".ps1").write_text(txt)
    tb.subprocess.run(rf"powershell.exe -executionpolicy Bypass -nologo -noninteractive -File {file.str}")

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
    else: raise NotImplementedError

    # Step 5: customize powershell profile such that it loads oh-my-posh and the terminal icons automatically.
    profile_path = tb.Terminal().run("$profile", shell=shell).as_path
    theme_path = env.LocalAppData.joinpath(r"Programs\oh-my-posh\themes").collapseuser()
    # makes the profile work on any machine.
    txt = f"oh-my-posh --init --shell pwsh --config {theme_path}\\jandedobbeleer.omp.json | Invoke-Expression"
    profile_path.modify_text(txt="oh-my-posh", alt=txt, newline=True)
    profile_path.modify_text(txt="Import-Module -Name Terminal-Icons", alt="Import-Module -Name Terminal-Icons", newline=True)


def choose(name=""):
    """run this function to interactively choose a style. Optionally, inpsect the themes of oh my posh and select one:
    """
    import os
    themes_path = tb.P(os.environ["POSH_THEMES_PATH"])
    current_theme = tb.P(os.environ["POSH_THEME"]).trunk

    if name == "manual":
        tb.P("https://ohmyposh.dev/docs/themes").start()  # replace ~/jan... with full path to theme. use: start $profile
        name = input(f"A chrome tab with styles is opened, choose one and put its name here: [jandedobbeleer] ")
    if name == "show":
        __import__("os").system("Write-Host Get-PoshThemes")
        return ""
    if name == "": name = themes_path.search().apply(lambda x: x.trunk).sample()[0]
    print("Current Theme:", current_theme)
    print("New theme: ", name)
    tb.Terminal().run("$profile", shell="pwsh").as_path.modify_text(txt=current_theme, alt=name, newline=False)


if __name__ == '__main__':
    pass
