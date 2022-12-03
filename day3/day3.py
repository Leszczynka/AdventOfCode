import string


def process_data(filename):
    with open(filename, 'r') as fp:
        rucksacks_data = fp.read()
        rucksacks_items = rucksacks_data.split('\n')
        return rucksacks_items


def calculate_sum_of_priorities():
    rucksacks_items = process_data('input.txt')

    lower_priority = {k: v for (v, k) in enumerate(string.ascii_lowercase, start=1)}
    upper_priority = {k: v for (v, k) in enumerate(string.ascii_uppercase, start=27)}
    priority_sum = 0

    for items in rucksacks_items:
        n = len(items)
        half = n//2
        first_half = set(items[0:half])
        second_half = set(items[half:])
        shared_item = ''.join(first_half & second_half)

        if shared_item.islower():
            priority_sum += lower_priority[shared_item]
        else:
            priority_sum += upper_priority[shared_item]

    return priority_sum


if __name__ == '__main__':
    print(f'Part one: Sum of the priorities of items shared in each rucksack is: {calculate_sum_of_priorities()}.')
