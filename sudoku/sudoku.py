

grid = [1,3,6,4,5,9,8,7,2,5,7,2,3,8,1,6,9,4,8,4,9,7,6,2,5,1,3,3,2,8,5,1,7,4,6,9,4,5,7,9,3,6,2,8,1,9,6,1,8,2,4,7,3,5,7,8,3,1,4,5,9,2,6,6,1,5,2,9,8,3,4,7,2,9,4,6,7,3,1,5,8]



def check_line(grid):
    pointer = 0
    i = 0
    gridline = [0] * 9
    while pointer < 81:
        gridline[i] = grid[pointer]

        if (pointer + 1) % 9 == 0:
            i = 0
            is_distinct = len(set(gridline))
            if is_distinct != 9:
                print("Error in line")
                break
        else:
            i += 1

        print(gridline, pointer)
        pointer += 1


def check_col(grid):
    pointer = 0

    for _ in


check_line(grid)