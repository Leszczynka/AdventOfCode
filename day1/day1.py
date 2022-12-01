def process_data(filename):
    with open(filename, 'r') as fp:
        calories_raw_data = fp.read()
        calories_list = calories_raw_data.rstrip().split('\n\n')
        calories_lists_clean = [element.split('\n') for element in calories_list]
        return calories_lists_clean


def calculate_sum_of_calories_by_elf(calories: list) -> list:
    total_calories_by_elf = []
    for elf_calories in calories:
        calories_sum = sum(int(calories) for calories in elf_calories)
        total_calories_by_elf.append(calories_sum)
    return total_calories_by_elf


def find_max_calories(calories: list, n: int):
    calories.sort(reverse=True)
    if n == 1:
        return calories[0]
    return calories[0:n]


if __name__ == '__main__':
    calories_data = process_data('input.txt')
    total_elfs_calories = calculate_sum_of_calories_by_elf(calories_data)

    max_calories = find_max_calories(total_elfs_calories, 1)
    print(f'Part one: Elf carrying the most Calories carried {max_calories} calories.')

    top_three_most_calories = find_max_calories(total_elfs_calories, 3)
    sum_of_top_three = sum(top_three_most_calories)
    print(f'Part two: Total sum of calories carried by the top three Elves is {sum_of_top_three} calories.')