
~/venvs/ve/Scripts/Activate.ps1
clear



ipython -i --no-banner --term-title CROSHELL -m crocodile.croshell
# --autocall 1 in order to enable shell-like behaviour: e.g.: P x is interpreted as P(x)

#if ($args[0] -eq $null) {
#    $name = "ipython"
#}
#else {
#    $name = $args[0]
#}
