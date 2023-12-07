cube_max = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

if __name__ == "__main__":
    game_sum = 0
    with open("./input.txt", 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            possible = True
            game_info, cube_info = line.split(':')
            game_idx = int(game_info.split(' ')[-1])
            cube_count = cube_info.split(';')
            for cc in cube_count:
                cube_N = cc.split(',')
                for cn in cube_N:
                    n, c = cn[1:].split(' ')
                    if int(n) > cube_max[c]:
                        possible = False
                        break
                if not possible:
                    break
            if possible:
                game_sum += game_idx
    print(game_sum)