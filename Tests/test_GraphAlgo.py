from unittest import TestCase
from implementation.Node import Node
from implementation.Edge import Edge
from implementation.DiGraph import DiGraph
from implementation.GraphAlgo import GraphAlgo

GraphAlgo = GraphAlgo(DiGraph())
GraphAlgo.load_from_json("C:\\Users\\malak\\PycharmProjects\\Ex3_OOP\\json files\\A0.json")

n0 = Node(0, 35.18753053591606, 32.10378225882353, 0.0)
n1 = Node(1, 35.18958953510896, 32.10785303529412, 0.0)
n2 = Node(2, 35.19341035835351, 32.10610841680672, 0.0)
n3 = Node(3, 35.197528356739305, 32.1053088, 0.0)
n4 = Node(4, 35.2016888087167, 32.10601755126051, 0.0)
# n5 = Node(5, 1, 1, 1)

e0 = Edge(0, 2, 1)
e1 = Edge(0, 1, 1)
e2 = Edge(1, 3, 1)
e3 = Edge(2, 3, 5)
e4 = Edge(3, 2, 5)
e5 = Edge(3, 4, 1)
e6 = Edge(4, 0, 1)
# e7 = Edge(3, 5, 1)

g = DiGraph()
g.add_node(n0.getId(), (n0.getx(), n0.gety(), n0.getz()))
g.add_node(n1.getId(), (n1.getx(), n1.gety(), n1.getz()))
g.add_node(n2.getId(), (n2.getx(), n2.gety(), n2.getz()))
g.add_node(n3.getId(), (n3.getx(), n3.gety(), n3.getz()))
g.add_node(n4.getId(), (n4.getx(), n4.gety(), n4.getz()))
# g.add_node(n5.getId(), (n5.getx(), n5.gety(), n5.getz()))

g.add_edge(e0.getSrc(), e0.getDest(), e0.getWeight())
g.add_edge(e1.getSrc(), e1.getDest(), e1.getWeight())
g.add_edge(e2.getSrc(), e2.getDest(), e2.getWeight())
g.add_edge(e3.getSrc(), e3.getDest(), e3.getWeight())
g.add_edge(e4.getSrc(), e4.getDest(), e4.getWeight())
g.add_edge(e5.getSrc(), e5.getDest(), e5.getWeight())
g.add_edge(e6.getSrc(), e6.getDest(), e6.getWeight())
# g.add_edge(e7.getSrc(), e7.getDest(), e7.getWeight())

g1 = DiGraph()
GraphAlgo = GraphAlgo(g)

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

g.add_edge(e0.getSrc(), e0.getDest(), e0.getWeight())
g.add_edge(e1.getSrc(), e1.getDest(), e1.getWeight())
g.add_edge(e2.getSrc(), e2.getDest(), e2.getWeight())
g.add_edge(e3.getSrc(), e3.getDest(), e3.getWeight())
g.add_edge(e4.getSrc(), e4.getDest(), e4.getWeight())


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        self.fail()

    def test_load_from_json(self):
        for i in GraphAlgo.graph.Nodes:
            self.assertEqual(GraphAlgo.graph.Nodes[i].getId(), i)

    def test_save_to_json(self):
        GraphAlgo.save_to_json("C:\\Users\\malak\\PycharmProjects\\Ex3_OOP\\json files\\SaveTest.json")

    def test_shortest_path(self):
        self.assertEqual((6.282672154710672, [1, 2, 3, 4, 5]), GraphAlgo.shortest_path(1, 5))

    def test_tsp(self):
        li = [1, 2, 3, 4]
        self.assertEqual(([1, 2, 3, 4], 4.338393158579095), GraphAlgo.TSP(li))

    def test_center_point(self):
        self.assertTrue(GraphAlgo.Is_Connected())
        Id = (GraphAlgo.graph.v_size())
        GraphAlgo.graph.add_node(Id, (1, 2, 3))
        self.assertFalse(GraphAlgo.Is_Connected())
        GraphAlgo.graph.add_edge(0, Id, 1)
        self.assertFalse(GraphAlgo.Is_Connected())

    def test_plot_graph(self):
        self.fail()
