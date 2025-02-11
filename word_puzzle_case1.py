def is_present(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])

    def search(row, col, i, direction):
        if i == len(word): 
            return True
        if row < 0 or row >= rows or col < 0 or col >= cols or word[i] != matrix[row][col]:
            return False
        temp = matrix[row][col]
        matrix[row][col] = '#'

        x, y = direction
        if search(row + x, col + y, i + 1, direction):
            matrix[row][col] = temp
            return True

        matrix[row][col] = temp
        return False

    directions = {
        "north_west": (-1, -1),
        "north": (-1, 0),
        "north_east": (-1, 1),
        "west": (0, -1),
        "east": (0, 1),
        "south_west": (1, -1),
        "south": (1, 0),
        "south_east": (1, 1)
    }

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == word[0]:
                for dir_name, (x, y) in directions.items():
                    if search(row, col, 0, (x, y)):
                        return True

    return False 

matrix = [
    ['A', 'B', 'C', 'R'],
    ['U', 'G', 'A', 'A'],
    ['N', 'O', 'R', 'T'],
    ['T', 'D', 'S', 'S']
]

print("Word Search Matrix:")
for row in matrix:
    print(" ".join(row))

word = input("\nEnter the word you want to find: ").strip().upper()

result = is_present(matrix, word)
print(result)