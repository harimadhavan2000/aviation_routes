class RoutesParser:
    def __init__(self):
        pass

    def parse(self, data):
        routes = []
        for line in data:
            routes.append(Route(line))
        return routes


class Route:
    # airline	from	to	codeshare	stops	equipment
    def __init__(self, data):
        self.airline = data[0]
        self.source_airport = data[1]
        self.destination_airport = data[2]
        self.codeshare = data[3]
        self.stops = data[4]
        self.equipment = data[5]
