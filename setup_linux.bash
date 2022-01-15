
# The following can run with no prerequisites:
sudo apt update -y
sudo apt upgrade -y
sudo apt install git -Y
# the equivalent of Windows Terminal: TMUX
# From here: https://github.com/dhaneshsivasamy07/tmux_tweaks/blob/master/.tmux.conf
curl -s https://raw.githubusercontent.com/dhaneshsivasamy07/tmux_tweaks/master/install.sh | sudo bash
cd ~ || exit
curl -s https://raw.githubusercontent.com/dhaneshsivasamy07/tmux_tweaks/master/tmux.conf > .tmux.conf
sudo apt install tmux  # allows multiple terminals that are persistent.
sudo apt install openssh-server  # allows SSHing to this machine.

# conda
#apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

# miniconda
sudo apt install wget
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh
bash Miniconda3-py39_4.10.3-Linux-x86_64.sh -y
source .bashrc  # reload to activate conda
# notice that on linux, the default is that miniconda will be added to PATH unlike windows where this is not recommended

# no conda
sudo apt install python3.9  # ignore system level one. launched with `python39`, as opposed to `python`
mkdir ~/venvs/
cd ~/venvs/ || exit
python39 -m virtualenv ve
~/venvs/ve/Scripts/activate

mkdir code
cd ~/code || exit
git clone https://github.com/thisismygitrepo/crocodile.git
cd crocodile || exit
pip install -e .
pip install -r requirements.txt
cd ~ || exit


# ==========================================================
# after having the private_keys, run this:
python -m fire ~/code/dotfiles/create_symlinks.py link_all_to_dotfiles
sudo chmod 600 ~/.ssh/id_ed25519


cd ~/code || exit
git clone git@github.com:thisismygitrepo/crypto.git
python -m fire ~/code/dotfiles/create_symlinks.py link_crypto_source_of_truth
cd ~/code/crypto || exist
pip install -r requirements.txt
cd ~ || exist
echo "All Done!"
