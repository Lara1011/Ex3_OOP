from api.GraphAlgoInterface import GraphAlgoInterface
from api.GraphInterface import GraphInterface
from DiGraph import DiGraph
import json
import string
from typing import List,cast

class GraphAlgo(GraphAlgoInterface):

    def __init__(self,graph):
        if graph == None :
            graph = DiGraph()
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
       try:
           data = json.load(open(file_name))
           pos = False
           for currNode in data["Nodes"]:
               if "pos" in currNode:
                   str = cast(string,currNode["pos"])
                   splitString = str.split(',')
                   self.graph.add_node(currNode["id"],(float(splitString[0]),float(splitString[1]),float(splitString[2])))
               else:
                   self.graph.add_node(currNode["id"])
           for currEdge in data["Edges"]:
               self.graph.add_edge(currEdge["src"],currEdge["dest"],currEdge["w"])
           return True
       except Exception as e:
           print(e)
           return False

    def save_to_json(self, file_name: str) -> bool:
        dict = {"Nodes" : [], "Edges" : []}
        for node in self.graph.Nodes:
            dict["Nodes"].append({"id" : node.getId(),"pos" : node.getx()+","+node.gety()+","+node.getz()})
        for edge in self.graph.Edges:
            dict["Edges"].append({"src" : edge.getSrc(), "dest" : edge.getDest(), "w" : edge.getWeight()})

        try:
            with open(file_name,'w') as f:
                json.dump(dict,indent = 2,fp = f)
            return True
        except Exception as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
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
