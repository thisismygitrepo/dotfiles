
$ErrorActionPreference = "Stop"  # if there is any error in any command, stop there instead of proceeding to the next.

# ================================================== PYTHON =================================================
winget install --name "Git" --Id "Git.Git" --source winget --accept-package-agreements --accept-source-agreements
#git config credential.helper store  # makes git remember credentials.

# a terminal restart of terminal is required to for git to work, or the one can update the path
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

winget install -e --id "Python.Python.3" -v "3.9.7150.0" --source winget  # from https:\\winget.run
# winget install Python.Python.3 --source winget  # installs the latest.
# OR: winget install --name "Python 3" --source winget  # gives the latest python

