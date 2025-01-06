import heapq
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start, end):
    """
    Implements Dijkstra's algorithm to find the shortest path 
    between two nodes in a graph.

    Args:
        graph (dict): The graph represented as a dictionary where keys 
                      are nodes and values are lists of tuples 
                      (neighbor, weight).
        start (str): The starting node.
        end (str): The target node.

    Returns:
        tuple: A pair consisting of a list of nodes representing the shortest 
               path and the total cost of this path.
    """
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous_nodes[node]

    path.reverse()
    return path, distances[end]


def round_trip_path(graph, start, waypoints):
    """
    Finds a round-trip path through specified waypoints, 
    returning to the starting node.

    Args:
        graph (dict): The graph represented as a dictionary.
        start (str): The starting node.
        waypoints (list): List of intermediate nodes to visit.

    Returns:
        tuple: A pair containing the full path (list of nodes) and total cost.
    """
    full_path = []
    total_cost = 0

    current_start = start
    for waypoint in waypoints:
        if waypoint not in graph:
            raise ValueError(f"Node {waypoint} does not exist in the graph.")

        path, cost = dijkstra(graph, current_start, waypoint)
        if full_path:
            full_path.extend(path[1:])
        else:
            full_path.extend(path)
        total_cost += cost
        current_start = waypoint

    path, cost = dijkstra(graph, current_start, start)
    full_path.extend(path[1:])
    total_cost += cost

    return full_path, total_cost


def check_node_connections(graph, node):
    """
    Checks the outgoing connections from a given node in the graph.

    Args:
        graph (dict): The graph represented as a dictionary.
        node (str): The node for which connections will be checked.

    Returns:
        None
    """
    if node not in graph:
        print(f"Node {node} does not exist in the graph.")
        return
    connections = graph[node]
    if not connections:
        print(f"Node {node} has no outgoing connections.")
    else:
        print(f"Connections for node {node}:")
        for neighbor, weight in connections:
            print(f" - {neighbor} (weight: {weight})")


def visualize_graph(start_node, static_graph, waypoints):
    """
    Visualizes the graph with the round-trip path highlighted.

    Args:
        start_node (str): The starting node.
        static_graph (dict): The graph represented as a dictionary.
        waypoints (list): List of intermediate nodes to visit.

    Returns:
        None
    """
    if start_node in static_graph and all(wp in static_graph for wp in waypoints):
        try:
            path, cost = round_trip_path(static_graph, start_node, waypoints)
            print(
                f"The shortest round-trip path from {start_node}, through {waypoints}, "
                f"back to {start_node}: {path} with a total cost of {cost}")

            G = nx.Graph()

            for node, edges in static_graph.items():
                for neighbor, weight in edges:
                    G.add_edge(node, neighbor, weight=weight)

            pos = nx.spring_layout(G)

            node_colors = []
            for node in G.nodes:
                if node == start_node:
                    node_colors.append('#98FB98')
                elif node in waypoints:
                    node_colors.append('#FFD700')
                elif node in path:
                    node_colors.append('#ADD8E6')
                else:
                    node_colors.append('#D3D3D3')

            plt.figure(figsize=(12, 8))
            nx.draw(G, pos, with_labels=True, node_color=node_colors,
                    node_size=600, font_size=10)
            labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(
                G, pos, edgelist=G.edges, edge_color='black')
            nx.draw_networkx_edges(
                G, pos, edgelist=path_edges, edge_color='red', width=2)

            plt.title("Graph with Highlighted Round-Trip Path")
            plt.show()
        except ValueError as e:
            print(e)
        else:
            print("Invalid nodes provided.")
