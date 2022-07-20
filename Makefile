.PHONY: all help run

all: help

help:
	 @echo "Usage:"
	 @echo " make run - run the app"
	 @echo " make requirements - install the requirement packages"

run:
	 python3 src/main.py

docker/build:
	 docker build -t ind_appointment_checker .

docker/run:
	 docker run -it ind_appointment_checker

requirements:
	 venv/bin/pip3.8 install -r requirements.txt