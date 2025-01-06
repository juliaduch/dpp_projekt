import unittest
from functions import dijkstra, round_trip_path, check_node_connections

class TestGraphUtils(unittest.TestCase):
    """
    Unit test class for testing utility functions related to graph operations:
    - dijkstra: Finds the shortest path between nodes in a graph.
    - round_trip_path: Calculates a round-trip path through specified waypoints.
    - check_node_connections: Checks the connections of a specific node in the graph.
    """

    def setUp(self):
        """
        Set up a sample graph as an adjacency list to be used across all test cases.
        """
        self.graph = {
            'A': [('B', 1), ('C', 4)],
            'B': [('A', 1), ('C', 2), ('D', 6)],
            'C': [('A', 4), ('B', 2), ('D', 1)],
            'D': [('B', 6), ('C', 1)],
            'E': []  # Disconnected node
        }

    # Tests for the dijkstra function

    def test_shortest_path_basic(self):
        """
        Test the shortest path calculation for a standard case in the graph.
        """
        path, distance = dijkstra(self.graph, 'A', 'D')
        self.assertEqual(path, ['A', 'B', 'C', 'D'])
        self.assertEqual(distance, 4)

    def test_shortest_path_same_start_end(self):
        """
        Test the case where the start and end nodes are the same.
        """
        path, distance = dijkstra(self.graph, 'A', 'A')
        self.assertEqual(path, ['A'])
        self.assertEqual(distance, 0)

    def test_shortest_path_unreachable_node(self):
        """
        Test the case where the end node is disconnected from the graph.
        """
        path, distance = dijkstra(self.graph, 'A', 'E')
        self.assertEqual(path, ['E'])
        self.assertEqual(distance, float('inf'))

    def test_shortest_path_single_node_graph(self):
        """
        Test the shortest path calculation for a graph with a single node.
        """
        single_node_graph = {'A': []}
        path, distance = dijkstra(single_node_graph, 'A', 'A')
        self.assertEqual(path, ['A'])
        self.assertEqual(distance, 0)

    # Tests for the round_trip_path function

    def test_round_trip_path(self):
        """
        Test the calculation of a round-trip path through multiple waypoints.
        """
        waypoints = ['B', 'C']
        path, cost = round_trip_path(self.graph, 'A', waypoints)
        self.assertEqual(path, ['A', 'B', 'C', 'B', 'A'])
        self.assertEqual(cost, 6)

    def test_round_trip_with_invalid_waypoint(self):
        """
        Test round-trip calculation with a waypoint that does not exist in the graph.
        """
        with self.assertRaises(ValueError):
            round_trip_path(self.graph, 'A', ['B', 'Z'])  # 'Z' does not exist

    # Tests for the check_node_connections function

    def test_check_node_connections_existing(self):
        """
        Test the function for a node that exists in the graph.
        Should print the connections for node 'A'.
        """
        check_node_connections(self.graph, 'A')

    def test_check_node_connections_non_existing(self):
        """
        Test the function for a node that does not exist in the graph.
        Should notify the user that the node is not found.
        """
        check_node_connections(self.graph, 'Z')


if __name__ == "__main__":
    unittest.main()
