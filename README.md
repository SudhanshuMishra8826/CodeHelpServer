# CodeHelpServer

### Repo initial setup
```
git clone https://github.com/SudhanshuMishra8826/CodeHelpServer 
cd CodeHelpServer
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

#Client Live at https://boring-almeida-721767.netlify.app/
