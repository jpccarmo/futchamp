.PHONY: testenv devenv activate clean system-packages python-packages install tests run all

testenv:
	python constants.py set_constants test

devenv:
	python constants.py set_constants dev

activate:
	cd .\venv\Scripts\
	activate

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

system-packages:
	sudo apt install python-pip -y

python-packages:
	pip install -r requirements.txt

install:
	system-packages python-packages

tests:
	python manage.py test

run:
	python manage.py run

all:
	clean install tests run