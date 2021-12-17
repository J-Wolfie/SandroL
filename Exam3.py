def second_state(column, row, grid):
    answer = [["O"]*column for x in range(row)]
    for i in range(row):
        for j in range(column):
            cell = grid[i][j]
            if cell =='O':
                answer[i][j] = '.'
                if i>0:
                    answer[i-1][j] = '.'
                if j>0:
                    answer[i][j-1] = '.'
                if i<column-1:
                    answer[i+1][j] = '.'
                if j<row-1:
                    answer[i][j+1] = '.'
    return answer
time, column, row = input().strip().split()
time = int(time)
column = int(column)
row = int(row)
grid = []
for i in range(row):
    a=input()
    grid.append(list(a))
if time%2==0:
    print([["O"]*column for i in range(row)])
elif time%4==1:
    print(grid)
else:
    print(second_state(column, row, grid))