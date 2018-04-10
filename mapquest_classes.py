# Kevin Hoang 76963024. Lab Section 11. Project #3.

class STEPS():
    def __init__(self):
        """ Initialize STEPS object with a str header
        """
        self._directions = "\nDIRECTIONS\n"
        
    def generate(self, json_response: "json"):
        """ Generate the str body of the STEPS object
        """
        steps = [ ]
        
        for index in json_response["route"]["legs"]:
            for index2 in index["maneuvers"]:
                steps.append(index2["narrative"])

        for step in steps:
            self._directions += step + "\n"

        return self._directions

        
class TOTALDISTANCE:
    def __init__(self):
        """ Initialize TOTALDISTANCE object with a str 
        """
        self._total_distance = "Total Distance: "
        
    def generate(self, json_response: "json"):
        """ Generate the rest of the TOTALDISTANCE object
        """
        self._total_distance += str(round(json_response["route"]["distance"]))+ \
                                " miles\n"
        
        return self._total_distance
        
        
class TOTALTIME:
    def __init__(self):
        """ Initialize TOTALTIME object with a 
        """
        self._total_time = "Total Time: "

    def generate(self, json_response: "json"):
        """ Generate the rest of the TOTALTIME object 
        """
        self._total_time += str(round(json_response["route"]["time"]/60.0)) + \
                            " minutes\n"
        
        return self._total_time
        
class LATLONG:
    def __init__(self):
        """ Initialize LATLONG object with empty lat_long variable
        """
        self._lat_long = ""
        
    def generate(self, json_response: "json"):
        """ Generate the rest of the LATLONG object by  
        """
        for index in json_response["route"]["locations"]:
            lat_deg = index["latLng"]["lat"]
            if lat_deg < 0:
                lat_deg = str(round(lat_deg * -1, 2))
                latitude = lat_deg + "S "
            else:
                lat_deg = str(round(lat_deg, 2))
                latitude = lat_deg + "N "

            lng_deg = index["latLng"]["lng"]
            if lng_deg < 0:
                lng_deg = str(round(lng_deg * -1, 2))
                longitude = lng_deg + "W "
            else:
                lng_deg = str(round(lng_deg, 2))
                longitude = lng_deg + "E "

            self._lat_long += latitude + longitude + "\n"
        
        return self._lat_long


def generate_outputs(outputs: [str], json_response: "json"):
    for output in outputs:
        print(output.generate(json_response))
