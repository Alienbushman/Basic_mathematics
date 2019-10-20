# Basic_mathematics
This is a repository to showcase some basic functions, I am planning to use it as a proof of concept for integrating technologies

# An example of running the docker image
docker build -t python-barcode . <br />
docker run python-barcode

To run the restful api in a docker container
docker build -t python-barcode .
docker run --network="host" python-barcode

# to test quality of code
pipenv install
pipenv shell
pylint BasicMath.py

# to read documentation
python -m pydoc -w restful_api

# or open a web browser
python -m pydoc -p 5433