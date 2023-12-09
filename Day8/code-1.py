from operator import itemgetter
from bisect import bisect_left

def find_path(node, direction, network):
    path_idx = bisect_left(
        list(
            map(itemgetter(0), network)
        ),
        node
    )
    if network[path_idx][0] != node:
        raise ValueError(
                f"node {node} is not in the map, you are lost!"
            )
    next_node = network[path_idx][1][direction]
    return next_node

if __name__ == '__main__':
    instructions = []
    network = []
    with open("./input.txt", 'r') as f:
        instructions_str = f.readline().replace('\n', '')
        for c in instructions_str:
            if c=='L':
                instructions.append(0)
            elif c=='R':
                instructions.append(1)
            else:
                raise ValueError()
        f.readline()
        for line in f:
            node, path = line.replace('\n', '').split('=')
            node = node.replace(' ', '')
            path = path.replace(' ', '')
            path = path[1:-1].split(',')
            network.append([node, path])

    network = sorted(network, key=itemgetter(0))

    current_node = 'AAA'
    # journey = []
    # no loop can be formed durning the process, so no need to track the 
    # past nodes
    steps = 0
    while current_node != 'ZZZ':
        for direction in instructions:
            # journey.append([current_node, direction])
            if current_node == "ZZZ":
                break
            current_node = find_path(
                current_node, direction,
                network
            )
            steps += 1
    print(steps)