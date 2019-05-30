
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

attractions = [[] for num in range(5)]


def get_destination_index(destination):
    try:
        return destinations.index(destination)
    except ValueError:
        return "Enter valid destination"


def get_traveler_location(traveler):
    return get_destination_index(traveler[1])


def add_attraction(destination, attraction):
    try:
        attractions[get_destination_index(destination)].append(attraction)
        return
    except ValueError:
        return "Enter a valid destination"


def find_attractions(destination, interests):
    attractions_in_city = attractions[get_destination_index(destination)]
    attractions_with_interest = []
    for attraction in attractions_in_city:
        attraction_tag = attraction[1]
        for interest in interests:
            if interest in attraction[1]:
                attractions_with_interest.append(attraction[0])
    return attractions_with_interest


def get_attraction_for_traveler(traveler):
    traveler_attractions = find_attractions(traveler[1], traveler[2])
    string1 = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler[1] + ":" + "\n"
    for attraction in traveler_attractions:
        string1 += attraction + "\n"
    return string1


add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
print(get_attraction_for_traveler(test_traveler))
print(get_attraction_for_traveler(["Derek Smill", "Paris, France", ["monument"]]))
print(find_attractions("Los Angeles, USA", ["art"]))
