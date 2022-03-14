
~/venvs/ve/Scripts/Activate.ps1
cd ~/code/dotfiles
if ($args[0] -eq $null) {
    $name = ""
}
else {
    $name = $args[0]
}
python -m fire ./windows_terminal_setup/install_fancy_terminal.py choose $args[0]
.$profile  # reload the profile
