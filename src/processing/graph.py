class Graph:
    def __init__(self, routes):
        self.routes = routes
        self.graph = self.build_graph()

    def build_graph(self):
        graph = {}
        for route in self.routes:
            if route.source_airport not in graph:
                graph[route.source_airport] = []
            graph[route.source_airport].append(route.destination_airport)
        return graph
    
    def get_diameter_path(