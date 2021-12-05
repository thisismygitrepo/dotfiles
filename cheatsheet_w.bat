

winget install --name "anaconda3"
winget install --name "PyCharm Professional Edition"
winget install --name "Node.js"
winget install --name "julia" --Id "Julialang.Julia 1.6.2"

winget install --name "notepad++"
winget install --name "Windows Terminal" --Id "Preview Microsoft.WindowsTerminal.Preview"
winget install --name "Powershell" --Id "Microsoft.PowerShell"
winget install JanDeDobbeleer.OhMyPosh


winget install --name "Git"
winget install --name "Mozilla Firefox"
winget install --name "Mozilla Thunderbird"
winget install --name "PuTTY"

winget install --name "AWS Command Line Interface"
winget install --name "Microsoft Garage Mouse without Borders"
winget install --name "DB Browser for SQLite"
winget install --name "VLC media player" --source "winget"

# add conda to PATH
set PATH=%PATH%;C:\ProgramData\Anaconda3
set PATH=%PATH%;C:\ProgramData\Anaconda3\Scripts
conda init powershell
# if windows-terminal doesn't accept modification, run this:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted


# Python 
tb.P("https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/CascadiaCode.zip").download().unzip()
# install fonts automatically?
import crocodile.toolbox as tb
p = tb.P(tb.Terminal(console="pwsh").run_command("echo $profile").stdout.replace("\n", ""))
p.parent.create()
p.write_text("oh-my-posh --init --shell pwsh --config ~/jandedobbeleer.omp.json | Invoke-Expression")
# full themes: https://ohmyposh.dev/docs/themes
# replace ~/jan... with full path to theme.
