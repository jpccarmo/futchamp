# futchamp

To start running the app, do the following:

First install the latest python 3.6 version

Install pip:<br/>
    sudo apt install python-pip -y

Install virtualenv:<br/>
    pip install virtualenv

Create the virtualenv folder:<br/>
    python -m venv venv

Activate virtualenv:<br/>
    run the script called "activate" inside the \venv\Scripts folder

install requirements:<br/>
    pip install -r requirements.txt

Set the environment:<br/>
    for the test environment (the one that uses a sqlite file on your machine): python constants.py set_constants test<br/>
    for the dev environment (the one that uses postgres on heroku server): python constants.py set_constants dev

Run:<br/>
    python manage.py run

<br/>
for simple usage check the Makefile
