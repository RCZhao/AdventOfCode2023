dict_tree = {
    'o': {
        'n': {
            'e': 1,
        },
    },

    't': {
        'w': {
            'o': 2,
        },
        'h': {
            'r': {
                'e': {
                    'e': 3,
                },
            },
        },
    },

    'f': {
        'o': {
            'u': {
                'r': 4,
            },
        },
        'i': {
            'v': {
                'e': 5,
            },
        },
    },

    's': {
        'i': {
            'x': 6,
        },
        'e': {
            'v': {
                'e': {
                    'n': 7,
                },
            },
        },
    },

    'e': {
        'i': {
            'g': {
                'h': {
                    't': 8,
                },
            },
        },
    },

    'n': {
        'i': {
            'n': {
                'e': 9,
            },
        },
    },
}

def search_tree(line, idx, length):
    sub_tree = dict_tree[line[idx]]
    _idx = idx + 1
    while (_idx < length):
        if line[_idx] in sub_tree:
            sub_tree = sub_tree[line[_idx]]
            _idx += 1
            if type(sub_tree) == int:
                return sub_tree
        else:
            return -1
    return -1

if __name__ == '__main__':
    sum = 0
    with open("./input.txt", 'r') as f:
        for line in f:
            first_digt = 0
            last_digt = None
            line_length = len(line)
            i=0
            while (i < line_length):
                char = line[i]
                if char.isnumeric():
                    if last_digt is None:
                        first_digt = int(char)
                        sum += 10*first_digt
                    last_digt = int(char)
                elif char in dict_tree:
                    w2d = search_tree(line, i, line_length)
                    if w2d > 0:
                        if last_digt is None:
                            first_digt = w2d
                            sum += 10*first_digt
                        last_digt = w2d
                i += 1
            sum += last_digt
    print(sum)