def is_this_number_inside_of_ranges(
        ranges: list[list[int, int]],
        number: int
    ) -> bool:

    for current_range in ranges:
        if current_range[0] <= number <= current_range[1]:
            return True

    return False

if __name__ == '__main__':
    ranges: list[list[int, int]] = [] # Ranges 1. from; 2. to (includes)
    ids: list[int] = []

    with open('input.txt', 'r') as file:
        switched_to_ids = False
        lines = [line.rstrip('\n') for line in file]
        for line in lines:
            if line == '':
                switched_to_ids = True
                continue

            if switched_to_ids:
                ids.append(int(line))
            else:
                current_range = line.split('-')
                ranges.append([int(current_range[0]), int(current_range[1])])

    sum_id = 0
    for current_id in ids:
        sum_id += is_this_number_inside_of_ranges(ranges, current_id)

    print(sum_id)