
# The following can run with no prerequisites:
sudo apt update -y
sudo apt upgrade -y
sudo apt install git

# conda
#apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6


# miniconda
sudo apt install wget
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh
bash Miniconda3-py39_4.10.3-Linux-x86_64.sh -y
bash .bashrc  # reload to activate conda


# no conda
#sudo apt install python3-pip

mkdir code
cd ~/code || exit
git clone https://github.com/thisismygitrepo/crocodile.git
cd crocodile || exis
pip install -e .
pip install -r requirements.txt
cd ..


# ==========================================================
# after having the private_keys, run this:
python -m fire ~/code/dotfiles/create_symlinks.py main
sudo chmod 600 ~/.ssh/id_ed25519


cd ~/code || exit
git clone git@github.com:thisismygitrepo/crypto.git
python -m fire ~/code/dotfiles/create_symlinks.py link_crypto_source_of_truth
cd ~/code/crypto || exist
pip install -r requirements.txt
cd ~ || exist
echo "All Done!"
