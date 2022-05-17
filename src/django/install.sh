#!/bin/sh


# installing base OS packeges: PostgresSQL, Python
sudo apt install postgresql postgresql-contrib python3 python3-pip python3-venv python3-dev libpq-dev
# start PostgreSQL deamon
sudo systemctl start postgresql.service


# entering data
echo "Enter username(NOT 'user') of db_user:"
read DB_USER
echo "You enter: '$DB_USER'\n"

echo "Enter password of db_user:"
read DB_PASSWORD
echo "You enter: '$DB_PASSWORD'\n"

echo "Enter db_name:"
read DB_NAME
echo "You enter: '$DB_NAME'\n"

echo "Enter Django SECRET_KEY:"
read SECRET_KEY
echo "You enter: '$SECRET_KEY'\n"


# psql
sudo -u postgres psql postgres -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"
sudo -u postgres psql postgres -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;"
sudo -u postgres psql postgres -c "GRANT ALL ON DATABASE $DB_NAME TO $DB_USER;"


# generate .env
echo "
DB_NAME=$DB_NAME
DB_USER=$DB_USER
DB_PASSWORD=$DB_PASSWORD
SECRET_KEY=$SECRET_KEY
DJANGO_DEBUG=True" >> .env


# venv and requirments
exec "python3 -m venv venv"
exec ". ./venv/bin/activate"
exec "pip install -r requirements.txt"


# manage
exec "./manage.py makemigrations"
exec "./manage.py migrate"
exec "./manage.py createsuperuser"
exec "./manage.py runserver"

