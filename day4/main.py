d = [
    (0, 1),  # right
    (1, 0),  # down
    (0, -1), # left
    (-1, 0), # up
    (1, 1),  # down-right
    (1, -1), # down-left
    (-1, 1), # up-right
    (-1, -1) # up-left
]

def count_words(input, word):
    matrix = input.read().strip().split("\n")

    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    def search_from_cell(x,y,dx,dy):
        for i in range(len(word)):
            new_x, new_y = x + i * dx, y + i * dy
            if new_x < 0 or new_y < 0 or new_x >= rows or new_y >= cols or matrix[new_x][new_y] != word[i]:
                return False
        return True
    
    def check_for_validity(x,y):
        if ((matrix[x-1][y-1] == 'M' and matrix[x+1][y+1] == 'S') and
            (matrix[x-1][y+1] == 'M' and matrix[x+1][y-1] == 'S')):
            return True
        if ((matrix[x-1][y-1] == 'S' and matrix[x+1][y+1] == 'M') and
            (matrix[x-1][y+1] == 'S' and matrix[x+1][y-1] == 'M')):
            return True
        if ((matrix[x-1][y-1] == 'M' and matrix[x+1][y+1] == 'S') and
            (matrix[x-1][y+1] == 'S' and matrix[x+1][y-1] == 'M')):
            return True
        if ((matrix[x-1][y-1] == 'S' and matrix[x+1][y+1] == 'M') and
            (matrix[x-1][y+1] == 'M' and matrix[x+1][y-1] == 'S')):
            return True
        return False

    def check_diagonals(x,y):
        if x > 0 and y > 0 and x < rows - 1 and y < cols - 1:
            return check_for_validity(x,y)
                
    
    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == "A":
            # for dx, dy in d:
                # if search_from_cell(x,y,dx,dy): Part 1
                if check_diagonals(x,y):
                    count += 1
    return count




with open("day4/input.txt", "r") as input:
    print(count_words(input, "XMAS")) # 1