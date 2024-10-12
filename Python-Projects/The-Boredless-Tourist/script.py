
# This section checks for the index of the destination
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
#"Hyderabad, India"
test_traveler = ["Erin Wilkes", "Shanhai, China", "historical site", "art"]

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index


print(get_destination_index("Los Angeles, USA"))
print(get_destination_index("Paris, France"))
#print(get_destination_index("Hyderabad, India"))


def get_traveler_location(traveler):
    '''This function checks for the index of the travelers location'''
    traveler_destination = traveler[1]
    traveler_destination_index = traveler.index(traveler_destination)
    return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)
