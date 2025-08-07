class Edge:
    def __init__(self, target, weight):
        self.target= target
        self.weight= weight

class Vertex:
    def __init__(self, label):
        self.label= label
        self.edges= []

class Graph:
    def __init__(self):
        self.vertices={} # vertices are stored in a dictionary where by each key represents a start point and the value represents the destination for each start point
    
    def add_location(self, label):
        if label not in self.vertices:
            self.vertices[label] = Vertex(label)

    def remove_location(self, label):
        if label in self.vertices:
            # remove all edges pointing to this vertex
            for vertex in self.vertices.values():
                vertex.edges = [edge for edge in vertex.edges if edge.target.label != label] # keep all edges where the target is not the one we're trying to remove
            # remove the vertex itself
            del self.vertices[label]
    
    def add_roads(self, _from, _to, weight):
        # check if the vertex we need to connect from and the vertex we need to connet to are present in the list of vertices, if yes, do the following:
        if _from in self.vertices and _to in self.vertices: 
            from_vertex = self.vertices[_from] # assign the label of the vertex - which we're connecting from - to the variable from_vertex
            to_vertex= self.vertices[_to] # assing the label of the vertex - which we're connecting to - to the variable to_vertex
            from_vertex.edges.append(Edge(to_vertex, weight)) # when appending this newly formed edge to the graph, give a weight like the user wants

    def remove_roads(self, _from, _to):
        # check if the vertices from and to are in the list of vertices
        if _from in self.vertices and _to in self.vertices:
            from_vertex = self.vertices[_from] # assign the label of the vertex - which we're connecting from - to the variable from_vertex
            # update the list of edges to hold all the available edges except the one that needs to be deleted
            # to remove the edge, loop through the list of edges
            # keep all edges where the target is not the one we're trying to remove
            from_vertex.edges = [ 
            edge for edge in from_vertex.edges if edge.target.label != _to
        ] 

    def dijkstra(self, source_label, target_label):
        distances={} # create a dictionary to store the shortest distances from source to all vertices
        for label in self.vertices:
            distances[label] = float('inf') # set the distance for each vertex to infinity as we don't know yet the distance
        distances[source_label] = 0 # set the distance of the source vertex to 0 because this is the starting point

        visited=set() # create an empty set to keep track of visited vertices

        while len(visited) < len(self.vertices): # as long as not all the vertices where visited, hence the length of the visited will be shorter than the actual list of vertices
            current= None # this variable is used to name the current vertex we're working on
            shortest_distance =float ('inf') # set the shortest_distance variable to be initially infinity, again because we don't know its actual distance

            for label in self.vertices: # loop through the list of vertices
                if label not in visited and distances[label] <shortest_distance: # if this vertex was not visited before and the distance to it is shorter than the shortest distance discovered so far:
                    shortest_distance= distances[label] # update the shortest distance to be this short distance
                    current= label # set this vertex as the current one

            if current is None:
                break

            visited.add(current) # add current ot the visited list to mark visited

            for edge in self.vertices[current].edges: # loop through each edge in the current vertex
                neighbor= edge.target.label # call the label of the target for that edge the neighbor
                weight = edge.weight # call the weight of this edge weight

                if neighbor not in visited: 
                    new_distance= distances[current] + weight # the distance of this new path is the distance between the previos vertices plus the distance to this new vertex (neighbor) and assign the sum to new_distance

                    if new_distance < distances[neighbor]: # if the new distance is shorter than the recorded one:
                        distances[neighbor] = new_distance # update the distance to this neighbor
            
        return distances[target_label] # once the loop is over, return the distance to the target label


    def reachable_locations(self, start_label):
        visited= set()
        queue=[] # create a queue for a BFS
        queue.append(start_label) # to start from the starting point, add the starting label to the queue

        while queue:
            current= queue.pop(0) # pop the first element in the queue and assign it to current
            if current not in visited: # if this vertex hasn't been visited before, add it to the visited set
                visited.add(current)
                for edge in self.vertices[current].edges: # loop through the edges of the current location
                    queue.append(edge.target.label) # add the label of the vertex which the edge points to
        return visited 




# create vertices
graph = Graph()
graph.add_location("Mall")
graph.add_location("Park")
graph.add_location("Hotel")
graph.add_location("Gym")
graph.add_location("School")
graph.add_location("Hospital")

# create edges with weights
graph.add_roads("Park", "Mall", 5)
graph.add_roads("Mall", "Hotel", 8)
graph.add_roads("Gym", "Mall", 7)
graph.add_roads("Hotel", "Hospital", 4)
graph.add_roads("Hospital", "Gym", 6)
graph.add_roads("School", "Park", 3)
graph.add_roads("Park", "School", 3)
graph.add_roads("School", "Hotel", 9)
graph.add_roads("Hotel", "Park", 5)
graph.add_roads("Gym", "School", 6)


print(graph.dijkstra("School", "Hospital"))
print(graph.reachable_locations("Mall"))
