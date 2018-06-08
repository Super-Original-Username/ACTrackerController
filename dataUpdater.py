class Updater(object):
    def __init__(self, latitude, longitude, altitude, time):
        self.lat = latitude
        self.lon = longitude
        self.alt = altitude
        self.time = time

    def get_lat(self):
        return self.lat

    def get_lon(self):
        return self.lon

    def get_alt(self):
        return self.alt

    def get_time(self):
        return self.time