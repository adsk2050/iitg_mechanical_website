#! /bin/bash

sudo apt update -y;
sudo apt upgrade -y;
sudo apt install -y python3-virtualenv virtualenv apache2-dev python3-dev;
git init;
git clone https://github.com/adsk2050/iitg_mechanical_website.git;
cd iitg_mechanical_website;
virtualenv --python=/usr/bin/python3 venv;
. ~/iitg_mechanical_website/venv/bin/activate;
pip install -r requirements.txt;
python manage.py collectstatic;
sudo cp ~/iitg_mechanical_website/extrasAD/mechweb.conf /etc/apache2/sites-available/mechweb.conf;
sudo a2ensite mechweb.conf;
sudo chown :www-data ~/iitg_mechanical_website/db.sqlite3;
sudo chown :www-data ~/iitg_mechanical_website;
sudo service apache2 restart;
