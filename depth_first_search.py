#This is to help me understand the depth first search algorithm.
# This is a non-recursive version of the depth first search algorithm.
# This is a simple graph with no weights or directions.
graph = {
  'A' : ['B','G'],
  'B' : ['C', 'D', 'E'],
  'C' : [],
  'D' : [],
  'E' : ['F'],
  'F' : [],
  'G' : ['H'],
  'H' : ['I'],
  'I' : [],
}

def DFS(node,visted,graph):
    #If the node is not in the visited set, then add it to the visited set.
    #Then print the node.
    #Then for each neighbour of the node, call the DFS function recursively.
    if node not in visted:
        print(node)
        #Add the node to the visited set.
        #This is to prevent the function from going into an infinite loop.
        visted.add(node)
        for neighbour in graph[node]:
            DFS(neighbour,visted,graph)
visted = set()
DFS('B',visted,graph)


