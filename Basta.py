class Menu:

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start = start_time
        self.end = end_time

    def __repr__(self):
        return "The {MENU} menu is available between {START} and {END}".format(MENU=self.name, START=self.start, END=self.end)

    def calculate_bill(self, purchased_items):
        amount = 0
        for item in purchased_items:
            amount += self.items.get(item)
        return "The total price of your purchase is ${PRICE}".format(PRICE=amount)


class Franchise:

    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return "This franchise is located at {ADDRESS}".format(ADDRESS=self.address)

    def available_menus(self, time):
        available = []
        for menu in self.menus:
            if (time > menu.start) and (time < menu.end):
                available.append(menu.name)
        if available == []:
            print("There are no menus available at this time.")
            return
        print ("The following menus are available at this time:")
        for item in available:
            print(item)


class Business:

    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

# CREATE MENUS
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu("Brunch", brunch_items, 1100, 1600)

early_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early = Menu("Early", early_items, 1500, 1800)

dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu("Dinner", dinner_items, 1700, 2300)

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu("Kids", kids_items, 1100, 2100)

# CREATE FRANCHISES
MAMS = Franchise("85 Prescott", {brunch, dinner, kids})
WPI = Franchise("100 Institute", {early, dinner, kids})

MAMS.available_menus(2400)

Worcester = Business("Worcester", [MAMS, WPI])
