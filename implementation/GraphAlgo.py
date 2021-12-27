from api.GraphAlgoInterface import GraphAlgoInterface
from api.GraphInterface import GraphInterface
from DiGraph import DiGraph
import json
import string
from typing import List, cast
from queue import PriorityQueue


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph):
        if graph == None:
            graph = DiGraph()
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
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
        dict = {"Nodes": [], "Edges": []}
        for node in self.graph.Nodes:
            dict["Nodes"].append({"id": node.getId(), "pos": node.getx() + "," + node.gety() + "," + node.getz()})
        for edge in self.graph.Edges:
            dict["Edges"].append({"src": edge.getSrc(), "dest": edge.getDest(), "w": edge.getWeight()})

        try:
            with open(file_name, 'w') as f:
                json.dump(dict, indent=2, fp=f)
            return True
        except Exception as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        l1 = shortestPath(self.graph, id1, id2)
        sum1 = sum(l1)
        return sum1, l1

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


def Dijkstra(G, src, dest):
    D = {}  # dictionary of final distances
    P = {}  # dictionary of predecessors
    Q = PriorityQueue()  # estimated distances of non-final vertices
    Q.put((0.0, src))

    for v in Q:
        D[v] = Q[v]
        if v == dest:
            break

        for w in G[v]:
            vwLength = D[v] + G[v][w]
            if w in D:
                if vwLength < D[w]:
                    raise ValueError("Dijkstra: found better path to already-final vertex")
            elif w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v

    return (D, P)


def shortestPath(G, start, end):
    D, P = Dijkstra(G, start, end)
    Path = []
    while 1:
        Path.append(end)
        if end == start:
            break
        end = P[end]
    Path.reverse()
    return Path
