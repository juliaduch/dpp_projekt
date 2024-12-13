import heapq

def dijkstra(graph, start, end):
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
    full_path = []
    total_cost = 0

    current_start = start
    for waypoint in waypoints:
        if waypoint not in graph:
            raise ValueError(f"Wierzchołek {waypoint} nie istnieje w grafie.")

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
