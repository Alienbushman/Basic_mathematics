import requests
url = 'http://localhost:5000/'
json_data =  [{'num_1': 2, 'num_2': 3, 'operation': 'add'},{'num_1': 7, 'num_2': 1, 'operation': 'subtract'}]
response = requests.post(url, json=json_data)
print(response.json())

