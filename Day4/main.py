def paper_cleaning_operation(sequence: list[str], is_remembering_where=False) -> (int, list[int, int]) or int:
    output = 0
    paper_is_cleared_position = []
    for y in range(len(sequence)):
        for x in range(len(sequence[y])):
            if sequence[y][x] == '.':
                continue

            count_paper = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if k == 0 and l == 0:
                        continue  # Not counting yourself

                    if y+k < 0 or y+k >= len(sequence)\
                        or x+l < 0 or x+l >= len(sequence[y]):
                        continue  # Edge cases
                    
                    if sequence[y+k][x+l] == '@':
                        count_paper += 1
                        
            
            if count_paper < 4:
                output += 1
                paper_is_cleared_position.append([y, x])
    
    if is_remembering_where:
        return output, paper_is_cleared_position
    return output


def clear_papers(sequence: list[str], positions: list[list[int]]) -> list[str]:
    for position in positions:
        sequence[position[0]] = sequence[position[0]][:position[1]] + '.' + sequence[position[0]][position[1]+1:]

    return sequence


if __name__ == '__main__':
    sequences: list[str] = []

    with open('input.txt', 'r') as file:
        lines = [line.rstrip('\n') for line in file]
        for line in lines:
            sequences.append(line)
    
    output = 0
    while True:
        amount_of_paper, positions = paper_cleaning_operation(
            sequence=sequences,
            is_remembering_where=True
        )
        if amount_of_paper == 0:
            break
        output += amount_of_paper
        sequences = clear_papers(sequences, positions)
    
    print(output)