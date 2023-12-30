class AlliancesParser:
    def __init__(self):
        pass

    def parse(self, data):
        alliances = []
        for line in data:
            alliances.append(Alliance(**data))


class Alliance:
    # alliance-name list-of-airlines
    def __init__(self, data):
        self.name = data[0]
        self.airlines = data[1]

    @staticmethod
    def get_alliance_from_airline(airline):
        pass