def process_data(filename):
    with open(filename, 'r') as fp:
        strategy_data = ((line[0], line[2]) for line in fp.readlines())
        return strategy_data


def count_total_score():
    strategy_data = process_data('input.txt')
    my_score = 0
    choice_points = {'X': 1, 'Y': 2, 'Z': 3}
    results = {
        ('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
        ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
        ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
    }
    for game_round in strategy_data:
        opponent = game_round[0]
        me = game_round[1]
        my_score += choice_points[me] + results[opponent, me]
    return my_score


if __name__ == '__main__':
    print(f'Part one: total score={count_total_score()}.')