from graphviz import Digraph 

INF = 99999


class Graph:  # Behaves like a directional acyclic graph
    def __init__(self):
        self.nodes = {}
        self.numPeople = 0

    def add_person(self, person):
        if person not in self.nodes:
            self.numPeople += 1
            self.nodes[person] = set()

    def add_edge(self, p1, p2):
        self.nodes[p1].add(p2)

def display_graph(web):
    dot = Digraph()
    ids = {}  # name - > letter ID (n)
    n = "A"
    for person in web.nodes:  # Give everyone a node
        ids[person] = n
        dot.node(ids[person], person)
        if n != "Z":
            n = chr(ord(n) + 1)
        else:
            n = chr(ord("a"))
    for person in web.nodes:  # Draw lines between friends
        for friend in web.nodes[person]:
            print(person + " -> " + friend)
            dot.edges([ids[person] + ids[friend]])
    print(dot.source)
    dot.render('friends.gv', view=True)

def display_dict(dist):

    for i in dist:
        for n in dist:
            if dist[i][n] != 0 and dist[i][n] != INF:
                print("From " + i + " to " + n + " are " + str(dist[i][n]) + " people")

def floyd_warshall(graph):
    V = graph.nodes.keys()
    dist = {}

    for v1 in V:
        dist[v1] = {}
        for v2 in V:
            dist[v1][v2] = INF
    for vertex in V:
        dist[vertex][vertex] = 0
        for friend in graph.nodes[vertex]:
            print(vertex+ "->" + friend)
            dist[vertex][friend] = 1

    for k in V:
        for i in V:
            for j in V:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    display_dict(dist)

if __name__ == '__main__':
    web = Graph()
    
    n = 7
    for i in range(n):
        f = open("./data/" + "data" + str(i) + ".txt", "r")
        print(f)
        temp = [x.strip("\n") for x in f.readlines()]
        current = temp[0]  # First name in the file indicates who's most messaged people we're retrieving
        web.add_person(current)
        for j in range(1, len(temp)):
            friend = temp[j]
            web.add_person(friend)
            web.add_edge(current, friend)
    display_graph(web)
    floyd_warshall(web)
