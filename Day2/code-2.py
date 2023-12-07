import numpy as np

_cube_min = {
    'red': 0,
    'green': 0,
    'blue': 0,
}

if __name__ == "__main__":
    power_sum = 0
    with open("./input.txt", 'r') as f:
        for line in f:
            cube_min = _cube_min.copy()
            line = line.replace('\n', '')
            game_info, cube_info = line.split(':')
            game_idx = int(game_info.split(' ')[-1])
            cube_count = cube_info.split(';')
            for cc in cube_count:
                cube_N = cc.split(',')
                for cn in cube_N:
                    n, c = cn[1:].split(' ')
                    if int(n) > cube_min[c]:
                        cube_min[c] = int(n)
            power_sum += np.prod(list(cube_min.values()))
    print(power_sum)