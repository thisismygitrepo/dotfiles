

import crocodile.toolbox as tb

folder = tb.P("https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/CascadiaCode.zip").download().unzip()
profile = tb.P(tb.Terminal(console="pwsh").run_command("echo $profile").stdout.replace("\n", ""))
profile.parent.create()
profile.write_text("oh-my-posh --init --shell pwsh --config ~/jonnychipz.omp.json | Invoke-Expression")

import webbrowser
webbrowser.open(url="https://ohmyposh.dev/docs/themes")
# replace ~/jan... with full path to theme.
