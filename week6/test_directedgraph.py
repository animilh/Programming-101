import unittest
from directedgraph import DirectedGraph


class TestDiretectedGraph(unittest.TestCase):

    def setUp(self):
        self.g = DirectedGraph()
        self.node_a = 'A'
        self.node_b = 'B'
        self.node_c = 'C'

    def test_instance_of_DirectedGraph(self):
        self.assertIsInstance(self.g, DirectedGraph)

    def test_has_node_in_DirectedGraph(self):
        self.g.add_node(self.node_a)
        self.assertIn(self.node_a, self.g.network)

    def test_node_not_in_DirectedGraph(self):
        self.assertNotIn(self.node_a, self.g.network)

    def test_add_node_in_DirectedGraph(self):
        self.g.add_node(self.node_a)
        self.assertIn(self.node_a, self.g.network)

    def test_add_edge_for_two_nodes_in_DirectedGraph(self):
        self.g.add_edge(self.node_a, self.node_b)
        self.assertIn(self.node_b, self.g[self.node_a])

    def test_get_neighbors_for_node_in_DirectedGraph(self):
        neighbors = [self.node_b]
        self.g.add_edge(self.node_a, self.node_b)
        self.assertTrue(self.g.get_neighbors_for(self.node_a) == neighbors)

    def test_get_neighbors_for_node__not_in_DirectedGraph(self):
        with self.assertRaises(KeyError):
            self.g.get_neighbors_for(self.node_c)

    def test_has_path_between_nodes_in_DirectedGraph(self):
        self.g.add_edge(self.node_a, self.node_b)
        self.g.add_edge(self.node_b, self.node_c)
        self.assertTrue(self.g.path_between(self.node_a, self.node_c))

    def test_no_path_between_nodes_in_DirectedGraph(self):
        self.g.add_node(self.node_a)
        self.g.add_node(self.node_c)
        self.assertFalse(self.g.path_between(self.node_a, self.node_c))

    def test_no_path_between_nodes_not_in_DirectedGraph(self):
        self.assertFalse(self.g.path_between(self.node_a, self.node_c))

    def test_get_path_between_nodes_in_DirectedGraph(self):
        path = ['A', 'B', 'C']
        self.g.add_edge(self.node_a, self.node_b)
        self.g.add_edge(self.node_b, self.node_c)
        self.assertEqual(self.g.get_path_between(self.node_a, self.node_c), \
            path)

    def test_get_path_between_non_related_nodes_in_DirectedGraph(self):
        self.assertEqual(self.g.get_path_between(self.node_a, self.node_c), \
            None)

if __name__ == '__main__':
    unittest.main()
