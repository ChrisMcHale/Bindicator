import requests, scrollphathd as sphd, time
from requests import HTTPError

URL = "https://mycouncil.northampton.digital/BinRoundFinder?postcode="


def get_bin_collection_data(postcode):
    try:
        url_to_get = URL + parse_postcode(postcode)
        response = requests.get(url_to_get)
        response.raise_for_status()
        json_response = response.json()
        type_string = json_response["type"]
        if type_string == "brown":
            type_string = "Garden & Recycling"
        if type_string == "black":
            type_string = "General Rubbish"
        show_on_display(json_response["day"] + " : " + type_string)
    except HTTPError as http_err:
        print(f'HTTP Error Occurred: {http_err}')
    except Exception as err:
        print(f'Error Occurred: {err}')


def show_on_display(string):
    sphd.rotate(180)
    sphd.write_string(string + " ")
    while True:
        sphd.show()
        sphd.scroll(1)
        time.sleep(0.05)


def parse_postcode(postcode):
    pc = postcode
    pc = pc.strip()
    pc = pc.lower()
    pc = pc.replace(" ", "")
    return pc


def parse_json(json):
    return json


if __name__ == "__main__":
    get_bin_collection_data(" NN49fa")
