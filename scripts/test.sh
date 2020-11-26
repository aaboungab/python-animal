#! /bin/bash

echo "Testing service 1"
cd service1/
pip3 install -r requirements.txt
python3 -m pytest --cov . --cov-report term-missing

cd ..

echo "Testing service 2"
cd service2/
pip3 install -r requirements.txt
python3 -m pytest --cov . --cov-report term-missing

cd ..

echo "Testing for Animallapp completed"
