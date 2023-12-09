# %%
from operator import itemgetter
from bisect import bisect_left
# %%
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

def check_loop(node, journey, instruction_idx, step):
    loop_start_idx = -1
    uniq_node = node + f'{instruction_idx:03d}'
    journey_node = list(map(itemgetter(0), journey))
    if len(journey) > 0:
        idx = bisect_left(journey_node, uniq_node)
        if idx < len(journey):
            if journey_node[idx] == uniq_node:
                loop_start_idx = journey[idx][1]
            else:
                journey.insert(idx, [uniq_node, step])
        else:
            journey.append([uniq_node, step])
    else:
        journey.append([uniq_node, step])
    return loop_start_idx

# %%
def ext_euclid(a, b):
    """
    Extended Euclidean algorithm, copied and modified from the sample 
    code in Wikipedia page: 
    https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm.

    Math:
    -----
        as+bt=\gcd(a,b)

    Parameters:
    -----------
    a, b (int):
        two integers numbers which theirs Greatest common divisor will be
        calculated along with the Bézout coefficients s and t that 
        fullfilled the Bézout's identity, which discribed by the equation
        above.

    Return:
    -------
    s, t, \gcd(a,b) (int):
        the Bézout coefficients s and t, and the Greatest common divisor
    """
    old_s, s = 1, 0
    old_t, t = 0, 1
    old_r, r = a, b
    if b == 0:
        return 1, 0, a
    else:
        while(r!=0):
            q = old_r // r
            old_r, r = r, old_r-q*r
            old_s, s = s, old_s-q*s
            old_t, t = t, old_t-q*t
    return old_s, old_t, old_r
# %%
if __name__ == '__main__':
    instructions = []
    network = []
    current_nodes = []
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
            if node[2] == 'A':
                current_nodes.append(node)

    network = sorted(network, key=itemgetter(0))
    loop_info = []
    for current_node in current_nodes:
        steps = 0
        journey = []
        z_idxes = []
        # it seems for each node chain there is only 
        # one node ends with Z
        loop_start_idx = -1
        while loop_start_idx < 0:
            for idx, direction in enumerate(instructions):
                if current_node[2] == 'Z':
                    z_idxes.append(steps)
                loop_start_idx = check_loop(
                    current_node, journey,
                    idx, steps
                )
                if loop_start_idx >=0:
                    break
                current_node = find_path(
                    current_node, direction,
                    network
                )
                steps += 1
        loop_info.append([
            loop_start_idx,
            len(journey),
            z_idxes[0],
            len(journey) - loop_start_idx, #period
        ])
    # in principle, we need to solve a Chinese remainder theorem problem
    # here, but for this specfic data, which is seted up very cleverly,
    # the answer is simpley the least common multiple of the periods of 
    # those loops.
    lcm = loop_info[0][-1]
    for i in range(1, len(loop_info)):
        gcd = ext_euclid(loop_info[i][-1], lcm)[2]
        if loop_info[i][2]*lcm % gcd:
            raise ValueError()
        lcm = loop_info[i][2]*lcm // gcd
    print(lcm)
