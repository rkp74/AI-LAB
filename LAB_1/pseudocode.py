# we have the graph in which we want to search, start / root and goal node.
function
graph_search(graph, start, goal):
# initialize an empty list to store the path
path = []
# initialize a queue to store the nodes that will be explored
queue = []
# add the start node to the queue
queue.append(start)
# initialize a set to store the visited nodes
visited = set()

# loop until the queue is empty
while queue:
    # remove the first node in the queue and mark it as visited
    current_node = queue.pop(0)
    visited.add(current_node)
    # if the current node is the goal, return the path
    if current_node == goal:
        return path
    # get the neighbors of the current node
    neighbors = graph[current_node]
    # loop through the neighbors
    for neighbor in neighbors:
        # if the neighbor has not been visited, add it to the queue and update the path
        if neighbor not in visited:
            queue.append(neighbor)
            path.append((current_node, neighbor))
# if the queue is empty and the goal has not been reached, return "Goal not found"
return "Goal not found”
