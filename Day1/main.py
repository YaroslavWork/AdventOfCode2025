def move_dial(is_left: bool, to: int, start_position: int) -> int:
    if is_left:
        return (start_position - to) % 100
    else:
        return (start_position + to) % 100

def check_how_many_times_dial_pointing_at_zero(
        is_left: bool,
        to: int,
        start_position: int
    ) -> int:

    if is_left:
        # To include zero must do operation -1
        result = abs((start_position - to - 1) // 100)
        if start_position == 0:
            return result - 1 # We now on zero (it is does not count)
        return result
    else:
        return (start_position + to) // 100


if __name__ == '__main__':
    # First parameter tell if dial is moving left than it's true
    # Second parameter tell by how much dial is moving
    combinations: list[list[bool, int]] = []

    with open('input.txt', 'r') as file:
        lines = [line.rstrip('\n') for line in file]
        for line in lines:
            is_left = line[0] == 'L'
            combinations.append([is_left, int(line[1:])])

    dial_position = 50
    pointing_to_zero_counts = 0
    for combination in combinations:
        new_dial_position = move_dial(
            is_left=combination[0],
            to=combination[1],
            start_position=dial_position
        )
        pointing_to_zero_counts += check_how_many_times_dial_pointing_at_zero(
            is_left=combination[0],
            to=combination[1],
            start_position=dial_position
        )
        dial_position = new_dial_position
    
    print(pointing_to_zero_counts)
