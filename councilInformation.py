
URLS = {
    "Daventry": "https://selfserve.daventrydc.gov.uk/forms/postcodechecker.aspx",
    "Northampton": "https://mycouncil.northampton.digital/BinRoundFinder?postcode=",
    "Corby": "https://my.corby.gov.uk/service/Waste_Collection_Date",
    "East Northamptonshire": "https://enc.maps.arcgis.com/apps/MapJournal/index.html?appid=a5dbcdceeea74ca69b2ee6403ab729c5&section=2",
    "Kettering": "https://secure.kettering.gov.uk/site/scripts/documents.php?categoryID=200084",
    "South Northants": "https://www.southnorthants.gov.uk/info/315/bin-collection-search",
    "South Northamptonshire": "https://www.southnorthants.gov.uk/info/315/bin-collection-search",
    "Wellingborough": "https://www.wellingborough.gov.uk/info/200084/bins_rubbish_and_recycling/1115/find_my_bin_collection_day",
        }


def get_council_bin_url(admin_district):
    return URLS[admin_district]