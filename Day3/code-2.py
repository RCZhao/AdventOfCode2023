def search_num_back_forward(line, s_idx):
    line_N = len(line)
    s_idx_b = s_idx-1
    while s_idx_b >= 0:
        if line[s_idx_b].isnumeric():
            s_idx_b -= 1
        else:
            break
    s_idx_f = s_idx+1
    while s_idx_f < line_N:
        if line[s_idx_f].isnumeric():
            s_idx_f += 1
        else:
            break
    num = int(line[s_idx_b+1:s_idx_f])
    return num, s_idx_f

def search_nums(
        s_idx, line_N,
        pre_line, cur_line, nex_line
    ):
    adj_num_N = 0
    num_prod = 1
    if s_idx>0:
        if cur_line[s_idx-1].isnumeric():
            adj_num_N += 1
            num, _ = search_num_back_forward(
                cur_line, s_idx-1
            )
            num_prod *= num
    if s_idx<line_N-1:
        if cur_line[s_idx+1].isnumeric():
            adj_num_N += 1
            num, _ = search_num_back_forward(
                cur_line, s_idx+1
            )
            num_prod *= num
    if pre_line is not None:
        search_idx = max(s_idx-1, 0)
        while (search_idx <= min(s_idx+1, line_N-1)):
            if pre_line[search_idx].isnumeric():
                adj_num_N += 1
                if adj_num_N > 2:
                    return None
                num, s_idx_f = search_num_back_forward(
                    pre_line, search_idx
                )
                num_prod *= num
                search_idx = s_idx_f + 1
            else:
                search_idx += 1
    if nex_line is not None:
        search_idx = max(s_idx-1, 0)
        while (search_idx <= min(s_idx+1, line_N-1)):
            if nex_line[search_idx].isnumeric():
                adj_num_N += 1
                if adj_num_N > 2:
                    return None
                num, s_idx_f = search_num_back_forward(
                    nex_line, search_idx
                )
                num_prod *= num
                search_idx = s_idx_f + 1
            else:
                search_idx += 1
    if adj_num_N == 2:
        return num_prod
    else:
        return None

def search_gear(pre_line, cur_line, nex_line):
    gear_ratio = 0
    line_N = len(cur_line)
    s_idx = 0
    while (s_idx < line_N):
        char = cur_line[s_idx]
        if char == '*':
            num = search_nums(
                s_idx, line_N,
                pre_line, cur_line, nex_line
            )
            if num is not None:
                gear_ratio += num
        s_idx += 1
    return gear_ratio

if __name__ == "__main__":
    tot_ratio = 0
    pre_line = None
    cur_line = None
    with open("./input.txt", 'r') as f:
        for l_idx, line in enumerate(f):
            line = line.replace('\n', '')
            s_idx = 0
            if l_idx >= 1:
                cur_line = nex_line
            nex_line = line
            if l_idx >= 1:
                tot_ratio += search_gear(pre_line, cur_line, nex_line)
            pre_line = cur_line
        tot_ratio += search_gear(cur_line, nex_line, None)

    print(tot_ratio)