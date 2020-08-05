# a8 - dijkstra algorithm
import math

def Dijkstra(graph,source,target):


    unvisited_nodes=graph
    shortest_distance={}
    route=[]
    predecessor={}

    for nodes in unvisited_nodes:
        shortest_distance[nodes]=math.inf

    shortest_distance[source]=0

    while(unvisited_nodes):

        min_Node=None
        for current_node in unvisited_nodes:

            if min_Node is None:
                min_Node=current_node
            elif shortest_distance[min_Node] > shortest_distance[current_node]:
                min_Node=current_node

        for child_node,value in unvisited_nodes[min_Node].items():
            if value + shortest_distance[min_Node] < shortest_distance[child_node]:
                shortest_distance[child_node] = value + shortest_distance[min_Node]
                predecessor[child_node] = min_Node

        unvisited_nodes.pop(min_Node)
    node = target

    while node != source:
        try:
            route.insert(0,node)
            node = predecessor[node]
        except Exception:
            print('Path not reachable')
            break
    route.insert(0,source)

    if shortest_distance[target] != math.inf:
        print('Shortest distance is ' + str(shortest_distance[target]))
        print('And the path is ' + str(route))


graph = {'a':{'b':5,'c':2},'b':{'c':1,'d':3},'c':{'b':3,'d':7},'d':{'e':7},'e':{'d':9}}
Dijkstra(graph,'a','e')
