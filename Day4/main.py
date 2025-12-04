def paper_cleaning_operation(sequence: list[str]) -> int:
    output = 0
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

    return output
                    


if __name__ == '__main__':
    sequences: list[str] = []

    with open('input.txt', 'r') as file:
        lines = [line.rstrip('\n') for line in file]
        for line in lines:
            sequences.append(line)
    
    print(paper_cleaning_operation(sequences))
    