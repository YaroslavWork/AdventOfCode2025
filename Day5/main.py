def is_this_number_inside_of_ranges(
        ranges: list[list[int, int]],
        number: int
    ) -> bool:

    for current_range in ranges:
        if current_range[0] <= number <= current_range[1]:
            return True

    return False


def find_all_number_inside_of_ranges(ranges: list[list[int, int]]) -> int:
    sorted_and_expanded_ranges = []

    for i in range(len(ranges)):
        start_id = 0

        is_added = False
        for j in range(len(sorted_and_expanded_ranges)):
            if sorted_and_expanded_ranges[j][0] <= ranges[i][0] <= \
                sorted_and_expanded_ranges[j][1]:
                start_id = j
                is_added = True
            
        for j in range(start_id, len(sorted_and_expanded_ranges)):
            if sorted_and_expanded_ranges[j][0] <= ranges[i][1] <= \
                sorted_and_expanded_ranges[j][1]:
                finish

            
        if not is_added:
            sorted_and_expanded_ranges.append(ranges[i])
            
        


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

    print(f"First half - {sum_id}")