if __name__ == '__main__':
    sum = 0
    with open("./input.txt", 'r') as f:
        for line in f:
            line_length = len(line)
            for i in range(line_length):
                char = line[i]
                if char.isnumeric():
                    sum += 10*int(char)
                    break
            for i in range(line_length)[::-1]:
                char = line[i]
                if char.isnumeric():
                    sum += int(char)
                    break
    print(sum)