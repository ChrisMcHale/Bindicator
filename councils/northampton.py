import requests
from requests import HTTPError


def get_bin_collection_data(url, postcode):
    return_string = ""
    try:
        url_to_get = url + postcode
        response = requests.get(url_to_get)
        response.raise_for_status()
        json_response = response.json()
        type_string = json_response["type"]
        if type_string == "brown":
            type_string = "Garden & Recycling"
        if type_string == "black":
            type_string = "General Rubbish"
        return_string = (json_response["day"] + " : " + type_string)
    except HTTPError as http_err:
        print(f'HTTP Error Occurred: {http_err}')
    except Exception as err:
        print(f'Error Occurred: {err}')
    return return_string
