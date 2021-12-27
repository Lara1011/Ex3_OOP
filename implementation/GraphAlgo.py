from api.GraphAlgoInterface import GraphAlgoInterface
from api.GraphInterface import GraphInterface
from implementation.Node import Node
from implementation.Edge import Edge
from implementation.DiGraph import DiGraph
import json
import string
from typing import List, cast


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph):
        if graph == None:
            graph = DiGraph()
        self.graph = graph

    def __init__(self, json_file: str):
        self.load_from_json(json_file)

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            graph = DiGraph()
            self.graph = graph
            data = json.load(open(file_name))
            for currNode in data["Nodes"]:
                if "pos" in currNode:
                    str = cast(string, currNode["pos"])
                    splitString = str.split(',')
                    self.graph.add_node(currNode["id"],
                                        (float(splitString[0]), float(splitString[1]), float(splitString[2])))
                else:
                    self.graph.add_node(currNode["id"])
            for currEdge in data["Edges"]:
                self.graph.add_edge(currEdge["src"], currEdge["dest"], currEdge["w"])
            return True
        except Exception as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        dict = {"Edges": [], "Nodes": []}
        for edge in self.graph.Edges:
            dict["Edges"].append({"src": self.graph.Edges[edge].getSrc(), "w": self.graph.Edges[edge].getWeight(),
                                  "dest": self.graph.Edges[edge].getDest()})

        for node in self.graph.Nodes:
            dict["Nodes"].append({"pos": (str(self.graph.Nodes[node].getx()) + "," + str(
                self.graph.Nodes[node].gety()) + "," +
                                          str(self.graph.Nodes[node].getz())), "id": self.graph.Nodes[node].getId()})

        try:
            with open(file_name, 'w') as f:
                json.dump(dict, indent=2, fp=f)
            return True
        except Exception as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        raise NotImplementedError

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        raise NotImplementedError


if __name__ == '__main__':
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
