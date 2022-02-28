

# =============================== PYTHON =================================================
winget install --name "Git"

# a terminal restart of terminal is required to for git to work, or the one can update the path
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

winget install -e --id "Python.Python.3" -v "3.9.7150.0" --source winget
set mypy ($env:LOCALAPPDATA + "\Programs\Python\Python39\python.exe")
# OR:
#winget install --name "Python 3" --source winget  # gives the latest python

python3.9 -m pip install --upgrade pip
python3.9 -m pip install venv
mkdir ~/venvs
cd ~
python3.9 -m venv "./venvs/ve"  # ve will have same python version as `python`, where it.
# activate
~/venvs/ve/Scripts/Activate.ps1
python -m pip install --upgrade pip  # upgrades the pip that is within the environment.


# Python: add conda to PATH, config terminals,
# set PATH=%PATH%;C:\ProgramData\Anaconda3
# set PATH=%PATH%;C:\ProgramData\Anaconda3\Scripts
# Conda by default do not contaminate global variables. instead, it provides two consoles, cmd and powershell
# That have their local variables with conda in them. If you want conda in all consoles
# The following contaminates all the global variables of the system with conda path
# following this contamination, conda command is available everywhere, then, conda init can help configure
# individual consoles so that its enviroments are accessible therein.
# [Environment]::SetEnvironmentVariable("Path", $env:Path + ";$home/miniconda3/Scripts", "User")
# # if windows-terminal doesn't accept modification, run this:
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
# conda init powershell
# pwsh -Command "conda init powershell"
# conda create --name ve python=3.9


# ====================== REPOS ======================================
# git repos:
cd ~
mkdir code
cd ~/code
git clone https://github.com/thisismygitrepo/crocodile.git
git clone https://github.com/thisismygitrepo/dotfiles  # Choose browser-based authentication.

cd ~/code/crocodile
pip install -e .  # local installation of crocodile (allows for development)
pip install -r requirements.txt  # not installed automatically by corocdile.

cd ~/code
start ($env:LOCALAPPDATA + "\Microsoft\OneDrive\onedrive.exe")
cd ~/code/dotfiles
python -m fire ./jobs/backup.py retrieve_dotfiles
cd ~/code/dotfiles
python -m fire./create_symlinks.py main


# ============================== Shells ===========================================
# winget install --name "PuTTY"
# winget install --name "AWS Command Line Interface"
winget install --name "Windows Terminal" --Id "Microsoft.WindowsTerminal" --Source winget
# Terminal is is installed by default on W 11
winget install --name "Powershell" --Id "Microsoft.PowerShell" --source winget  # powershell require admin

# ==== Fancy shell:
winget install JanDeDobbeleer.OhMyPosh
cd ~/code/dotfiles
python -m fire "windows_terminal_setup/change_terminal_settings.py" main
python -m fire "windows_terminal_setup/install_fancy_terminal.py" install
python -m fire "windows_terminal_setup/install_fancy_terminal.py" choose
