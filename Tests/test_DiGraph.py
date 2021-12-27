from unittest import TestCase
from implementation.Edge import Edge
from implementation.Node import Node
from implementation.DiGraph import DiGraph

n0 = Node(0, 35.18753053591606, 32.10378225882353, 0.0)
n1 = Node(1, 35.18958953510896, 32.10785303529412, 0.0)
n2 = Node(2, 35.19341035835351, 32.10610841680672, 0.0)
n3 = Node(3, 35.197528356739305, 32.1053088, 0.0)
n4 = Node(4, 35.2016888087167, 32.10601755126051, 0.0)

e0 = Edge(0, 1, 1.4004465106761335)
e1 = Edge(0, 10, 1.4620268165085584)  # There is no n10
e2 = Edge(1, 0, 1.8884659521433524)
e3 = Edge(1, 2, 1.7646903245689283)
e4 = Edge(2, 1, 1.7155926739282625)

g = DiGraph()
g.add_node(n0.getId(), (n0.getx(), n0.gety(), n0.getz()))
g.add_node(n1.getId(), (n1.getx(), n1.gety(), n1.getz()))
g.add_node(n2.getId(), (n2.getx(), n2.gety(), n2.getz()))
g.add_node(n3.getId(), (n3.getx(), n3.gety(), n3.getz()))
g.add_node(n4.getId(), (n4.getx(), n4.gety(), n4.getz()))

g.add_edge(e0.getSrc(), e0.getDest(), e0.getWeight())
g.add_edge(e1.getSrc(), e1.getDest(), e1.getWeight())
g.add_edge(e2.getSrc(), e2.getDest(), e2.getWeight())
g.add_edge(e3.getSrc(), e3.getDest(), e3.getWeight())
g.add_edge(e4.getSrc(), e4.getDest(), e4.getWeight())


class TestDiGraph(TestCase):
    def test_v_size(self):
        self.assertEqual(g.v_size(), 5)

    def test_e_size(self):
        self.assertEqual(g.e_size(), 4)

    def test_get_all_v(self):
        dictionary = dict()
        dictionary[0] = n0
        dictionary[1] = n1
        dictionary[2] = n2
        dictionary[3] = n3
        dictionary[4] = n4
        self.assertEqual(g.get_all_v().keys(), dictionary.keys())

    def test_all_in_edges_of_node(self):
        dictionary = dict()
        dictionary[1] = e2.getWeight()
        self.assertEqual(dictionary, g.all_in_edges_of_node(0))

    def test_all_out_edges_of_node(self):
        dictionary = dict()
        dictionary[0] = e2.getWeight()
        dictionary[2] = e3.getWeight()
        self.assertEqual(dictionary, g.all_out_edges_of_node(1))

    def test_get_mc(self):
        self.assertEqual(9, g.get_mc())

    def test_add_edge(self):
        e5 = Edge(2, 3, 1.1435447583365383)
        e6 = Edge(10, 3, 1.1435447583365383)
        self.assertTrue(g.add_edge(e5.getSrc(), e5.getDest(), e5.getWeight()))
        self.assertFalse(g.add_edge(e6.getSrc(), e6.getDest(), e6.getWeight()))

    def test_add_node(self):
        n5 = Node(5, 35.20582803389831, 32.10625380168067, 0.0)
        self.assertTrue(g.add_node(n5.getId(), (n5.getx(), n5.gety(), n5.getz())))

    def test_remove_node(self):
        self.assertTrue(g.remove_node(0))

    def test_remove_edge(self):
        self.assertTrue(g.remove_edge(e0.getSrc(), e0.getDest()))
        self.assertFalse(g.remove_edge(e1.getSrc(), e1.getDest()))
