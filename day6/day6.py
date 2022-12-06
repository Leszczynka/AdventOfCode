def process_data(filename):
    with open(filename, 'r') as fp:
        data = fp.read().strip()
        return data


def calculate_number_of_processed_char():
    characters = process_data('input.txt')
    for i in range(len(characters) - 4):
        if len(set(characters[i:i+4])) == 4:
            return i + 4


if __name__ == '__main__':
    part_one = calculate_number_of_processed_char()
    print(f'First marker was detected after processing {part_one} characters.')