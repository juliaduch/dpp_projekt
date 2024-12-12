import unittest
from functions import dijkstra

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

if __name__ == "__main__":
    unittest.main()
