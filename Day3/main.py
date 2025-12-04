def find_the_highest_combination(sequence: str) -> int:
    largest_first_digit = 0
    index_of_first_digit_in_sequence = 0
    largest_second_digit = 0
    sequence_length = len(sequence)

    # Find first biggest digit in sequnece (except last number)
    for i in range(sequence_length-1):
        current_digit = int(sequence[i])
        if current_digit > largest_first_digit:
            largest_first_digit = current_digit
            index_of_first_digit_in_sequence = i

    # Find second biggest digit in sequence (continue from first digit)
    for i in range(index_of_first_digit_in_sequence+1, sequence_length):
        current_digit = int(sequence[i])
        if current_digit > largest_second_digit:
            largest_second_digit = current_digit
    
    return largest_first_digit * 10 + largest_second_digit

if __name__ == '__main__':
    sequences: list[list[str]] = []

    with open('input.txt', 'r') as file:
        lines = [line.rstrip('\n') for line in file]
        for line in lines:
            sequences.append(line)

    total_output = 0
    for sequence in sequences:
        total_output += find_the_highest_combination(sequence)

    print(total_output)