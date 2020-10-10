#!/bin/bash
pyenv virtualenv 3.6.3 djangoevents_3.6.3
pyenv local djangoevents_3.6.3 .

pip install -U -r requirements.txt
python setup.py develop

pytest
