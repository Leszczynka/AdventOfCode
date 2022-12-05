from copy import deepcopy


def process_data(filename):
    with open(filename, 'r') as fp:
        data = fp.read().split('\n\n')
        stacks_rows = data[0].split('\n')[::-1]
        stacks = [
            [row[i] for row in stacks_rows if row[i] != ' ']
            for i in range(1, len(stacks_rows[0]), 4)
        ]
        instructions_rows = data[1].split('\n')
        instructions = [instruction.split() for instruction in instructions_rows]
        moves = [[int(move[1]), int(move[3]), int(move[5])] for move in instructions]

        return stacks, moves


def rearrange_stacks():
    stacks_part1, instructions = process_data('input.txt')
    stacks_part2 = deepcopy(stacks_part1)

    for instruction in instructions:
        quantity = instruction[0]
        _from = instruction[1]
        _to = instruction[2]

        for n in range(quantity):
            stacks_part1[_to - 1].append(stacks_part1[_from - 1].pop())

        stacks_part2[_to - 1].extend((stacks_part2[_from - 1])[-quantity::])
        del stacks_part2[_from - 1][-quantity::]

    crates_on_top_part1 = ''.join(stacks_part1[i][-1] for i in range(len(stacks_part1)))
    crates_on_top_part2 = ''.join(stacks_part2[i][-1] for i in range(len(stacks_part2)))

    return crates_on_top_part1, crates_on_top_part2


if __name__ == '__main__':
    part1, part2 = rearrange_stacks()
    print(f'Part One: Crates on top of stacks: {part1}.')
    print(f'Part Two: Crates on top of stacks: {part2}.')

