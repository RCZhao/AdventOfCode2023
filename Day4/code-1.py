def line_2_num(line):
    line = line.replace('\n', '')
    win_num, my_num = line.split(':')[1].split('|')
    win_num_str_list = win_num.split(' ')
    my_num_str_list = my_num.split(' ')
    win_num_list = []
    for wn in win_num_str_list:
        wn = wn.replace(' ', '')
        if len(wn) > 0:
            win_num_list.append(int(wn))
    my_num_list = []
    for mn in my_num_str_list:
        mn = mn.replace(' ', '')
        if len(mn) > 0:
            my_num_list.append(int(mn))
    return sorted(win_num_list), sorted(my_num_list)

def count_points(win_nums, my_nums):
    win_N = len(win_nums)
    my_N = len(my_nums)
    match_N = 0
    i = 0
    j = 0
    while (i<win_N):
        win = win_nums[i]
        while (j<my_N) and (my_nums[j]<=win):
            if my_nums[j] == win:
                match_N += 1
            j += 1
        i += 1
    return match_N

if __name__ == "__main__":
    tot_points = 0
    with open("./input.txt", 'r') as f:
        for l_idx, line in enumerate(f):
            win_nums, my_nums = line_2_num(line)
            match_N = count_points(win_nums, my_nums)
            if match_N > 0:
                tot_points += 2**(match_N-1)
    print(tot_points)