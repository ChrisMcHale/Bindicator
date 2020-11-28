import requests, json
from requests import HTTPError

POSTCODE_LOOKUP_URL = "https://api.postcodes.io/postcodes/"


def get_all_postcode_data(postcode):
    try:
        url_to_get = POSTCODE_LOOKUP_URL + postcode
        response = requests.get(url_to_get)
        response.raise_for_status()
        return response
    except HTTPError as http_err:
        if response.status_code == 404:
            print(f'Sorry, the postcode {postcode} does not exist')
        if response.status_code == 400:
            print(f'HTTP Error {http_err} - Bad Request')
        if response.status_code == 500:
            print(f'HTTP Error {http_err} - Server Error')
        else:
            print(f'HTTP Error {http_err}')
    except Exception as err:
        print(f'Error Occurred: {err}')

