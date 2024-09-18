import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt


def main() -> None:
    # Loading road map with OSMnx
    G_osmnx = ox.graph_from_bbox(39.97,
                                 39.84,
                                 116.46,
                                 116.30,
                                 network_type='drive')

    # For each edge, add the attributes "type" and "length"
    for u, v, k, data in G_osmnx.edges(keys=True, data=True):
        data['type'] = data.get('highway', 'unknown')
        data['length'] = data['length']

    source = list(G_osmnx.nodes())[0]
    target = list(G_osmnx.nodes())[-1]

    # Find the shortest path using the shortest_path function of the NetworkX library
    shortest_path = nx.shortest_path(G_osmnx,
                                     source=source,
                                     target=target,
                                     weight="length")

    # Network visualization using OSMnx
    fig, ax = ox.plot_graph(G_osmnx,
                            edge_color='b',
                            node_color='r',
                            figsize=(10, 10),
                            show=False)

    # Visualize the shortest path
    shortest_path_edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
    shortest_path_graph = nx.Graph()
    shortest_path_graph.add_edges_from(shortest_path_edges)

    ox.plot_graph_route(G_osmnx,
                        shortest_path,
                        ax=ax,
                        route_color='g',
                        route_linewidth=5,
                        route_alpha=0.7,
                        orig_dest_size=100)

    # Get the types of roads to build a histogram
    highway_types = [data['type'] for _, _, data in G_osmnx.edges(data=True)]

    # Convert a list of lists to a flat list
    flat_highway_types = [item for sublist in highway_types for item in sublist]

    # Construct a histogram of the distribution of road types
    plt.figure(figsize=(8, 6))
    plt.hist(flat_highway_types, bins=10, color='b', alpha=0.7)
    plt.xlabel('Highway Type')
    plt.ylabel('Frequency')
    plt.title('Distribution of Highway Types')
    plt.xticks(rotation=45, ha='right')
    plt.show()

    road_lengths = [data['length'] for _, _, data in G_osmnx.edges(data=True)]

    plt.figure(figsize=(8, 6))
    plt.hist(road_lengths, bins=20, color='g', alpha=0.7)
    plt.xlabel('Road Length')
    plt.ylabel('Frequency')
    plt.title('Distribution of Road Lengths')
    plt.show()


if __name__ == '__main__':
    main()
