import sys
from collections import deque

# Creating Node Class

class Node:
    def __init__(self, name, cum_cost, d, f):
        self.name = name
        self.parents = None
        self.cum_cost = cum_cost
        self.d = d
        self.f = f

class Uninformed_search:

    def find_route(self, start, goal):

# Reading input file and storing the values in List of Arrays

        input_file = sys.argv[1]
        f = open(input_file, "r")
        routes = []
        visited = []
        for line in f:
            if "END OF INPUT" in line:
                break
            else:
                cities = line.split()
                sources = cities[0]
                destinations = cities[1]
                distance = cities[2]
                route1 = [sources, destinations, distance]
                route2 = [destinations, sources, distance]
                routes.append(route1)
                routes.append(route2)

# Initializing queue and adding Node with source to the queue
        fringe = deque()
        fringe.append(Node(start, 0, 0, None))
        nodes_expanded = 0
        goalnotfound = False
        while True:
            if len(fringe) != 0:

# Popping the first element of the queue and checking if it is the goal state

                node_expanded = fringe.popleft()
                nodes_expanded += 1
                if node_expanded.name == goal:
                    break
                else:
# Adding the node to the visited list if it is not it visited list and expanding the node to generate it's successors

                    if node_expanded.name not in visited:
                        visited.append(node_expanded.name)
                        for value in routes:
                            if value[0] == node_expanded.name:
                                n = Node(value[1], node_expanded.cum_cost+int(value[2]), node_expanded.d+1, None)
                                n.parents= node_expanded
                                fringe.append(n)
                                s=sorted(fringe, key=lambda node:node.cum_cost)
                                fringe=deque(s)
            else:
                goalnotfound = True
                break

# Printing the route information and number of nodes expanded

        if(goalnotfound == True):
            print ("Nodes Expanded: "+str(nodes_expanded))
            print ("Distance: Infinity")
            print ("Route: None")
        else:
            print ("Nodes Expanded: "+str(nodes_expanded))
            print ("Distance: " + str(node_expanded.cum_cost))
            print ("Route: ")
            path = []
            path.append(goal)
            while node_expanded.parents != None:
                path.append(node_expanded.parents.name)
                node_expanded = node_expanded.parents
            path.reverse()
            i=0
            while i < len(path)-1:
                for v in routes:
                    if path[i]==v[0] and path[i+1] == v[1]:
                        print (v[0] +" to "+ v[1]+ " - "+v[2])
                i += 1


class Informed_search:

    def find_route(self, start, goal):
        input_file = sys.argv[1]
        heuristicfile = sys.argv[4]
        f = open(input_file, "r")
        h = open(heuristicfile, "r")
        routes = []
        heuristics = []
        visited = []
        for line in h:
            if "END OF INPUT" in line:
                break
            else:
                heuristic = line.split()
                hcity = heuristic[0]
                hvalue = heuristic[1]
                heuristics.append([hcity, hvalue])

        for line in f:
            if "END OF INPUT" in line:
                break
            else:
                cities = line.split()
                sources = cities[0]
                destinations = cities[1]
                distance = cities[2]
                route1 = [sources, destinations, distance]
                route2 = [destinations, sources, distance]
                routes.append(route1)
                routes.append(route2)
        fringe = deque()
        fringe.append(Node(start, 0, 0, 0))
        nodes_expanded=0
        goalnotfound = False
        while True:
            if len(fringe) != 0:
                node_expanded = fringe.popleft()
                nodes_expanded += 1
                if node_expanded.name == goal:
                    break
                else:
                    if node_expanded.name not in visited:
                        visited.append(node_expanded.name)
                        for value in routes:
                            if value[0] == node_expanded.name:
                                for hu in heuristics:
                                    if hu[0] == value[1]:
                                        heuristicvalue=hu[1]

                                n = Node(value[1], node_expanded.cum_cost+int(value[2]), node_expanded.d+1, node_expanded.cum_cost+int(value[2])+int(heuristicvalue))
                                n.parents= node_expanded
                                fringe.append(n)
                                s=sorted(fringe, key=lambda node:node.f)
                                fringe=deque(s)
            else:
                goalnotfound = True
                break
        if(goalnotfound == True):
            print ("Nodes Expanded: "+str(nodes_expanded))
            print ("Distance: Infinity")
            print ("Route: None")
        else:
            print ("Nodes Expanded: "+str(nodes_expanded))
            print ("Distance: " + str(node_expanded.cum_cost))
            print ("Route: ")
            path = []
            path.append(goal)
            while node_expanded.parents != None:
                # print ('Route:', node_expanded.parents.name)
                path.append(node_expanded.parents.name)
                node_expanded = node_expanded.parents
            path.reverse()
            i=0
            while i < len(path)-1:
                for v in routes:
                    if path[i]==v[0] and path[i+1] == v[1]:
                        print (v[0] +" to "+ v[1]+ " - "+v[2])
                i += 1


if __name__ == "__main__":

    source = sys.argv[2]
    destination = sys.argv[3]
    if len(sys.argv) >4:
        u=Informed_search()
    else:
        u=Uninformed_search()
    u.find_route(source, destination)
    # print (heuristic)
