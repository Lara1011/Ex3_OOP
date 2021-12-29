from unittest import TestCase
from implementation.Node import Node
from implementation.Edge import Edge
from implementation.DiGraph import DiGraph
from implementation.GraphAlgo import GraphAlgo

# GraphAlgo.load_from_json("C:\\Users\\malak\\PycharmProjects\\Ex3_OOP\\json files\\A0.json")
G0 = GraphAlgo(DiGraph())
G1 = GraphAlgo(DiGraph())
G2 = GraphAlgo(DiGraph())
G3 = GraphAlgo(DiGraph())
G4 = GraphAlgo(DiGraph())
G5 = GraphAlgo(DiGraph())
G6 = GraphAlgo(DiGraph())

# Lara's Macbook
"""""
G0.load_from_json("/Users/laraabu/PycharmProjects/Ex3_OOP/json files/A0.json")
G1.load_from_json("/Users/laraabu/PycharmProjects/Ex3_OOP/json files/A1.json")
G2.load_from_json("/Users/laraabu/PycharmProjects/Ex3_OOP/json files/A2.json")
G3.load_from_json("/Users/laraabu/PycharmProjects/Ex3_OOP/json files/A3.json")
G4.load_from_json("/Users/laraabu/PycharmProjects/Ex3_OOP/json files/A4.json")
G5.load_from_json("/Users/laraabu/PycharmProjects/Ex3_OOP/json files/A5.json")
G6.load_from_json("/Users/laraabu/PycharmProjects/Ex3_OOP/json files/T0.json")
"""""
# Malak's Laptop
G0.load_from_json("C:\\Users\\malak\\PycharmProjects\\Ex3_OOP\\json files\\A0.json")
G1.load_from_json("C:\\Users\\malak\\PycharmProjects\\Ex3_OOP\\json files\\A1.json")
G2.load_from_json("C:\\Users\\malak\\PycharmProjects\\Ex3_OOP\\json files\\A2.json")
G3.load_from_json("C:\\Users\\malak\\PycharmProjects\\Ex3_OOP\\json files\\A3.json")
G4.load_from_json("C:\\Users\\malak\\PycharmProjects\\Ex3_OOP\\json files\\A4.json")
G5.load_from_json("C:\\Users\\malak\\PycharmProjects\\Ex3_OOP\\json files\\A5.json")
G6.load_from_json("C:\\Users\\malak\\PycharmProjects\\Ex3_OOP\\json files\\T0.json")

n0 = Node(0, 35.18753053591606, 32.10378225882353, 0.0)
n1 = Node(1, 35.18958953510896, 32.10785303529412, 0.0)
n2 = Node(2, 35.19341035835351, 32.10610841680672, 0.0)
n3 = Node(3, 35.197528356739305, 32.1053088, 0.0)
n4 = Node(4, 35.2016888087167, 32.10601755126051, 0.0)
n5 = Node(5, 1, 1, 1)

e0 = Edge(0, 2, 1)
e1 = Edge(0, 1, 1)
e2 = Edge(1, 3, 1)
e3 = Edge(2, 3, 5)
e4 = Edge(3, 2, 5)
e5 = Edge(3, 4, 1)
e6 = Edge(4, 0, 1)
e7 = Edge(3, 5, 1)

g = DiGraph()
g.add_node(n0.getId(), (n0.getx(), n0.gety(), n0.getz()))
g.add_node(n1.getId(), (n1.getx(), n1.gety(), n1.getz()))
g.add_node(n2.getId(), (n2.getx(), n2.gety(), n2.getz()))
g.add_node(n3.getId(), (n3.getx(), n3.gety(), n3.getz()))
g.add_node(n4.getId(), (n4.getx(), n4.gety(), n4.getz()))
g.add_node(n5.getId(), (n5.getx(), n5.gety(), n5.getz()))

g.add_edge(e0.getSrc(), e0.getDest(), e0.getWeight())
g.add_edge(e1.getSrc(), e1.getDest(), e1.getWeight())
g.add_edge(e2.getSrc(), e2.getDest(), e2.getWeight())
g.add_edge(e3.getSrc(), e3.getDest(), e3.getWeight())
g.add_edge(e4.getSrc(), e4.getDest(), e4.getWeight())
g.add_edge(e5.getSrc(), e5.getDest(), e5.getWeight())
g.add_edge(e6.getSrc(), e6.getDest(), e6.getWeight())
g.add_edge(e7.getSrc(), e7.getDest(), e7.getWeight())

g1 = DiGraph()
GraphAlgo = GraphAlgo(g)


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        for i in G0.get_graph().get_all_v().keys():
            self.assertEqual(G0.graph.Nodes[i].getId(), i)
        for i in G1.get_graph().get_all_v().keys():
            self.assertEqual(G1.graph.Nodes[i].getId(), i)
        for i in G2.get_graph().get_all_v().keys():
            self.assertEqual(G2.graph.Nodes[i].getId(), i)
        for i in G3.get_graph().get_all_v().keys():
            self.assertEqual(G3.graph.Nodes[i].getId(), i)
        for i in G4.get_graph().get_all_v().keys():
            self.assertEqual(G4.graph.Nodes[i].getId(), i)
        for i in G5.get_graph().get_all_v().keys():
            self.assertEqual(G5.graph.Nodes[i].getId(), i)
        for i in G6.get_graph().get_all_v().keys():
            self.assertEqual(G6.graph.Nodes[i].getId(), i)

    def test_load_from_json(self):
        for i in G0.graph.Nodes:
            self.assertEqual(G0.graph.Nodes[i].getId(), i)
        for i in G1.graph.Nodes:
            self.assertEqual(G1.graph.Nodes[i].getId(), i)
        for i in G2.graph.Nodes:
            self.assertEqual(G2.graph.Nodes[i].getId(), i)
        for i in G3.graph.Nodes:
            self.assertEqual(G3.graph.Nodes[i].getId(), i)
        for i in G4.graph.Nodes:
            self.assertEqual(G4.graph.Nodes[i].getId(), i)
        for i in G5.graph.Nodes:
            self.assertEqual(G5.graph.Nodes[i].getId(), i)
        for i in G6.graph.Nodes:
            self.assertEqual(G6.graph.Nodes[i].getId(), i)

    def test_save_to_json(self):
        # GraphAlgo.save_to_json("C:\\Users\\malak\\PycharmProjects\\Ex3_OOP\\json files\\SaveTest.json")
        G0.save_to_json("/Users/laraabu/Downloads/LargeConnectedGraphs/SaveTest.json")

    def test_shortest_path(self):
        self.assertEqual((2, [1, 3, 5]), GraphAlgo.shortest_path(1, 5))

    def test_tsp(self):
        lst0 = []
        for i in range(0, 11):
            lst0.append(i)
        self.assertEqual(([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14.470852790366884), G0.TSP(lst0))

        lst1 = []
        for i in range(0, 17):
            lst1.append(i)
        self.assertEqual(([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 22.63446693792369), G1.TSP(lst1))

        lst2 = []
        for i in range(0, 31):
            lst2.append(i)
        self.assertEqual(([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 14, 17, 18, 19, 20, 11, 10, 9,
                           23, 22, 21, 22, 23, 24, 25, 26, 8, 7, 27, 7, 6, 5, 28, 29, 28, 5, 6, 7, 8, 9, 10, 11, 20,
                           30], 64.53058547292315), G2.TSP(lst2))

        lst3 = []
        for i in range(0, 49):
            lst3.append(i)
        self.assertEqual(([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 39, 17, 18, 19, 20, 11, 10, 9,
                           23, 22, 21, 22, 23, 24, 25, 26, 8, 7, 27, 7, 6, 5, 28, 29, 28, 4, 3, 31, 30, 31, 32, 33, 34,
                           35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48], 83.76023223512816), G3.TSP(lst3))

        lst4 = []
        for i in range(0, 40):
            lst4.append(i)
        self.assertEqual(([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                           26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], 61.57069709465682), G4.TSP(lst4))

        lst5 = []
        for i in range(0, 48):
            lst5.append(i)
        self.assertEqual(([0, 1, 9, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                           26, 27, 28, 29, 30, 31, 32, 21, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47],
                          64.69479090028206), G5.TSP(lst5))

        lst6 = []
        for i in range(0, 4):
            lst6.append(i)
        self.assertEqual(([0, 1, 2, 3], 3.4), G6.TSP(lst6))

    def test_center_point(self):
        self.assertEqual((7, 6.806805834715163), G0.centerPoint())
        self.assertEqual((8, 9.925289024973141), G1.centerPoint())
        self.assertEqual((0, 7.819910602212574), G2.centerPoint())
        self.assertEqual((2, 8.182236568942237), G3.centerPoint())
        self.assertEqual((6, 8.071366078651435), G4.centerPoint())
        self.assertEqual((40, 9.291743173960954), G5.centerPoint())
        self.assertEqual((None, float("inf")), G6.centerPoint())

    def test_plot_graph(self):
        G0.plot_graph()
        G1.plot_graph()
        G2.plot_graph()
        G3.plot_graph()
        G4.plot_graph()
        G5.plot_graph()
        G6.plot_graph()

    def test_isStronglyConnected(self):
        self.assertTrue(G0.isStronglyConnected())
        self.assertTrue(G1.isStronglyConnected())
        self.assertTrue(G2.isStronglyConnected())
        self.assertTrue(G3.isStronglyConnected())
        self.assertTrue(G4.isStronglyConnected())
        self.assertTrue(G5.isStronglyConnected())
        self.assertFalse(G6.isStronglyConnected())
