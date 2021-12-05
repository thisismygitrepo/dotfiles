

# Change resolution of a headless linux server (no screen)
xrandr --fb 1920x1080

# install chrome, lastpass, conda, pycharm
# mount g drive, one drive: sh -c "~"



sudo apt install rclone
rclone config
rclone --vfs-cache-mode writes mount onedrive: ~/OneDrive

sudo touch /etc/samba/.credentials.conf
cd /etc/samba
sudo nano .credentials.conf
username=s4551072
password=

sudo mkdir /mnt/pmegdrive
sudo mount -t cifs //file.eait.uq.edu.au/groups /mnt/pmegdrive -o uid=alex,credentials=/etc/samba/.credentials.conf
sudo mount -t cifs //file.eait.uq.edu.au/groups /mnt/rdrive -o uid=alex,credentials=/etc/samba/.credentials.conf

# install python engine API from Matlab installation
# cd /usr/local/MATLAB/R2020b/extern/engines/python
# sudo ~/anaconda3/envs/myenv/bin/python setup.py install


# Adding ssh keys
mkdir .ssh
chmod 700 .ssh
cd .ssh
touch authorized_keys
chmod 600 authorized_keys
Edit your authorized_keys file to add your id_rsa.pub key to this file (paste cleanly!)
cd ..
