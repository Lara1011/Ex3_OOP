# Ex3_OOP
----

### Directed weighted graph - Python :
In this project we implemented a directed weighted graph. Reading from json file or manually adding nodes,edges etc. <br>

### Packages :
- __Images :__ In this package you will find UML image, running time images. <br>
- __Tests :__ In this package contains Junit tests for each class. <br>
- __api :__ In this package you will find all Interfaces and main class to test your implementation. <br>
- __implementation :__ In this package you will find our implementation classes for the 2 interfaces, in addition to Node and Edge class. <br>
- __json files :__ In this package we have json files to test `load(String file)` method. <br>
---

### Classes :
1) __Edge :__ This class contains the source,destination and weight of this edge.
2) __Node :__ This class contains the id,position(x,y,z),dictionary of edges out and dictionary of edges in of the node.
3) __DiGraph :__ This class implements GraphInterface, it contains two dictionaries, one for the nodes and the other is for the edges, it also contains an counter named MC (short for Mode Count) that counts the changes made in graph.
4) __GraphAlgo :__ This class implements GraphAlgoInterface, it contains a DiGraph(directed weighted graph) that we implemented. <br> In this class we implemented some algorithms for searching shortest path,tsp, etc.
---

### UML:
![UML](https://github.com/Lara1011/Ex3_OOP/blob/2e1f5d5f1ccb5f19a953f229103371f0ac47a482/Images/UML.png)
---

### Algorithms:
- [Dijkstra Algorithm ](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm): Dijkstra's original algorithm found the shortest path between two given nodes.
- [Depth-First Search ](https://en.wikipedia.org/wiki/Depth-first_search): (DFS) is an algorithm for traversing or searching tree or graph data structures,  and takes time O(|V| + |E|).
- [Travelin Salesman Problem ](https://en.wikipedia.org/wiki/Travelling_salesman_problem): (TSP) asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?" It is an NP-hard problem in combinatorial optimization, important in theoretical computer science and operations research.
---

### Performance Analysis :
| GraphSize | TSP |	Center | IsConnected |
|-----------|-----|--------|-------------|
|    A0     | 2ms |  4ms   |     3ms     |
|    A1   	| 5ms |  3ms   |     1ms     |
|    A2     |10ms |  13ms  |     2ms     |
|    A3   	|35ms |  54ms  |     42ms    |
|    A4     |12ms |  39ms  |     41ms    |
|    A5   	|36ms |  41ms  |     39ms    |
|    T0     |10ms |  2ms   |     3ms     |
|   1000    |2.258sec|5.545sec|     10ms     | 
|   10000   |8mins,12sec|        |     *     |
|   100000  ||        |     *     |
