
def ground_shipping(weight):

    if weight > 10:
        return 4.75 * weight + 20
    elif weight > 6:
        return 4.00 * weight + 20
    elif weight > 2:
        return 3.00 * weight + 20
    else:
        return 2.5 * weight + 20


def premium_shipping():

    return 125


def drone_shipping(weight):

    if weight > 10:
        return 14.25 * weight
    elif weight > 6:
        return 12 * weight
    elif weight > 2:
        return 9 * weight
    else:
        return 4.5 * weight


def get_cheapest(weight):

    ground = ground_shipping(weight)
    premium = premium_shipping()
    drone = drone_shipping(weight)

    if ground < premium and ground < drone:
        return "Ground is cheapest"
    elif premium < ground and premium < drone:
        return "Premium is cheapest"
    elif drone < premium and drone < ground:
        return "Drone is cheapest"
    else:
        return "Some of the price values are the same"


weight_user = input("Enter the weight of your package. ")
weight_convert = float(weight_user)
print("Ground Shipping Cost: ", ground_shipping(weight_convert))
print("Premium Shipping Cost: ", premium_shipping())
print("Drone Shipping Cost: ", drone_shipping(weight_convert))
print(get_cheapest(weight_convert))
