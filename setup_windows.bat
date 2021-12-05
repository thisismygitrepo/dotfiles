
@REM IDEs
winget install --name "anaconda3"
winget install --name "PyCharm Professional Edition"
winget install --name "Node.js"
winget install --name "julia" --Id "Julialang.Julia 1.6.2"
winget install --name "DB Browser for SQLite"

@REM add conda to PATH
set PATH=%PATH%;C:\ProgramData\Anaconda3
set PATH=%PATH%;C:\ProgramData\Anaconda3\Scripts
@REM # if windows-terminal doesn't accept modification, run this:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
conda init powershell
conda create --name ve python=3.9

@REM shells
winget install --name "Git"
cd code
git clone https://github.com/thisismygitrepo/crocodile.git

winget install --name "notepad++"
winget install --name "Windows Terminal" --Id "Preview Microsoft.WindowsTerminal.Preview"
winget install --name "Powershell" --Id "Microsoft.PowerShell" --source winget
winget install JanDeDobbeleer.OhMyPosh
winget install --name "PuTTY"
winget install --name "AWS Command Line Interface"

@REM productivity
winget install --name "Mozilla Firefox"
winget install --name "Mozilla Thunderbird"
winget install --name "Microsoft Garage Mouse without Borders"
winget install --name "VLC media player" --source "winget"

python install_fancy_terminal
