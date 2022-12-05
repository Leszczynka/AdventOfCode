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
    stacks, instructions = process_data('input.txt')
    for instruction in instructions:
        quantity = instruction[0]
        _from = instruction[1]
        _to = instruction[2]
        for n in range(quantity):
            stacks[_to - 1].append(stacks[_from-1].pop())

    return ''.join(stacks[i][-1] for i in range(len(stacks)))


if __name__ == '__main__':
    print(f'Part One: Crates on top of stacks: {rearrange_stacks()}.')
