# Basic_mathematics
This is a repository to showcase some basic functions by extrapolating the +1 and -1 function into a basic calculator ([inspired by a Feynman lecture](https://www.feynmanlectures.caltech.edu/I_22.html) ). 

This is mainly a showcase for taking a basic project and integrating it with everything you would want in an end-end project (Docker, CI/CD, Restful API, static code analysis, unit tests, coverage).

# Overview of the structure
The code for the project can be accessed via the project of basic_math.py as demonstrated with unit tests in basic_math_test.py <br />
Alternatively, you can access the project via API by editing the JSON data in the requst.py file once the API is up and running (see the 'Accessing the project via API' section)

# Accessing the project via API
### Running the script
Run the API with the command
```
python restful_api.py
```

Then to access the running API
```
python request.py
```
This will return a list of numbers which are the result of the JSON payload in request.py
### Editing the function
To edit the execution, edit the request.py script's variable 'json_data' so that it follows the structure
```
[{'num_1': int, 'num_2': int, 'operation': 'valid_function_name'}]
```
for example
```
    json_data = [{'num_1': 2, 'num_2': 3, 'operation': 'add'},
                 {'num_1': 7, 'num_2': 1, 'operation': 'subtract'}]
```
The valid functions names are ['add', 'subtract', 'multiplication', 'integer_divide', 'remainder', 'power', 'root']



# An example of running the docker image

To expose the restful API from within the docker container 
```
docker build -t python-barcode . 
docker run --network="host" python-barcode 
```

To test the dependencies you can also run the API without exposing the network from outside the container with the following commands
```
docker build -t python-barcode . 
docker run python-barcode
```
# Temporary dependency management with pipenv
If you would like to run the project with the dependencies in a virtual environment, you can use pipenv with the following two commands
```
pipenv install
pipenv shell 
```
# Unit tests
Run the unit tests
```
coverage  run basic_math_test.py
```
to view the report you can either get the results with
```
coverage report
```
or view a more detailed report with the following command (this highlights which functions were run)
```
coverage html
```
# Test the quality of the code quality of code
```
pylint <python_filename.py>
e.g.
pylint basic_math.py
```

# To read the documentation of a function use pydoc
To write out the documentation for function use the following format
```
python -m pydoc -w <filename>
e.g.
python -m pydoc -w restful_api
```
or view all the functions via browser use
```
python -m pydoc -p 5433
```
