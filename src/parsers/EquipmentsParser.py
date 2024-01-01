class EquipmentsParser:
    def __init__(self):
        pass

    def parse(self, data):
        equipments = []
        for line in data:
            equipments.append(Equipment(line))


class Equipment:
    # alliance-name list-of-airlines
    def __init__(self, data):
        self.name = data[0]
        self.airlines = data[1]
