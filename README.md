# Basic_mathematics
This is a repository to showcase some basic functions, I am planning to use it as a proof of concept for integrating technologies

# An example of running the docker image
docker build -t python-barcode . <br />
docker run python-barcode

To run the restful api in a docker container <br />
docker build -t python-barcode . <br />
docker run --network="host" python-barcode <br />

# to test quality of code
pipenv install <br />
pipenv shell <br />
pylint basic_math.py

# to read documentation
python -m pydoc -w restful_api

# or open a web browser
python -m pydoc -p 5433

# for basic covarage testing
coverage run BasicMathTest.py
coverage report
# or to get an html document with an outlined section on what is being covered
coverage html
# Note you can also run decision coverage if you want with 
coverage run --branch BasicMathTest.py

# To run mutation testing
 mut.py -t basic_math.py --unit-test BasicMathTest.py 
# add the following flag in order to carfully inspect code and see why mutants survived
 -r REPORT_FILE
 # It is rather well documented https://pypi.org/project/MutPy/