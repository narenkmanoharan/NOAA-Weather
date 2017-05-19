class Location(object):

    # Location object to initialize the latitude and longitude
    def __init__(self):
        self.latitude = None
        self.longitude = None

    # setter for latitude
    def set_latitude(self, latitude):
        self.latitude = latitude

    # getter for latitude
    def get_latitude(self):
        return self.latitude

    # setter for longitude
    def set_longitude(self, longitude):
        self.longitude = longitude

    # getter for longitude
    def get_longitude(self):
        return self.longitude
