card_2_hax_dict = {
    'A': 'e',
    'K': 'd',
    'Q': 'c',
    'J': 'b',
    'T': 'a'
}
hand_type_dict = {
    '5': 6,
    '41': 5,
    '32': 4,
    '311': 3,
    '221': 2,
    '2111': 1,
    '11111': 0
}
def hand_2_hax_and_classif(hand):
    hax_string = ''
    card_count = [0] * 13
    for c in hand:
        if c.isalpha():
            h = card_2_hax_dict[c]
        else:
            h = c
        card_count[int(h, base=16)-2] += 1
        hax_string += h
    card_count = sorted(card_count)[::-1]
    hand_type = ''
    i = 0
    while card_count[i] > 0:
        hand_type += str(card_count[i])
        i += 1
    hand_type = hand_type_dict[hand_type]
    return hax_string, hand_type

if __name__ == '__main__':
    hand_cata = [
        [] for _ in range(7)
    ]
    with open("./input.txt", 'r') as f:
        for line in f:
            hand, bid = line.replace('\n', '').split(' ')
            hand, hand_type = hand_2_hax_and_classif(hand)
            bid = int(bid)
            hand_cata[hand_type].append([hand, bid])

    tot_win = 0
    rank = 1
    for hands in hand_cata:
        hands = sorted(
            hands, 
            key=lambda k: int(k[0], base=16)
        )
        for hand in hands:
            tot_win += hand[1] * rank
            rank += 1

    print(tot_win)