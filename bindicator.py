import postcodeTools as pcT
import councilInformation as cI
import councils.northampton as northampton

def get_bin_collection_data(postcode):
    postcode_response = pcT.get_all_postcode_data(parse_postcode(postcode))
    postcode_json = postcode_response.json()
    admin_district = postcode_json["result"]["admin_district"]
    if not admin_district:
        print(f"Unable to locate council for postcode {postcode}")
    else:
        print(f"Council for postcode {postcode} is {admin_district}")
    print(f"The URL for {admin_district} is {cI.get_council_bin_url(admin_district)}")
    print(f"Your bin collection is {northampton.get_bin_collection_data(cI.get_council_bin_url(admin_district), postcode)}")

def parse_postcode(postcode):
    pc = postcode
    pc = pc.strip()
    pc = pc.lower()
    pc = pc.replace(" ", "")
    return pc


def parse_json(json):
    return json


if __name__ == "__main__":
    get_bin_collection_data("nn49fa")
