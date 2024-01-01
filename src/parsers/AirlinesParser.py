class AirlinesParser:
    def __init__(self):
        pass

    def parse(self, data):
        airlines = []
        for line in data:
            airlines.append(Airline(line))
        return airlines


class Airline:
    def __init__(self, data):
        self.airline_id = data[0]
        self.name = data[1]
