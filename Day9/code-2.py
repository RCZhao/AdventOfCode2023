import numpy as np

val_sum = 0
with open("./input.txt", 'r') as f:
    for line in f:
        depth = 1
        num_str_list = line.replace('\n', '').split(' ')
        seq = np.asarray(num_str_list).astype('int')
        all_zero = False
        diffes = [seq,]
        while not all_zero:
            diffes.append(np.diff(seq))
            if diffes[-1].max() == diffes[-1].min() == 0:
                all_zero = True
            else:
                seq = diffes[-1]
        val_pre = 0
        for seq in diffes[::-1]:
            val_pre = seq[0] - val_pre
        val_sum += val_pre
print(val_sum)