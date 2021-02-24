### DEFINE STATES OF THE NODES
ALREADY_VISITED = 1
NOT_VISITED = 0
CURRENTLY_VISITING = -1


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


def visit(node : GraphNode, state):

    print(state)

    state[node.value] = CURRENTLY_VISITING

    answer = False

    for neighbour_node in node.neighbours:

        if state[neighbour_node.value] == CURRENTLY_VISITING:

            print(f'Found back edge from {node.value} -> {neighbour_node.value}')

            answer = True

            break

        elif state[neighbour_node.value] == NOT_VISITED:
            
            answer = answer or visit(neighbour_node, state)

    
    state[node.value] = ALREADY_VISITED

    return answer








def has_cycle(adjList):

    state = {}

    for node in adjList:
        
        state[node.value] = NOT_VISITED

    does_contain_cycle = False
    
    for node in adjList:

        if state[node.value] == NOT_VISITED:

            does_contain_cycle = does_contain_cycle or visit(node, state)

            
        

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