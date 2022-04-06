

# =============================== PYTHON =================================================
winget install --name "Git"

# a terminal restart of terminal is required to for git to work, or the one can update the path
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

winget install -e --id "Python.Python.3" -v "3.9.7150.0" --source winget
set mypy ($env:LOCALAPPDATA + "\Programs\Python\Python39\python.exe")
# OR: winget install --name "Python 3" --source winget  # gives the latest python

python3.9 -m pip install venv
mkdir ~/venvs
cd ~
python3.9 -m venv "./venvs/ve"  # ve will have same python version as `python`, where it.
# activate
~/venvs/ve/Scripts/Activate.ps1
python -m pip install --upgrade pip  # upgrades the pip that is within the environment.

# ====================== REPOS ======================================
cd ~
mkdir code
cd ~/code
git clone https://github.com/thisismygitrepo/crocodile.git
git clone https://github.com/thisismygitrepo/dotfiles  # Choose browser-based authentication.

cd ~/code/crocodile
pip install -e .  # local installation of crocodile (allows for development)
pip install -r requirements.txt  # not installed automatically by corocdile.

# ============================== Shells ===========================================
# winget install --name "PuTTY"
# winget install --name "AWS Command Line Interface"
winget install --name "Windows Terminal" --Id "Microsoft.WindowsTerminal" --Source winget  # Terminal is is installed by default on W 11
winget install --name "Powershell" --Id "Microsoft.PowerShell" --source winget  # powershell require admin

# ==== Fancy shell:
winget install JanDeDobbeleer.OhMyPosh
cd ~/code/dotfiles

python -m fire "./create_symlinks.py" add_scripts_to_path
python -m fire "windows_terminal_setup/change_terminal_settings.py" main
python -m fire "windows_terminal_setup/fancy_prompt_themes.py" install
python -m fire "windows_terminal_setup/fancy_prompt_themes.py" choose

croshell -c "P(r'https://download.sysinternals.com/files/ZoomIt.zip').download(P.home().joinpath('Downloads')).unzip(inplace=True).joinpath('ZoomIt.exe').move(folder=env.WindowsApps)"
