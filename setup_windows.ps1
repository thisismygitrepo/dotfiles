
# 1- Getting Started
winget install --name "Google Chrome" --Id "Google.Chrome" --source winget
winget install --name "Chrome Remote Desktop Host" --Id "Google.ChromeRemoteDesktop" --source winget
# 2- Sign in to Chrome with G account, this will give access to LastPass, sign in to that as well.

# IDEs
# winget install --name "anaconda3"
# winget install --name miniconda3
winget install --name "PyCharm Professional Edition"
winget install --name "Node.js"
winget install --name "julia" --Id "Julialang.Julia" --source winget
winget install --name "DB Browser for SQLite"

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

winget install --name "Python 3.9" --source msstore  # system level python
# OR:
winget install --name "Python 3" --source winget  # latest
python -m pip install --upgrade pip
python -m pip install virtualenv
mkdir ~/.virtualenvs
cd ~
python -m venv "./.virtualenvs/ve"  # ve will have same python version as `python`, where it.
# activate
~/.virtualenvs/ve/Scripts/Activate.ps1

# git repos:
winget install --name "Git"
mkdir code
git clone https://github.com/thisismygitrepo/crocodile.git

cd ~/code/crocodile
pip install -e .  # local installation of crocodile (allows for development)
pip install -r requirements.txt  # not installed automatically by corocdile.
cd ~

# decryption:
# why launching this in a separate thread?
python -m crocodile.run code/dotfiles/create_symlinks.py -f main --python


git clone https://github.com/thisismygitrepo/crypto.git
cd ~/code/crypto  # you need to cd first then run pip because the latter doesn't understand "~"
pip install -r requirements.txt

# Shells
winget install --name "notepad++"
# winget install --name "PuTTY"
# winget install --name "AWS Command Line Interface"
winget install --name "Windows Terminal" --Id "Microsoft.WindowsTerminal" --Source winget
winget install --name "Powershell" --Id "Microsoft.PowerShell" --source winget

winget install JanDeDobbeleer.OhMyPosh
python -m fire "terminal_setup/install_fancy_terminal.py" install
# python -m fire "terminal_setup/install_fancy_terminal.py" choose
python "terminal_setup/change_terminal_settings.py"

# productivity
winget install --name "Mozilla Firefox"
winget install --name "Mozilla Thunderbird"
winget install --name "Microsoft Garage Mouse without Borders"
winget install --name "VLC media player" --source "winget"

#  winget install "sql server management studio"
