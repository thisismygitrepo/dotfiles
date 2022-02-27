
# to get exact version of an app in winget, head to: https://winget.run

# ================================= APPS ================================================
# 1- Getting Started
winget install --name "Google Chrome" --Id "Google.Chrome" --source winget
#winget install --name "Chrome Remote Desktop Host" --Id "Google.ChromeRemoteDesktop" --source winget
# 2- Sign in to Chrome with G account, this will give access to LastPass, sign in to that as well.
# winget search "Microsoft Teams" --Id "Microsoft.Teams" --Source winget

# productivity
winget install --name "Mozilla Firefox"
winget install --name "Mozilla Thunderbird"
winget install --name "Microsoft Garage Mouse without Borders"
#winget install --name "VLC media player" --source "winget"

# winget install "sql server management studio"

# IDEs
# winget install --name "anaconda3"
# winget install --name miniconda3
winget install --name "notepad++" --source winget
winget install --name "Microsoft Visual Studio Code" --Id "Microsoft.VisualStudioCode" --source winget
winget install --name "PyCharm Professional Edition"
winget install --name "Node.js"
winget install --name "julia" --Id "Julialang.Julia" --source winget
winget install --name "DB Browser for SQLite"
winget install --name "Ubuntu" --Id Canonical.Ubuntu --source winget
# in the future it will be: `wsl --install`
Ubuntu  # this will install it, you will be prompted for user name and password.

