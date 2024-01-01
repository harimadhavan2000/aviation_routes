from parsers import (
    AirlinesParser,
    AirportsParser,
    AlliancesParser,
    RoutesParser,
    EquipmentsParser,
)
from utils import read_file
from pathlib import Path

import networkx as nx

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

    airlines_parser = AirlinesParser.AirlinesParser()
    airports_parser = AirportsParser.AirportsParser()
    alliances_parser = AlliancesParser.AlliancesParser()
    equipment_parser = EquipmentsParser.EquipmentsParser()
    routes_parser = RoutesParser.RoutesParser()

    airlines = airlines_parser.parse(airlines_data)
    airports = airports_parser.parse(airports_data)
    alliances = alliances_parser.parse(alliances_data)
    equipment = equipment_parser.parse(equipment_data)
    routes = routes_parser.parse(routes_data)

    routes_tuples = routes_parser.get_routes_tuples(routes)
    graph = nx.Graph(routes_tuples)
    Gcc = sorted(nx.connected_components(graph), key=len, reverse=True)
    G0 = graph.subgraph(Gcc[0])
    # diameter = nx.diameter(G0) = 13
    n1, n2 = nx.periphery(G0)  # LPS PTJ
    diameter_nodes = nx.shortest_path(G0, source=n1, target=n2)
    for node in diameter_nodes:
        print(airports_parser.get_airport_name_from_code(node, airports))


if __name__ == "__main__":
    main()
