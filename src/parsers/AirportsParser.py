class AirportsParser:
    def __init__(self):
        pass

    def parse(self, data):
        airports = []
        for line in data:
            airports.append(Airport(line))
        return airports

    def get_airport_name_from_code(self, code, airports):
        for airport in airports:
            if airport.airport_id == code:
                return airport.name
        return None


class Airport:
    # airport-id	latitude	longitude	airport-name
    def __init__(self, data):
        self.airport_id = data[0]
        self.latitude = data[1]
        self.longitude = data[2]
        self.name = data[3]
