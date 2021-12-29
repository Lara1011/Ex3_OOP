# Ex3_OOP
----

### Directed weighted graph - Python :

In this project we implemented a directed weighted graph. Reading from json file or manually adding nodes,edges
etc. <br>

### Packages :

- __Images :__ This package contains UML image, running time images. <br>
- __Tests :__ This package contains Junit tests for each class. <br>
- __api :__ This package contains all the Interfaces and the main class to test the implementation. <br>
- __implementation :__ This package contains our implementation classes for the 2 interfaces, in addition to
  Node and Edge class. <br>
- __json files :__ This package contains json files to test `load(String file)` method. <br>

---

### Classes :

1) __Edge :__ This class contains the source, destination and weight of this edge.
2) __Node :__ This class contains the id, position(x,y,z), dictionary of edges out and dictionary of edges in of the node.
3) __DiGraph :__ This class implements GraphInterface, it contains two dictionaries, one for the nodes and the other is
   for the edges, it also contains an counter named MC (short for Mode Count) that counts the changes made in graph.
4) __GraphAlgo :__ This class implements GraphAlgoInterface, it contains a DiGraph(directed weighted graph) that we
   implemented. <br> In this class we implemented some algorithms for searching shortest-path, tsp, etc.

---

### UML:

![UML](https://github.com/Lara1011/Ex3_OOP/blob/2e1f5d5f1ccb5f19a953f229103371f0ac47a482/Images/UML.png)
---

### Algorithms:

- [Dijkstra Algorithm ](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm): Dijkstra's original algorithm found the
  shortest path between two given nodes.
- [Depth-First Search ](https://en.wikipedia.org/wiki/Depth-first_search): (DFS) is an algorithm for traversing or
  searching tree or graph data structures, and takes time O(|V| + |E|).
- [Travelin Salesman Problem ](https://en.wikipedia.org/wiki/Travelling_salesman_problem): (TSP) asks the following
  question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route
  that visits each city exactly once and returns to the origin city?" It is an NP-hard problem in combinatorial
  optimization, important in theoretical computer science and operations research.

---

### Performance Analysis :

#### MacBook Pro [`CPU: 2.9 GHz Dual-Core Intel Core i5-6267U, Memory: 8 GB, GPU: Intel Iris Graphics 550`]

| GraphSize | TSP       | Center     | IsConnected     | Shortest Path (between 1->10) |
|-----------|-----------|------------|-----------------|-------------------------------|
| A0        | 2 ms      | 4 ms       | 3 ms            | 3 ms                          |
| A1        | 5 ms      | 3 ms       | 1 ms            | 4 ms                          |
| A2        | 10 ms     | 13 ms      | 2 ms            | 6 ms                          |
| A3        | 35 ms     | 54 ms      | 42 ms           | 3 ms                          |
| A4        | 12 ms     | 39 ms      | 41 ms           | 4 ms                          |
| A5        | 36 ms     | 41 ms      | 39 ms           | 2 ms                          |
| T0        | 10 ms     | 2 ms       | 3 ms            | 3 ms                          |
| 1000      | 2.258 sec | 5.545 sec  | 10 ms           | 24 ms                         |
| 10000     | 8.12 mins | 19.28 mins | RecursionError! | 212 ms                        |
| 100000    | *         | *          | RecursionError! | 5.370 sec                     |

<br>

#### MSI Laptop [`CPU: 2.60 GHz up to 4.5 GHz Intel Core i7-9750H 2.59 GHz, Memory: 16 GB, GPU: NVIDIA GeForce GTX 1660 Ti`]

| GraphSize | TSP       | Center     | IsConnected     | Shortest Path (between 1->10) |
|-----------|-----------|------------|-----------------|-------------------------------|
| A0        | 2 ms      | 3 ms       | 3 ms            | 2 ms                          |
| A1        | 3 ms      | 3 ms       | 1 ms            | 1 ms                          |
| A2        | 4 ms      | 4 ms       | 2 ms            | 3 ms                          |
| A3        | 8 ms      | 8 ms       | 3 ms            | 2 ms                          |
| A4        | 5 ms      | 6 ms       | 2 ms            | 2 ms                          |
| A5        | 7 ms      | 9 ms       | 2 ms            | 2 ms                          |
| T0        | 1 ms      | 3 ms       | 1 ms            | 2 ms                          |
| 1000      | 1.79 sec  | 3.81 sec   | 4 ms            | 155 ms                        |
| 10000     | 3.54 mins | 10.12 mins | RecursionError! | 201 ms                        |
| 100000    | *         | too long   | RecursionError! | 2.297 sec                     |