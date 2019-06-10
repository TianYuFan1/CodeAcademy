class Art:

    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return "{NAME}. \"{TITLE}\". {YEAR}, {MEDIUM}. {OWNERN}, {OWNERL}.".format(NAME=self.artist, TITLE=self.title, YEAR=self.year, MEDIUM=self.medium, OWNERN=self.owner.name, OWNERL=self.owner.location)


class Marketplace:

    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, remove_listing):
        self.listings.remove(remove_listing)

    def show_listings(self):
        for listing in self.listings:
            print(listing)


class Client:

    def __init__(self, name, location="Private Collection", is_museum=False):
        self.name = name
        self.location = location
        self.is_museum = is_museum

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            art_list = Listing(artwork, price, self.name)
            veneer.add_listing(art_list)

    def buy_artwork(self, artwork):
        if artwork.owner == self:
            return "You already own this artwork"
        art_listing = None
        for listing in veneer.listings:
            if listing.art == artwork:
                art_listing = listing
                break
        artwork.owner = self
        veneer.remove_listing(art_listing)


class Listing:

    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return "{NAME} is selling {ART}".format(NAME=self.seller, ART=self.art.title)


# Create Client
john = Client("John Smith")
MAMS = Client("MAMS", "Worcester", True)

# Create Art Object
girl = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", "1910", john)
print(girl)

# Create Marketplace Object
veneer = Marketplace()
veneer.show_listings()

john.sell_artwork(girl, "6M")

veneer.show_listings()
MAMS.buy_artwork(girl)

print(girl)
veneer.show_listings()