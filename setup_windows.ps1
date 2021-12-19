
# 1- Getting Started
winget install --name "Google Chrome" --Id "Google.Chrome" --source winget
winget install --name "Chrome Remote Desktop Host" --Id "Google.ChromeRemoteDesktop" --source winget
# 2- Sign in to Chrome with G account, this will give access to LastPass, sign in to that as well.

# IDEs
winget install --name "anaconda3"
winget install --name "PyCharm Professional Edition"
winget install --name "Node.js"
winget install --name "julia" --Id "Julialang.Julia 1.6.2"
winget install --name "DB Browser for SQLite"

# Python: add conda to PATH, config terminals,
set PATH=%PATH%;C:\ProgramData\Anaconda3
set PATH=%PATH%;C:\ProgramData\Anaconda3\Scripts
# # if windows-terminal doesn't accept modification, run this:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
conda init powershell
# pwsh -Command "conda init powershell"
conda create --name ve python=3.9

# git repos:
winget install --name "Git"
mkdir code
cd code
git clone https://github.com/thisismygitrepo/crocodile.git
pip install -e ./crocodile  # local installation of crocodile (allows for development)
pip install -r ./crocodile/requirements.txt  # not installed automatically by corocdile.
cd ~
conda activate ve

# decryption:
# why launching this in a separate thread?
python -m crocodile.run code/dotfiles/create_symlinks.py -f main --python


git clone https://github.com/thisismygitrepo/crypto.git
pip install -r ./crypto/requirements.txt

# Shells
winget install --name "notepad++"
winget install --name "PuTTY"
winget install --name "AWS Command Line Interface"
winget install --name "Windows Terminal" --Id "Preview Microsoft.WindowsTerminal.Preview"
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