import heapq
import sys
from collections import defaultdict
from api.GraphAlgoInterface import GraphAlgoInterface
from api.GraphInterface import GraphInterface
from implementation.Node import Node
from implementation.Edge import Edge
from implementation.DiGraph import DiGraph
import json
import string
from typing import List, cast


class GraphAlgo(GraphAlgoInterface):
    #  sys.setrecursionlimit(10**6)
    def __init__(self, graph: DiGraph = None):
        if graph == None:
            graph = DiGraph()
        self.graph = graph

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
        return self.Dijkstra(id1, id2)

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """
        if len(node_lst) == 0:
            return [], float("inf")
        if len(node_lst) == 1:
            return node_lst, 0
        nodes = node_lst
        shortestPath = self.shortest_path(nodes.pop(0), nodes.pop(0))
        path = []
        weight = 0
        weight = weight + shortestPath[0]
        path = path + shortestPath[1]
        while nodes:
            currNode = nodes.pop(0)
            if currNode in path:
                continue
            if len(path) != 0:
                shortestPath = self.shortest_path(path.pop(len(path) - 1), currNode)
                weight = weight + shortestPath[0]
                path = path + shortestPath[1]
        return path, weight


    def centerPoint(self) -> (int, float):
            """
            Finds the node that has the shortest distance to it's farthest node.
            :return: The nodes id, min-maximum distance
            """
            center = 0
            minMaxWeight = float("inf")
            for node in self.graph.get_all_v():
                maximum = 0
                distance = self.Dijkstra_v2(node)
                for dest in distance.values():
                    if maximum < dest:
                        maximum = dest
                temp = maximum
                if temp < minMaxWeight:
                    center = node
                    minMaxWeight = temp
            return center, minMaxWeight

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """

    #########################################################################
    #########################################################################
    def Dijkstra_v2(self, src: int):
        distance = defaultdict(lambda: float('inf'))
        prev = {}
        visited = set()
        list_ = []
        distance[src] = 0
        heapq.heappush(list_, (0, src))
        if self.graph.e_size() == 0:
            return float('inf'), []
        while list_:
            s = heapq.heappop(list_)
            node, dist = s[1], s[0]
            visited.add(node)
            for neighbor, weight in self.graph.all_out_edges_of_node(node).items():
                if neighbor in visited:
                    continue
                updateDist = dist + weight
                if distance[neighbor] > updateDist:
                    prev[neighbor] = node
                    distance[neighbor] = updateDist
                    heapq.heappush(list_, (updateDist, neighbor))
        dictionary = dict()
        for key in distance:
            dictionary[key] = distance.get(key)
        return dictionary

    def Dijkstra(self, src: int, dest: int):
        distance = defaultdict(lambda: float('inf'))
        prev = {}
        visited = set()
        list_ = []
        distance[src] = 0
        heapq.heappush(list_, (0, src))
        if self.graph.e_size() == 0:
            return float('inf'), []
        while list_:
            s = heapq.heappop(list_)
            node, dist = s[1], s[0]
            visited.add(node)
            for neighbor, weight in self.graph.all_out_edges_of_node(node).items():
                if neighbor in visited:
                    continue
                updateDist = dist + weight
                if distance[neighbor] > updateDist:
                    prev[neighbor] = node
                    distance[neighbor] = updateDist
                    heapq.heappush(list_, (updateDist, neighbor))

        if dest not in distance:
            return float('inf'), []

        path = list()
        index = dest
        path.append(index)
        while index != src:
            index = prev.get(index)
            path.insert(0, index)
        if dest in distance:
            weight = distance.get(dest)
        else:
            return float('inf'), []
        return weight, path

    #########################################################################
    #########################################################################

    # DFS function
    def dfsIn(self, node, graphIn: dict, vis1):
        vis1[node] = True
        if node not in graphIn:
            graphIn[node] = {}

        for currNode in graphIn[node]:
            if (not vis1[currNode]):
                self.dfsIn(currNode, graphIn, vis1)

    # DFS function
    def dfsOut(self, node, graphOut: dict, vis2):
        vis2[node] = True

        if node not in graphOut:
            graphOut[node] = {}

        for currNode in graphOut[node]:
            if (not vis2[currNode]):
                self.dfsOut(currNode, graphOut, vis2)

    def Is_Connected(self):
        graphIn = dict()
        graphOut = dict()
        for node in self.graph.Nodes:
            graphIn[node] = list(self.graph.all_in_edges_of_node(node).keys())
            graphOut[node] = list(self.graph.all_out_edges_of_node(node).keys())

        vis1 = [0] * (self.graph.v_size())
        vis2 = [0] * (self.graph.v_size())

        # Call for correct direction
        vis1 = [False] * len(vis1)
        self.dfsIn(0, graphIn, vis1)

        # Call for reverse direction
        vis2 = [False] * len(vis2)
        self.dfsOut(0, graphOut, vis2)

        for i in range(0, self.graph.v_size()):

            # If any vertex it not visited in any direction
            # Then graph is not connected
            if (not vis1[i] and not vis2[i]):
                return False

        # If graph is connected
        return True

    #########################################################################
    #########################################################################

    def DFSUtil(self, node, visited, graph):
        visited[node] = True
        for i in graph[node]:
            if visited[i] == False:
                self.DFSUtil(i, visited, graph)

    def isStronglyConnected(self) -> bool:
        graphIn = dict()
        graphOut = dict()

        visited = [False] * (self.graph.v_size())
        for node in self.graph.Nodes:
            graphIn[node] = list(self.graph.all_in_edges_of_node(node).keys())
            graphOut[node] = list(self.graph.all_out_edges_of_node(node).keys())

        self.DFSUtil(0, visited, graphIn)

        if any(i == False for i in visited):
            return False

        visited = [False] * (self.graph.v_size())

        self.DFSUtil(0, visited, graphOut)

        if any(i == False for i in visited):
            return False

        return True


#########################################################################
#########################################################################


if __name__ == '__main__':
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
    #GraphAlgo.load_from_json("C:\\Users\\malak\\PycharmProjects\\Ex3_OOP\\json files\\A1.json")
    #GraphAlgo.load_from_json("C:\\Users\\malak\\OneDrive\\Desktop\\LargeConnectedGraphs\\10000Nodes.json")
    GraphAlgo.load_from_json("/Users/laraabu/PycharmProjects/Ex3_OOP/json files/A1.json")

    # print(GraphAlgo.shortest_path(1, 8))
    #print(GraphAlgo.centerPoint())
    lst = []
    for i in range(0, 17):
        lst.append(i)
    print(GraphAlgo.TSP(lst))