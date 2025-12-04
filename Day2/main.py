def find_pattern_between_ranges(begin: int, end: int) -> list[int]:
    raise NotImplementedError('Function not pass unit tests.')
    pattern_numbers = []
    max_length_of_half_number = len(str(end)) // 2 + 1
    min_number_length = len(str(begin))
    max_number_length = len(str(end))

    for current_length in range(1, max_length_of_half_number + 1):
        start_number = int(str(begin)[:current_length])-1
        end_number = int(str(end)[:current_length])+1
        if end_number < start_number:
            end_number = int(str(end)[:current_length + 1])

        for current_range in range(start_number, end_number + 1):
            #Check if repeated number is between range
            for repeats in range(
                min_number_length//current_length-1,
                max_number_length//current_length+1
            ):
                if repeats <= 0:
                    continue
                
                number = int(str(current_range)*repeats)
                
                if repeats == 1:  # Additional check for single repeats
                    if len(set(str(number))) != 1:
                        continue
                
                if begin <= number <= end:
                    pattern_numbers.append(number)

    uniqued_list = list(set(pattern_numbers))
    uniqued_list.sort()
    # Single digit is not repeated digit
    filtered_list = [x for x in uniqued_list if x >= 10]

    return filtered_list

def has_pattern(number: int) -> bool:
    number_str = str(number)
    number_length = len(number_str)
    if number_length == 1:
        return False # One digit has not similarity pattern
    for repeats in range(1, number_length // 2 + 1):
        if number_length % repeats != 0:
            continue # the pattern does not have the same number of repetitions
        repetition = [
            number_str[start_index*repeats:start_index*repeats+repeats]
                for start_index in range(number_length // repeats)
        ]
        if len(set(repetition)) == 1:
            return True
    return False

def find_pattern_between_ranges_brute_force(begin: int, end: int) -> list[int]:
    pattern_numbers = []
    for number in range(begin, end+1):
        if has_pattern(number):
            pattern_numbers.append(number)

    return pattern_numbers

if __name__ == '__main__':
    # First parameter: from (include)
    # Second parameter: to (include)
    ranges: list[list[int, int]] = []

    with open('input.txt', 'r') as file:
        content = file.read().rstrip('\n')

        ranges_str = content.split(',')

        ranges_without_sign = [ranges_str[i].split('-')
            for i in range(len(ranges_str))]

        for single_range in ranges_without_sign:
            ranges.append([int(single_range[0]), int(single_range[1])])

    invalid_id = []
    for single_range in ranges:
        #invalid_id.extend(find_pattern_between_ranges(single_range[0], single_range[1]))
        invalid_id.extend(find_pattern_between_ranges_brute_force(single_range[0], single_range[1]))

    print(sum(invalid_id))