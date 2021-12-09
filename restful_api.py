"""This module is responsible for running the Flask restful API to
communicate the the values of basic_math to a localhost on port 5000 """
from flask import Flask, request
from flask_restful import Resource, Api
import basic_math

APP = Flask(__name__)
API = Api(APP)


def verify_list(list1, list2):
    """
    Verifies whether all the elements are in both lists are identical

    Args:
        list1: This is a list with string values
        list2: This is a list with string values

    Returns:
        A boolean whether the lists contain the same values

    Raises:
        None
    """
    return all(elem in list1 for elem in list2)


def convert_data(json_data):
    """
    This converts a json string into a dictionary to process later.

    Args:
        json_data: This is data it accepts in a json format
        an example [{'num_1': 2, 'num_2': 3, 'operation': 'add'}]

    Returns:
        This returns a dictionary with keys:
            num_1: The first number which the program program should apply the operation to
            num_2: The second number the program uses to apply the operation to
            operation: This is the mathematical operation that is used to apply to the numbers given

    Raises:
        KeyError:
            if JSON does not contain the required keys it returns with a json 'message':
            'the json does not contain required fields in the specified format, namely'
            if JSON does not have values stored in the correct
            format for num_1, num_2 or, operation,
            the program returns with a json
             'message': 'could not read in data properly'
    """
    keylist = []
    data = json_data
    dictionary = []
    required_keys = ['num_1', 'num_2', 'operation']
    for key in data[0]:
        keylist.append(key)
    if not verify_list(keylist, required_keys):
        return {'message':
                    'the json does not contain required fields in the spesified format, namely '
                    + str(required_keys)
                }
    try:
        for datapoint in data:
            dictionary.append(
                {'num_1': datapoint['num_1'],
                 'num_2': datapoint['num_2'],
                 'operation': datapoint['operation']})
        return dictionary
    except IndexError:
        return {'message': 'could not read in data properly'}


class ApiManager(Resource):
    '''
    The api which manages the resources for a flask restful api
    which can be used to communicate with

    Attributes
    ----------
    None, this is the format required for the flask restful api standard

    Methods
    -------
    post(self)
        This receives resources when listening on the API and sends it off
        to be converted at convert_data(json_format) and communicates with the basic_math module
    '''
    def post(self):
        '''
        The default flask required format, communicates with requests
        and returns the result of the processing in a json format
        Args:
            Resources from the URL request
        Returns:
            JSON with the function processed with the basic_math module,
            along with a success code (or a message specifying why it could not be processed)
        '''
        json_format = request.get_json()
        converted_format = convert_data(json_format)
        result = []
        functions = {'add': basic_math.adding,
                     'subtract': basic_math.subtraction,
                     'multiplication': basic_math.multiplication,
                     'integer_divide': basic_math.integer_divide,
                     'remainder': basic_math.remainder,
                     'power': basic_math.power,
                     'root': basic_math.root}
        for datapoint in converted_format:
          # todo remove old code
            '''#original fixed to new function for better styling
          if(datapoint['operation']=='add'):
              result.append(BasicMath.adding(datapoint['num_1'],datapoint['num_2']))
          elif(datapoint['operation']=='subtract'):
              result.append(BasicMath.subtraction(datapoint['num_1'],datapoint['num_2']))
          elif(datapoint['operation']=='multiplication'):
              result.append(BasicMath.multiplication(datapoint['num_1'],datapoint['num_2']))
          elif(datapoint['operation']=='integer_divide'):
              result.append(BasicMath.integer_divide(datapoint['num_1'],datapoint['num_2']))
          elif(datapoint['operation']=='remainder'):
              result.append(BasicMath.remainder(datapoint['num_1'],datapoint['num_2']))
          elif(datapoint['operation']=='power'):
              result.append(BasicMath.power(datapoint['num_1'],datapoint['num_2']))
          elif(datapoint['operation']=='root'):
              result.append(BasicMath.root(datapoint['num_1'],datapoint['num_2']))'''
            try:
                result.append(
                    functions[datapoint['operation']]
                    (datapoint['num_1'], datapoint['num_2'])
                )
            except IndexError:
                result.append('operation not supported')

        return result, 201

API.add_resource(ApiManager, '/')
if __name__ == '__main__':
    APP.run(debug=True)
