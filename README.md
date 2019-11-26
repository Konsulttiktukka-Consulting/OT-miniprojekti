# OT-miniprojekti [![CircleCI](https://circleci.com/gh/Konsulttiktukka-Consulting/OT-miniprojekti.svg?style=svg)](https://circleci.com/gh/Konsulttiktukka-Consulting/OT-miniprojekti)

## How to install
* Make sure to have the latest verison of Python 3, python3-venv, SQLite 3 and pip. 
* Unzip the program folder if needed and make it your current working directory.
* Make virtual environment with  
`python3 -m venv venv`  
* Add the new environment as your source with  
`source venv/bin/activate`  
* Install required libraries with the command  
`pip install -r requirements.txt`  
* Configure flask to run the application

   `export FLASK_APP=application`
* Initialize database

   `flask init-db`
* Run the application with  
`python3 run.py` 

## Tests
* Use the virtual environment  
* Run tests with  
`python3 -m pytest application/tests` 

## Definition of Done

For us, a task is done when all features meant to be implemented have been implemented, tested and are working, test coverage is over 75% and the feature works on Heroku.
## Links
[Backlog](https://docs.google.com/spreadsheets/d/1Wlm32y41gkM6qK-flYYq2uv-XSGK1AAIOtu35zd_JlQ/edit?usp=sharing)

[Heroku](http://konsulttitukkaconsulting.herokuapp.com/)
