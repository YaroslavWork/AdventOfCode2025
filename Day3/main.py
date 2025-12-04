from itertools import combinations

def find_the_highest_combination(sequence: str, max_digit=2) -> int:
    list_of_sequence = [int(digit) for digit in sequence]
    output = 0
    current_index = -1
    for current_digit in range(max_digit):
        local_max_digit = 0
        for i in range(current_index+1, len(sequence)-max_digit+current_digit+1):
            if list_of_sequence[i] > local_max_digit:
                local_max_digit = list_of_sequence[i]
                current_index = i

        output += local_max_digit * 10 ** (max_digit-current_digit-1)

    return output

if __name__ == '__main__':
    sequences: list[list[str]] = []

    with open('input.txt', 'r') as file:
        lines = [line.rstrip('\n') for line in file]
        for line in lines:
            sequences.append(line)

    total_output = 0
    for sequence in sequences:
        total_output += find_the_highest_combination(sequence, max_digit=12)

    print(total_output)