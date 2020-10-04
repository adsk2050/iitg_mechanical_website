(For development)How to run it on your system:

- sudo apt update -y;
- sudo apt install virtualenv python3-virtualenv;
- cd ~;
- git init;
- git clone https://github.com/adsk2050/iitg_mechanical_website.git;
- git checkout -b <your_new_branch_name>;
- cd iitg_mechanical_website;
- virtualenv --python=/usr/bin/python3 venv;
*Here you can use your version of python instead of /usr/bin/python. For example if you installed anaconda3, use: ~/anaconda3/bin/python
- source ~/iitg_mechanical_website/venv/bin/activate;
- pip install -r requirements.txt;
- python manage.py collectstatic;
- python manage.py runsslserver;

If you are an IITG student, you get $100 credit on Microsoft Azure. Log in to [Microsoft Azure](portal.azure.com), claim your benefits and get going with the project. In case you use Azure VM, be sure to create an inbound rule in neworking section of the VM to allow port 8080 and instead of running python manage.py runsslserver, run *python manage.py runsslserver 0:8080*. Then you will be able to access the website on <Azure VM Public IP address>:8080.
  
 I would love to see a student from IITG take up this project from my hands and take it forward. Others are also welcome.
 
 I would strongly advise to use [Sublime merge](https://www.sublimemerge.com/docs/linux_repositories#apt) to manage version control. It is very intuitive and doesn't have a steep learning curve like git bash.
