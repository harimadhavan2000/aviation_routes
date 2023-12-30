from .parsers import (
    # al_parser,
    AirportsParser,
    # aln_parser,
    # rt_parser,
    # eq_parser,
)
from processing import graph
from utils import read_file
from pathlib import Path

current_path = Path(__file__).parent.absolute()

airlines_data_path = current_path / "../resources/airlines.dat"
airports_data_path = current_path / "../resources/airports.dat"
alliances_data_path = current_path / "../resources/alliances.dat"
equipment_data_path = current_path / "../resources/equipment.dat"
routes_data_path = current_path / "../resources/routes.dat"


def main():
    airlines_data = read_file(airlines_data_path)
    airports_data = read_file(airports_data_path)
    alliances_data = read_file(alliances_data_path)
    equipment_data = read_file(equipment_data_path)
    routes_data = read_file(routes_data_path)

    print(airports_data[0:10])
    # airlines_parser = AirlinesParser(airlines_data)
    airports_parser = AirportsParser.AirportsParser().parse(airports_data)
    # alliances_parser = AlliancesParser(alliances_data)
    # equipment_parser = EquipmentsParser(equipment_data)
    # routes_parser = RoutesParser(routes_data)

    # airlines = airlines_parser.parse()
    # airports = airports_parser.parse()
    # alliances = alliances_parser.parse()
    # equipment = equipment_parser.parse()
    # routes = routes_parser.parse()

    # graph = graph.Graph(airlines, airports, alliances, equipment, routes)


if __name__ == "__main__":
    main()
