def process_data(filename):
    with open(filename, 'r') as fp:
        data = fp.read().strip()
        return data


def calculate_number_of_processed_char():
    characters = process_data('input.txt')
    for i in range(len(characters) - 4):
        if len(set(characters[i:i+4])) == 4:
            start_of_packet_marker = i + 4
    for i in range(len(characters) - 14):
        if len(set(characters[i:i+14])) == 14:
            start_of_message_marker = i + 14

    return start_of_packet_marker, start_of_message_marker


if __name__ == '__main__':
    part_one, part_two = calculate_number_of_processed_char()
    print(f'First start-of-packet marker was detected after processing {part_one} characters.')
    print(f'First start-of-message-marker was detected after processing {part_two} characters.')