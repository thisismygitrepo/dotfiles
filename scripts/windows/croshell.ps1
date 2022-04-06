
param ($c="")

~/venvs/ve/Scripts/Activate.ps1

if ($c -eq "") {
    clear
    ipython -i --no-banner --term-title CROSHELL -m crocodile.croshell -c $c
}
else {
    python -c ("from crocodile.toolbox import *; import crocodile.environment as env;" + $c)
}


# --autocall 1 in order to enable shell-like behaviour: e.g.: P x is interpreted as P(x)

#if ($args[0] -eq $null) {
#    $name = "ipython"
#}
#else {
#    $name = $args[0]
#}

# https://www.red-gate.com/simple-talk/sysadmin/powershell/how-to-use-parameters-in-powershell/
