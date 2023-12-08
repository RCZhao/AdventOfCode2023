from math import (sqrt, floor, ceil)

def line_2_num(line):
    line = line.replace('\n', '')
    num_str = line.split(':')[1]
    num_str_list = num_str.split(' ')
    num_list = []
    for wn in num_str_list:
        wn = wn.replace(' ', '')
        if len(wn) > 0:
            num_list.append(int(wn))
    return num_list

def count_num_of_ways(time, d_record):
    t_1 = (-time + sqrt(time**2 - 4*d_record)) / -2.
    t_2 = (-time - sqrt(time**2 - 4*d_record)) / -2.
    t_max = floor(max(t_1, t_2))
    t_min = ceil(min(t_1, t_2))
    if t_max*(time-t_max) == d_record:
        t_max -= 1
    if t_min*(time-t_min) == d_record:
        t_min += 1
    ways_N = t_max - t_min + 1
    return t_min, t_max, ways_N

if __name__ == "__main__":
    with open("./input.txt", 'r') as f:
        time_list = line_2_num(f.readline())
        dist_list = line_2_num(f.readline())
    points = 1
    for idx, time in enumerate(time_list):
        t_min, t_max, ways = \
            count_num_of_ways(time, dist_list[idx])
        points *= ways
    print(points)