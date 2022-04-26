
# Set up project for tests:

> #### There are two ways to do that:
>
>1. Using PostgreSQL
>2. Using SQLite

### 1. Config with PostgreSQL

Clone this repo and switch to Django-dev branch with this command:

    git clone -b django_setup https://github.com/semleon333/BossDog.git && cd BossDog/src

Install and run postgresql on your server:

    sudo apt install postgresql postgresql-contrib
    sudo systemctl start postgresql.service

Then rename **.env.dist** to **.env** and replace all values in this file with yours.<br>
Set this values into DATABASE variable in **config/settings.py**

After that, get PostgreSQL shell:

    sudo -u postgres psql postgres

and configure database and user (all values in "<>" must match with .env):

    CREATE USER <DB_USER> WITH PASSWORD '<DB_PASSWORD>';
    CREATE DATABASE <DB_NAME> OWNER <DB_USER>;
    GRANT ALL ON DATABASE <DB_NAME> TO <DB_USER>;
    \q
    

Create virtual environment and install dependencies:

    python -m venv venv && . ./venv/bin/activate && pip install -r requirements.txt

Then make django migrations and start server:

    ./manage.py makemigrations && ./manage.py migrate
    ./manage.py runserver