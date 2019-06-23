number_list = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_value = "New York City"

def linear_search(search_list, target_value):
    matches = []
    for idx in range(len(search_list)):
        print(search_list[idx])
        if target_value == search_list[idx]:
            matches.append(idx)
    if matches != []:
        return matches
    else:
        raise ValueError("{0} not in list".format(target_value))

try:
    result = linear_search(number_list, target_value)
    print(result)
except ValueError as error_message:
    print("{0}".format(error_message))

