from operator import itemgetter
from bisect import bisect_right

def map_2_next(val, plane_map):
    source_list = list(
        map(itemgetter(1), plane_map)
    )
    idx = bisect_right(source_list, val) - 1
    if (idx >= 0):
        map_seg = plane_map[idx]
        dest_low = map_seg[0]
        source_low = map_seg[1]
        map_range = map_seg[2]
        if (val < source_low + map_range):
            return val + dest_low - source_low
    return val

map_list = []
with open("./input.txt", 'r') as f:
# with open("./example.txt", 'r') as f:
    seed_info = f.readline().split(':')[1][1:]
    seed_list = list(map(int, seed_info.split(' ')))
    line = f.readline()
    while line != '':
        plane_map = []
        line = f.readline()
        line = f.readline()
        while line != '\n' and line != '':
            map_seg = list(map(int, line.split(' ')))
            plane_map.append(map_seg)
            line = f.readline()
        plane_map = sorted(plane_map, key=itemgetter(1))
        map_list.append(plane_map)
lowest_loc = -1
for seed in seed_list:
    val = seed
    # print(val, end=' ')
    for _map in map_list:
        val = map_2_next(val, _map)
        # print(val, end=' ')
    # print()

    if val < lowest_loc or lowest_loc < 0:
        lowest_loc = val
print(lowest_loc)
