# City Route Planner

This project implements a directed, weighted graph to represent locations in a city and the roads connecting them. It provides key graph operations such as adding/removing locations (vertices), adding/removing roads (edges), computing the shortest path between two locations using Dijkstra's algorithm, and finding all reachable locations from a starting point using Breadth-First Search (BFS).

## Features

- Add and remove locations
- Add and remove roads with weights (representing distances or travel times)
- Find the shortest path between two locations (Dijkstra)
- Discover all reachable locations from a starting point (BFS)

## Example Use Case

This program can simulate real-world applications such as GPS navigation, city traffic planning, or logistics routing. For instance, given a list of city locations and roads with travel distances, it helps find the shortest path from one place to another or identify all places reachable from a specific location.


## Sample Output
print(graph.dijkstra("School", "Hospital"))
output: 13
print(graph.reachable_locations("Mall"))
output: {'Park', 'Hotel', 'School', 'Mall', 'Hospital', 'Gym'}
