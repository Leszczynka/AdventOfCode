from collections import defaultdict


def process_data(filename):
    with open(filename, 'r') as fp:
        data = fp.read().strip().split('\n')
        return data


def create_file_system():
    commands = process_data('input.txt')
    dir_sizes = defaultdict(int)
    stack = []
    for command in commands:
        match command.split():
            case[_, _, '/']:
                stack = []
            case[_, _, '..']:
                stack.pop()
            case[_, _, x]:
                stack.append(x)
            case[n, _] if n.isdigit():
                for i in range(len(stack) + 1):
                    path = '/' + '/'.join(stack[:i])
                    dir_sizes[path] += int(n)
    return dir_sizes


def calculate_total_sum_of_dirs():
    dir_sizes = create_file_system()
    return sum(val for val in dir_sizes.values() if val <= 100000)


if __name__ == '__main__':
    part1 = calculate_total_sum_of_dirs()
    print(f'Total size of directories (with a total size of at most 100000) is {part1}.')

