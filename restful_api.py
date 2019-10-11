from flask import Flask,request
from flask_restful import Resource, Api
import sys
import BasicMath

app = Flask(__name__)
api = Api(app)
def verify_list(list1,list2):
    return all(elem in list1 for elem in list2)

def convert_data(json_data):
    keylist=[]
    data=json_data
    dictionary = []
    required_keys=['num_1','num_2','operation']
    for key in data[0]:
        keylist.append(key)
    if (not verify_list(keylist,required_keys)):
        return {'message':'the json does not contain required fields in the spesified format, namely '+str(required_keys)}
    try:
    	for datapoint in data:
            dictionary.append(
                {'num_1': datapoint['num_1'], 'num_2': datapoint['num_2'], 'operation': datapoint['operation']})
    	return dictionary
    except:
        return {'message': 'could not read in data properly'}

class api_manager(Resource):
    def post(self):
        json_format=request.get_json()
        converted_format = convert_data(json_format)
        result=[]
        functions = {'add': BasicMath.adding,'subtract':BasicMath.subtraction,'multiplication':BasicMath.multiplication,'integer_divide':BasicMath.integer_divide,'remainder':BasicMath.remainder,
        'power':BasicMath.power,'root':BasicMath.root}
        for datapoint in converted_format:
        	try:
        		result.append(functions[datapoint['operation']](datapoint['num_1'],datapoint['num_2']))
        	except:
        		result.append('operation not supported')

        	'''
        	#original fixed to new function for better styling
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
        		result.append(BasicMath.root(datapoint['num_1'],datapoint['num_2']))
			'''
        return result, 201

api.add_resource(api_manager,'/')
if __name__== '__main__':
	app.run(debug=True)