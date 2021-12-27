from unittest import TestCase
from implementation.Node import Node
from implementation.Edge import Edge
from implementation.DiGraph import DiGraph
from implementation.GraphAlgo import GraphAlgo

G1 = GraphAlgo("C:\\Users\\malak\\PycharmProjects\\Ex3_OOP\\json files\\A0.json")

n0 = Node(0, 35.18753053591606, 32.10378225882353, 0.0)
n1 = Node(1, 35.18958953510896, 32.10785303529412, 0.0)
n2 = Node(2, 35.19341035835351, 32.10610841680672, 0.0)
n3 = Node(3, 35.197528356739305, 32.1053088, 0.0)
n4 = Node(4, 35.2016888087167, 32.10601755126051, 0.0)

e0 = Edge(0, 2, 1)
e1 = Edge(0, 1, 1)
e2 = Edge(1, 3, 1)
e3 = Edge(2, 3, 5)
e4 = Edge(3, 2, 5)
e5 = Edge(3, 4, 1)
e6 = Edge(4, 0, 1)

g = DiGraph()
g.add_node(n0.getId(), (n0.getx(), n0.gety(), n0.getz()))
g.add_node(n1.getId(), (n1.getx(), n1.gety(), n1.getz()))
g.add_node(n2.getId(), (n2.getx(), n2.gety(), n2.getz()))
g.add_node(n3.getId(), (n3.getx(), n3.gety(), n3.getz()))
g.add_node(n4.getId(), (n4.getx(), n4.gety(), n4.getz()))

GraphAlgo = GraphAlgo(g)


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        self.fail()

    def test_load_from_json(self):
        for i in G1.graph.Nodes:
            self.assertEqual(G1.graph.Nodes[i].getId(), i)

    def test_save_to_json(self):
        G1.save_to_json("C:\\Users\\malak\\PycharmProjects\\Ex3_OOP\\json files\\SaveTest.json")

    def test_shortest_path(self):
        GraphAlgo.shortest_path(1, 2)


    def test_tsp(self):
        self.fail()

    def test_center_point(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()
