
# allow ssh to linux:
# on the linux machine:
sudo apt install openssh-server

# locally
sftp username@hostname  # put in password for once
# !!
mkdir .ssh
cd .ssh || exit
put ./.ssh/id_rsa.pub
exit  # sftp doesn't support cat command.
cat id_rsa.pub > authorized_keys


# The following can run with no prerequisites:
# when there is a !! sign, means the command before it requires input, putting another command behind it
# will cause it to fail
ssh alex@salhn-thinkpad
# !!

sudo apt update
sudo apt upgrade
sudo apt install wget
sudo apt install git
# the equivalent of Windows Terminal: TMUX
# From here: https://github.com/dhaneshsivasamy07/tmux_tweaks/blob/master/.tmux.conf
curl -s https://raw.githubusercontent.com/dhaneshsivasamy07/tmux_tweaks/master/install.sh | sudo bash
cd ~ || exit
curl -s https://raw.githubusercontent.com/dhaneshsivasamy07/tmux_tweaks/master/tmux.conf > .tmux.conf
sudo apt install tmux  # allows multiple terminals that are persistent.

# install chrome:
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
# install snap store
sudo mv /etc/apt/preferences.d/nosnap.pref ~/Documents/nosnap.backup
sudo apt update
sudo apt install snapd
# install development apps:
sudo snap install pycharm-community --classic
sudo snap install code --classic
sudo snap install powershell --classic

# conda
#apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

# miniconda
#sudo apt install wget
#wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh
#bash Miniconda3-py39_4.10.3-Linux-x86_64.sh -y
#source .bashrc  # reload to activate conda
## notice that on linux, the default is that miniconda will be added to PATH unlike windows where this is not recommended

sudo apt install python3.9  # ignore system level one. launched with `python39`, as opposed to `python`
sudo apt install python3.9-venv
mkdir ~/venvs/
cd ~/venvs/ || exit
python3.9 -m venv ve
cd ~ || exit
source ~/venvs/ve/bin/activate || exit


cd ~ || exit
mkdir code
cd ~/code || exit
git clone https://github.com/thisismygitrepo/crocodile.git
git clone https://github.com/thisismygitrepo/dotfiles.git
cd ~/crocodile || exit
pip install -e .
pip install -r requirements.txt
cd ~ || exit

python -m fire ~/code/dotfiles/create_symlinks.py link_scripts
sudo chmod 600 ~/.ssh/id_ed25519
echo "All Done!"
