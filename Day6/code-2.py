from math import (sqrt, floor, ceil)
def line_2_num(line):
    line = line.replace('\n', '')
    num_str = line.split(':')[1].replace(' ', '')
    return int(num_str)

# def count_num_of_ways(time, d_record):
#     t_max = time//2
#     ways_N = 0
#     t = t_max
#     while ((time-t)*t > d_record):
#         ways_N += 1
#         t -= 1
#     t = t_max+1
#     while ((time-t)*t > d_record):
#         ways_N += 1
#         t += 1
#     return ways_N

# def count_num_of_ways(time, d_record):
#     t_1 = (-time + sqrt(time**2 - 4*d_record)) / -2
#     t_2 = (-time - sqrt(time**2 - 4*d_record)) / -2
#     t_max = floor(max(t_1, t_2))
#     t_min = ceil(min(t_1, t_2))
#     return t_max - t_min + 1

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
        time = line_2_num(f.readline())
        dist = line_2_num(f.readline())
    t_min, t_max, ways = count_num_of_ways(time, dist)
    print(ways)