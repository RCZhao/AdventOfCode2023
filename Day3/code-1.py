def check_symbol(char):
    if (not char.isnumeric()) and (char != '.'):
        adj_2_symb = True
    else:
        adj_2_symb = False
    return adj_2_symb

def search_symbol(
        s_idx, line_N,
        pre_line, cur_line, nex_line
    ):
    num = ""
    adj_2_symb = False
    # check pre idx
    if s_idx > 0:
        adj_2_symb = check_symbol(cur_line[s_idx-1])
        if (not adj_2_symb) and (pre_line is not None):
            adj_2_symb = check_symbol(pre_line[s_idx-1])
        if (not adj_2_symb) and (nex_line is not None):
            adj_2_symb = check_symbol(nex_line[s_idx-1])
    # check current idx
    char = cur_line[s_idx]
    while (char.isnumeric() and s_idx < line_N):
        num += char
        if (not adj_2_symb) and (pre_line is not None):
            adj_2_symb = check_symbol(pre_line[s_idx])
        if (not adj_2_symb) and (nex_line is not None):
            adj_2_symb = check_symbol(nex_line[s_idx])
        s_idx += 1
        if s_idx < line_N:
            char = cur_line[s_idx]
    # check next idx
    if (not adj_2_symb) and (s_idx < line_N):
        adj_2_symb = check_symbol(cur_line[s_idx])
        if (not adj_2_symb) and (pre_line is not None):
            adj_2_symb = check_symbol(pre_line[s_idx])
        if (not adj_2_symb) and (nex_line is not None):
            adj_2_symb = check_symbol(nex_line[s_idx])
    if not adj_2_symb:
        num = None
    else:
        num = int(num)
    return s_idx, num

def search_adj_num(pre_line, cur_line, nex_line):
    adj_num_sum = 0
    line_N = len(cur_line)
    s_idx = 0
    while (s_idx < line_N):
        char = cur_line[s_idx]
        if char.isnumeric():
            s_idx, num = search_symbol(
                s_idx, line_N,
                pre_line, cur_line, nex_line
            )
            if num is not None:
                adj_num_sum += num
        else:
            s_idx += 1
    return adj_num_sum

if __name__ == "__main__":
    tot_sum = 0
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
                tot_sum += search_adj_num(pre_line, cur_line, nex_line)
            pre_line = cur_line
        tot_sum += search_adj_num(cur_line, nex_line, None)

    print(tot_sum)