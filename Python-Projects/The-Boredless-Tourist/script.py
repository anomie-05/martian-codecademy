
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

# Visiting Interesting Places

attractions = []
for detination in destinations:
    attractions.append([])



def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
    return

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#print(attractions)

# Finding the best places to go
#attractions_with_interest = []
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest


la_arts = find_attractions("Los Angeles, USA", ["art"])
print(la_arts)

# See The Parts of a City You want to See

def get_attraction_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interestests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interestests)
    interests_string = (f"Hi {traveler[0]}, we think you'll like these places around {traveler_destination}: "
                        f"the {traveler_attractions}.")
    return interests_string

smills_france = get_attraction_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)