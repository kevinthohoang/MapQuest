# Kevin Hoang 76963024. Lab Section 11. Project #3.

import json
import mapquest_classes
import urllib.parse
import urllib.request

MAPQUEST_API_KEY  = "GET A KEY"
BASE_MAPQUEST_URL = "http://open.mapquestapi.com"

def build_mapquest_url(locations: [str]) -> str:
    """ Build and return a mapquest URL that can be used to interact with the mapquest
        API. Mapquest URL combines base url, API key, and encoded location search query
    """
    search_parameters = [("from", locations[0])]

    for index in range(len(locations) - 1):
        search_parameters.append(("to", locations[index + 1]))
    
    return BASE_MAPQUEST_URL + "/directions/v2/route?key=" + \
           MAPQUEST_API_KEY + "&" + urllib.parse.urlencode(search_parameters)

def get_result(url: str) -> "json":
    """ Given a mapquest URL, return a Python object representing the parsed JSON
        response.
    """
    json_response = None

    try:
        json_response = urllib.request.urlopen(url)
        json_text = json_response.read().decode(encoding = "utf-8")

        return json.loads(json_text)
    
    finally:
        if json_response != None:
            json_response.close()
