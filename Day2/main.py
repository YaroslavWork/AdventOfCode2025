def find_pattern_between_ranges(begin: int, end: int) -> list[int]:
    # Find first half of begin and end numbers
    if begin < 10:
        half_of_begin_number = 0
    else:
        half_of_begin_number = int(str(begin)[:int(len(str(begin)) // 2)])
    half_of_end_number = int(str(end)[:len(str(begin)) // 2 + 1])
    
    pattern_numbers = []
    for i in range(half_of_begin_number, half_of_end_number+1):
        #Check if repeated number is between range
        number = int(str(i)+str(i))
        if begin <= number <= end:
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
        invalid_id.extend(find_pattern_between_ranges(single_range[0], single_range[1]))

    print(sum(invalid_id))