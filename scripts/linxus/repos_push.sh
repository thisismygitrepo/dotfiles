
# shellcheck disable=SC1090
source ~/venvs/ve/bin/activate
cd ~
python -m fire ./code/dotfiles/jobs/repos.py push_all
