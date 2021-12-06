
@REM IDEs
winget install --name "anaconda3"
winget install --name "PyCharm Professional Edition"
winget install --name "Node.js"
winget install --name "julia" --Id "Julialang.Julia 1.6.2"
winget install --name "DB Browser for SQLite"

@REM Python: add conda to PATH, config terminals,
set PATH=%PATH%;C:\ProgramData\Anaconda3
set PATH=%PATH%;C:\ProgramData\Anaconda3\Scripts
@REM # if windows-terminal doesn't accept modification, run this:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
conda init powershell
@REM pwsh -Command "conda init powershell"
conda create --name ve python=3.9

@REM git repos:
winget install --name "Git"
cd code
git clone https://github.com/thisismygitrepo/crocodile.git
pip install -e ./crocodile
pip install -r ./crocodile/requirements.txt
cd code/dotfiles
python create_symlinks.py
git clone https://github.com/thisismygitrepo/crypto.git
pip install -r ./crypto/requirements.txt

@REM Shells
winget install --name "notepad++"
winget install --name "PuTTY"
winget install --name "AWS Command Line Interface"
winget install --name "Windows Terminal" --Id "Preview Microsoft.WindowsTerminal.Preview"
winget install --name "Powershell" --Id "Microsoft.PowerShell" --source winget
winget install JanDeDobbeleer.OhMyPosh
python "terminal_setup/install_fancy_terminal.py"
python "terminal_setup/change_terminal_settings.py"

@REM productivity
winget install --name "Mozilla Firefox"
winget install --name "Mozilla Thunderbird"
winget install --name "Microsoft Garage Mouse without Borders"
winget install --name "VLC media player" --source "winget"

