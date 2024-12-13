import unittest
from functions import dijkstra, round_trip_path, check_node_connections


class TestGraphUtils(unittest.TestCase):

    def setUp(self):
        # Graph represented as adjacency list
        self.graph = {
            'A': [('B', 1), ('C', 4)],
            'B': [('A', 1), ('C', 2), ('D', 6)],
            'C': [('A', 4), ('B', 2), ('D', 1)],
            'D': [('B', 6), ('C', 1)],
            'E': []  # Disconnected node
        }

    # test djikstry

    def test_shortest_path_basic(self):
        path, distance = dijkstra(self.graph, 'A', 'D')
        self.assertEqual(path, ['A', 'B', 'C', 'D'])
        self.assertEqual(distance, 4)

    def test_shortest_path_same_start_end(self):
        path, distance = dijkstra(self.graph, 'A', 'A')
        self.assertEqual(path, ['A'])
        self.assertEqual(distance, 0)

    def test_shortest_path_unreachable_node(self):
        path, distance = dijkstra(self.graph, 'A', 'E')
        self.assertEqual(path, ['E'])
        self.assertEqual(distance, float('inf'))

    def test_shortest_path_single_node_graph(self):
        single_node_graph = {'A': []}
        path, distance = dijkstra(single_node_graph, 'A', 'A')
        self.assertEqual(path, ['A'])
        self.assertEqual(distance, 0)

    # test round_trip_path

    def test_round_trip_path(self):
        waypoints = ['B', 'C']
        path, cost = round_trip_path(self.graph, 'A', waypoints)
        self.assertEqual(path, ['A', 'B', 'C', 'B', 'A'])
        self.assertEqual(cost, 6)

    def test_round_trip_with_invalid_waypoint(self):
        with self.assertRaises(ValueError):
            round_trip_path(self.graph, 'A', ['B', 'Z'])  # 'Z' does not exist

    # Test check_node_connections

    def test_check_node_connections_existing(self):
        # This should print the connections
        check_node_connections(self.graph, 'A')

    def test_check_node_connections_non_existing(self):
        # This should notify that the node does not exist
        check_node_connections(self.graph, 'Z')


if __name__ == "__main__":
    unittest.main()
