from tqdm import tqdm
from operator import itemgetter
from bisect import bisect_right

def map_2_next(val_range, plane_map):
    plane_map_N = len(plane_map)
    source_list = list(
        map(itemgetter(1), plane_map)
    )
    val_low = val_range[0]
    val_length = val_range[1]
    val_up = val_low+val_length
    idx_low = bisect_right(
        source_list, val_low
    ) - 1
    idx_up = bisect_right(
        source_list, val_up
    ) - 1
    dest_range_list = []
    if idx_low == idx_up:
        if idx_low < 0:
            dest_range_list.append(val_range)
        else:
            map_seg = plane_map[idx_low]
            dest_low = map_seg[0]
            source_low = map_seg[1]
            map_range = map_seg[2]
            source_up = source_low + map_range
            if val_up <= source_up:
                dest_range_list.append(
                    [val_low+dest_low-source_low,
                     val_length]
                )
            elif val_low >= source_up:
                dest_range_list.append(val_range)
            else:
                dest_range_list.append(
                    [val_low+dest_low-source_low,
                     source_up-val_low]
                )
                dest_range_list.append(
                    [source_up,
                     val_up-source_up
                    ]
                )
        return dest_range_list
    if idx_low >= plane_map_N-1:
        map_seg = plane_map[plane_map_N-1]
        dest_low = map_seg[0]
        source_low = map_seg[1]
        map_range = map_seg[2]
        source_up = source_low + map_range
        if val_up <= source_up:
            dest_range_list.append(
                [val_low+dest_low-source_low,
                 val_length
                ]
            )
        else:
            dest_range_list.append(
                [val_low+dest_low-source_low,
                 source_up-val_low
                ]
            )
            dest_range_list.append(
                [source_up,
                 val_up-source_up
                ]
            )
        return dest_range_list

    if idx_low < 0:
        map_seg = plane_map[0]
        dest_low = map_seg[0]
        source_low = map_seg[1]
        map_range = map_seg[2]
        dest_range_list.append(
            [val_low, source_low-val_low]
        )
    elif idx_low < plane_map_N-1:
        map_seg = plane_map[idx_low]
        dest_low = map_seg[0]
        source_low = map_seg[1]
        map_range = map_seg[2]
        source_up = source_low + map_range
        if val_low < source_up:
            dest_range_list.append(
                [val_low+dest_low-source_low,
                 source_up-val_low
                ]
            )
            map_seg = plane_map[idx_low+1]
            source_next = map_seg[1]
            if source_next > source_up:
                dest_range_list.append(
                    [source_up,
                    source_next-source_up
                    ]
                )
    for idx in range(idx_low+1, idx_up):
        map_seg = plane_map[idx]
        dest_low = map_seg[0]
        source_low = map_seg[1]
        map_range = map_seg[2]
        source_up = source_low + map_range
        dest_range_list.append(
            [dest_low, map_range]
        )
        map_seg = plane_map[idx+1]
        source_next = map_seg[1]
        if source_next > source_up:
            dest_range_list.append(
                [source_up,
                source_next-source_up
                ]
            )
    map_seg = plane_map[idx_up]
    dest_low = map_seg[0]
    source_low = map_seg[1]
    map_range = map_seg[2]
    source_up = source_low + map_range
    if val_up <= source_up:
        dest_range_list.append(
            [dest_low,
             val_up - source_low
            ]
        )
    else:
        dest_range_list.append(
            [dest_low, map_range]
        )
        dest_range_list.append(
            [source_up,
             val_up-source_up
            ]
        )
    dest_range_list = sorted(
        dest_range_list,
        key=itemgetter(0)
    )
    return dest_range_list

if __name__ == "__main__":
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
    seed_seg_N = len(seed_list) // 2
    seed_range_list = []
    for i in tqdm(range(seed_seg_N)):
        seed_range_list.append([
            seed_list[i*2],
            seed_list[i*2+1]
        ])

    val_range_list = seed_range_list
    for _map in tqdm(map_list):
        dest_range_list = []
        for val_range in tqdm(
                val_range_list,
                leave=False
            ):
            dest_range_list += map_2_next(val_range, _map)
            dest_range_list = sorted(
                dest_range_list,
                key=itemgetter(0)
            )
        val_range_list = dest_range_list

    print(len(dest_range_list))
    print(dest_range_list[0][0])