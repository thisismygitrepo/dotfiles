
# to get exact version of an app in winget, head to: https://winget.run

# ================================= APPS ================================================
winget install --name "Google Chrome" --Id "Google.Chrome" --source winget
#winget install --name "Chrome Remote Desktop Host" --Id "Google.ChromeRemoteDesktop" --source winget
# winget search "Microsoft Teams" --Id "Microsoft.Teams" --Source winget

# productivity
winget install --name "7-zip" --Id "7zip.7zip" --source winget
winget install --name "Mozilla Firefox"
winget install --name "Mozilla Thunderbird"
winget install --name "Microsoft Garage Mouse without Borders"
#winget install --name "VLC media player" --source "winget"
#winget install --name "StreamlabsOBS" --Id "Streamlabs.StreamlabsOBS" --source "winget"
#winget install --name "sql server management studio" --Id "Microsoft.SQLServerManagementStudi" --source winget
#winget install --name "MiKTeX" --Id "ChristianSchenk.MiKTeX"  --source winget  # library / lanugage
#winget install --name "TexMaker" --Id "Texmaker.Texmaker" --source winget  # IDE better than simple TexWorks shipped with MikTex. IDE is basically GUI for cmd interface of Tex

# IDEs
# winget install --name "anaconda3"
# winget install --name miniconda3
winget install --name "notepad++" --source winget
winget install --name "Microsoft Visual Studio Code" --Id "Microsoft.VisualStudioCode" --source winget
winget install --name "PyCharm Professional Edition"
# winget install --name "PyCharm Community Edition" --Id "JetBrains.PyCharm.Community" --source winget
# winget install spyder

winget install --name "Node.js"
winget install --name "julia" --Id "Julialang.Julia" --source winget
winget install --name "DB Browser for SQLite"
wsl --install -d Ubuntu
