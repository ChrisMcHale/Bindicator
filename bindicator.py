import requests, scrollphathd
from requests import HTTPError

URL = "https://mycouncil.northampton.digital/BinRoundFinder?postcode="


def get_bin_collection_data(postcode):
    try:
        url_to_get = URL + parse_postcode(postcode)
        response = requests.get(url_to_get)
        response.raise_for_status()
        json_response = response.json()
        print(json_response)
        scrollphathd.write_string("blaj", x=0, y=0, font=None, letter_spacing=1, brightness=1.0)
        scrollphathd.show()

    except HTTPError as http_err:
        print(f'HTTP Error Occurred: {http_err}')
    except Exception as err:
        print(f'Error Occurred: {err}')


def parse_postcode(postcode):
    pc = postcode
    pc = pc.strip()
    pc = pc.lower()
    pc = pc.replace(" ", "")
    return pc


def parse_json(json):
    return json


if __name__ == "__main__":
    get_bin_collection_data(" NN4 9fa")
