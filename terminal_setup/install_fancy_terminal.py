

import crocodile.toolbox as tb

# Step 1: download the required fonts that has all the glyphs:
folder = tb.P("https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/CascadiaCode.zip").download().unzip()
# install the fonts.
txt = tb.P("install_fonts.ps1").read_text().replace(r".\fonts-to-be-installed", str(folder))
tb.P("install_fonts.ps1").write_text(txt)
tb.subprocess.run(rf"powershell.exe -executionpolicy Bypass -nologo -noninteractive -file .\Install_Fonts.ps1")

# Step 2: change the profile of the terminal such that it autoloads oh-my-posh
response = tb.subprocess.run("pwsh -Command $profile", shell=True, capture_output=True, text=True)
# use this if you want to customize Windows Powershell:
# response = tb.subprocess.run("powershell -Command $profile", shell=True, capture_output=True, text=True)
profile_path = tb.P(response.stdout.replace("\n", ""))
profile_path.parent.create()
theme_path = tb.P.home().joinpath(r"AppData\Local\Programs\oh-my-posh\themes")
profile_path.write_text(f"oh-my-posh --init --shell pwsh --config {theme_path}/atomicBit.omp.json | Invoke-Expression")

# Optionally, inpsect the themes of oh my posh and select one:
import webbrowser
webbrowser.open(url="https://ohmyposh.dev/docs/themes")
# replace ~/jan... with full path to theme.
# use: start $profile
# to update: . $profile
