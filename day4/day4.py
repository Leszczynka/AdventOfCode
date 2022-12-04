def process_data(filename):
    with open(filename, 'r') as fp:
        sections_data = fp.read().rstrip().split('\n')
        pairs_data = [tuple(pair.split(',')) for pair in sections_data]
        elf1 = [tuple(pair[0].split('-')) for pair in pairs_data]
        elf2 = [tuple(pair[1].split('-')) for pair in pairs_data]
        return elf1, elf2


def calculate_pairs_with_overlapping_ranges():
    elf1, elf2 = process_data('input.txt')
    total_full_overlapping_ranges = 0
    total_overlapping_ranges = 0

    for i in range(len(elf1)):
        start1 = int(elf1[i][0])
        end1 = int(elf1[i][1])
        start2 = int(elf2[i][0])
        end2 = int(elf2[i][1])

        if start1 <= start2 <= end2 <= end1 or start2 <= start1 <= end1 <= end2:
            total_full_overlapping_ranges += 1
            total_overlapping_ranges += 1
        elif start1 <= start2 and end1 >= start2:
            total_overlapping_ranges += 1
        elif start1 >= start2 and start1 <= end2:
            total_overlapping_ranges += 1

    return total_full_overlapping_ranges, total_overlapping_ranges


if __name__ == '__main__':
    part_one_answer, part_two_answer = calculate_pairs_with_overlapping_ranges()
    print(f'Part one: Total full overlapping ranges is {part_one_answer}.')
    print(f'Part one: Total overlapping ranges is {part_two_answer}.')



