import heapq
import matplotlib.pyplot as plt
from collections import defaultdict
from api.GraphAlgoInterface import GraphAlgoInterface
from api.GraphInterface import GraphInterface
from implementation.DiGraph import DiGraph
import json
import string
from typing import List, cast


class GraphAlgo(GraphAlgoInterface):

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
                    strg = cast(string, currNode["pos"])
                    splitString = strg.split(',')
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
        dicty = {"Edges": [], "Nodes": []}
        for edge in self.graph.Edges:
            dicty["Edges"].append({"src": self.graph.Edges[edge].getSrc(), "w": self.graph.Edges[edge].getWeight(),
                                   "dest": self.graph.Edges[edge].getDest()})

        for node in self.graph.Nodes:
            dicty["Nodes"].append({"pos": (str(self.graph.Nodes[node].getx()) + "," + str(
                self.graph.Nodes[node].gety()) + "," +
                                           str(self.graph.Nodes[node].getz())), "id": self.graph.Nodes[node].getId()})

        try:
            with open(file_name, 'w') as f:
                json.dump(dicty, indent=2, fp=f)
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
        try:
            if not self.Is_Connected():
                return None, float("inf")
        except:
            print("==> RecursionError: maximum recursion depth exceeded in comparison <==")
            print("Continuing with the code without checking if the Graph is Connected ...")
            pass

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
        i = 0
        j = 0
        plt.style.use("seaborn-whitegrid")
        for currNode in self.graph.Nodes.values():
            if currNode.getx() == -1:
                plt.plot(i, i, markersize=18, marker='o', color="hotpink")
                plt.plot(i, i, currNode.getId(), color="black")
                for currEdge in self.graph.all_out_edges_of_node(currNode.getId()):
                    if self.graph.Nodes[currEdge].getx() == -1:
                        plt.annotate("", xy=(j, j),
                                     xytext=(i, i),
                                     arrowprops=dict(arrowstyle="->", lw=3, alpha=0.7, color="navy"))
                        x = (j + i) / 2
                        y = (j + i) / 2
                        plt.text(x, y,
                                 float("{0:.3f}".format(self.graph.all_out_edges_of_node(currNode.getId())[currEdge])))
                        j = j + 1
                    else:
                        for currEdge in self.graph.all_out_edges_of_node(currNode.getId()):
                            plt.annotate("", xy=(self.graph.Nodes[currEdge].getx(), self.graph.Nodes[currEdge].gety()),
                                         xytext=(i, i),
                                         arrowprops=dict(arrowstyle="->", lw=3, alpha=0.7, color="navy"))
                            x = (self.graph.Nodes[currEdge].getx() + i) / 2
                            y = (self.graph.Nodes[currEdge].gety() + i) / 2
                            plt.text(x, y, float(
                                "{0:.3f}".format(self.graph.all_out_edges_of_node(currNode.getId())[currEdge])))
                i = i + 1
            plt.plot(currNode.getx(), currNode.gety(), markersize=18, marker='o', color="hotpink")
            plt.text(currNode.getx(), currNode.gety(), currNode.getId(), color="black", fontsize=11, fontweight="bold",
                     horizontalalignment='center',
                     verticalalignment='center')
            for currEdge in self.graph.all_out_edges_of_node(currNode.getId()):
                plt.annotate("", xy=(self.graph.Nodes[currEdge].getx(), self.graph.Nodes[currEdge].gety()),
                             xytext=(currNode.getx(), currNode.gety()),
                             arrowprops=dict(arrowstyle="->", lw=3, alpha=0.7, color="navy"))
                x = (self.graph.Nodes[currEdge].getx() + currNode.getx()) / 2
                y = (self.graph.Nodes[currEdge].gety() + currNode.gety()) / 2
                plt.text(x, y, float("{0:.3f}".format(self.graph.all_out_edges_of_node(currNode.getId())[currEdge])))
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.grid(False)
        plt.tight_layout()
        plt.show()

    def Is_Connected(self):
        return self.isStronglyConnected()

    """
    +---------------------------------------------------------------------+
    | Helper functions: [Dijkstra, DFS, IsConnected]                      |
    +---------------------------------------------------------------------+
    """

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

    '''
    +---------------------------------------------------------------------+
    | section of codes that we wrote and didn't use                       |
    +---------------------------------------------------------------------+
    '''

    '''
    def isWeaklyConnected(self):
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
    '''
