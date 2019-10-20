"""This is a basic example of a request"""
import requests


def run_request():
    """
    This runs a small example request

    Args:
        None
    Returns:
        Returns json status from the restful_api
    """
    url = 'http://localhost:5000/'
    json_data = [{'num_1': 2, 'num_2': 3, 'operation': 'add'},
                 {'num_1': 7, 'num_2': 1, 'operation': 'subtract'}]
    response = requests.post(url, json=json_data)
    return response.json()


print(run_request())
