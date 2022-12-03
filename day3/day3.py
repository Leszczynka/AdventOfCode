import string


def process_data(filename):
    with open(filename, 'r') as fp:
        rucksacks_data = fp.read()
        rucksacks_items = rucksacks_data.split('\n')
        return rucksacks_items


def find_items_types():
    rucksacks_items = process_data('input.txt')
    shared_items = []

    for items in rucksacks_items:
        n = len(items)
        half = n//2
        first_half = set(items[0:half])
        second_half = set(items[half:])
        shared_item = ''.join(first_half & second_half)
        shared_items.append(shared_item)

    return shared_items


def find_items_types_corresponded_to_the_groups():
    rucksacks_items = process_data('input.txt')
    groups = [rucksacks_items[x:x+3] for x in range(0, len(rucksacks_items), 3)]
    badge_items = []

    for group in groups:
        elf1 = set(group[0])
        elf2 = set(group[1])
        elf3 = set(group[2])
        group_badge = ''.join(elf1 & elf2 & elf3)
        badge_items.append(group_badge)

    return badge_items


def calculate_sum_of_items_priorities(items):
    lower_priority = {k: v for (v, k) in enumerate(string.ascii_lowercase, start=1)}
    upper_priority = {k: v for (v, k) in enumerate(string.ascii_uppercase, start=27)}
    priority_sum = 0

    for item in items:
        if item.islower():
            priority_sum += lower_priority[item]
        else:
            priority_sum += upper_priority[item]

    return priority_sum


if __name__ == '__main__':
    part1_items = find_items_types()
    part1_sum = calculate_sum_of_items_priorities(part1_items)
    print(f'Part one: Sum of the priorities of item types is: {part1_sum}.')

    part2_items = find_items_types_corresponded_to_the_groups()
    part2_sum = calculate_sum_of_items_priorities(part2_items)
    print(f'Part two: Sum of the priorities of groups item types is: {part2_sum}.')