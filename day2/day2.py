def process_data(filename):
    with open(filename, 'r') as fp:
        strategy_data = ((line[0], line[2]) for line in fp.readlines())
        return strategy_data


def count_total_score():
    strategy_data = process_data('input.txt')
    my_score_part1 = 0
    my_score_part2 = 0
    choice_points = {'X': 1, 'Y': 2, 'Z': 3}
    results = {
        ('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
        ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
        ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
    }
    my_choices = {(k[0], v): k[1] for k, v in results.items()}
    print(my_choices)
    strategy = {'X': 0, 'Y': 3, 'Z': 6}
    for game_round in strategy_data:
        opponent = game_round[0]
        me = game_round[1]
        my_score_part1 += choice_points[me] + results[opponent, me]
        my_score_part2 += choice_points[my_choices[(opponent, strategy[me])]] + strategy[me]
    return my_score_part1, my_score_part2


if __name__ == '__main__':
    part1, part2 = count_total_score()
    print(f'Part one: total score={part1}.')
    print(f'Part two: total score={part2}.')
