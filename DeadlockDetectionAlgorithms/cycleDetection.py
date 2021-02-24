class GraphNode:
    def __init__(self, value : int):
        self.value = value
        self.neighbours = []


    def __str__(self):
        return f'<{self.value}>'

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def add_neighbours(self, neighbours):
        for neighbour in neighbours:
            self.add_neighbour(neighbour)


def visit(node : GraphNode, is_visited):

    print(is_visited)

    is_visited[node.value] = -1

    answer = False

    for neighbour_node in node.neighbours:

        if is_visited[neighbour_node.value] == -1:

            print(f'Found back edge from {node.value} -> {neighbour_node.value}')

            answer = True

            break

        elif is_visited[neighbour_node.value] == 0:
            
            answer = answer or visit(neighbour_node, is_visited)

    
    is_visited[node.value] = 1

    return answer








def has_cycle(adjList):

    is_visited = {}

    for node in adjList:
        is_visited[node.value] = 0

    does_contain_cycle = False
    
    for node in adjList:

        if not is_visited[node.value]:

            does_contain_cycle = does_contain_cycle or visit(node, is_visited)

            
        

    return does_contain_cycle


def main():
    node_one = GraphNode(1)
    node_two = GraphNode(2)
    node_three = GraphNode(3)
    node_four = GraphNode(4)
    node_five = GraphNode(5)

    # Construct the graph
    node_one.add_neighbours([node_four, node_two])
    node_four.add_neighbours([node_two])
    node_two.add_neighbours([node_five, node_three])
    node_three.add_neighbour(node_one)


    adjList = [node_one, node_two, node_three, node_four, node_five]

    ## check if the adjList contains a cycle or not
    is_cycle_present_in_graph = has_cycle(adjList)

    print(is_cycle_present_in_graph)



if __name__ == "__main__":
    main()