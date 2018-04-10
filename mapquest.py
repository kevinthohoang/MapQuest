# Kevin Hoang 76963024. Lab Section 11. Project #3.

import mapquest_interact
import mapquest_classes

def get_locations() -> [str]:
    """ Prompt the user for locations
    """
    locations = [ ]
    
    try:
        amount = int(input())
        
        if amount == 2 or amount > 2:
            for loops in range(amount):
                address = input()
                locations.append(address)
            return locations
        else:
            print("You must specify at least two locations to run this program.")
    except:
        print("The first line must specify a positive integer number of locations.")

    
def get_outputs() -> [str]:
    """ Prompt the user for desired outputs
        Valid outputs are locate in possible_output
    """
    outputs = [ ]

    try:
        amount = int(input())

        if amount == 1 or amount > 1:
            for loops in range(amount):
                output = input()

                if _check_output(output) == True:
                    outputs.append(_create_object(output))
                else:
                    print("Invalid output type: {}".format(output))
            return outputs
    except:
        print("There must be a positive integer number of outputs.")

def _check_output(output: str) -> bool:
    """ Check to see if user's desired output action is valid
    """
    possible_output = ["STEPS", "TOTALDISTANCE", "TOTALTIME", "LATLONG"]
    
    if output in possible_output:
        return True
    else:
        return False

def _create_object(output:str) -> "mapquest class":
    """
    """
    if output == "STEPS":
        return mapquest_classes.STEPS()
    if output == "TOTALDISTANCE":
        return mapquest_classes.TOTALDISTANCE()
    if output == "TOTALTIME":
        return mapquest_classes.TOTALTIME()
    if output == "LATLONG":
        return mapquest_classes.LATLONG()

def copyright_message() -> None:
    """ Display copyright message to indicate that the information provided is issued
        by MapQuest services
    """
    print("\nDirections Courtesy of Mapquest; Map Data Copyright OpenStreetMapContributors.")

if __name__ == "__main__":
    locations = get_locations()
    if locations != None:
        outputs   = get_outputs()
        if outputs != [ ]:
            mapquest_url  = mapquest_interact.build_mapquest_url(locations)
            json_response = mapquest_interact.get_result(mapquest_url)
            try:
                mapquest_classes.generate_outputs(outputs, json_response)
                copyright_message()
            except:
                print("The most common cause for this is one of your locations does not exist or",
                      "was not specified in a format that MapQuest supports")
