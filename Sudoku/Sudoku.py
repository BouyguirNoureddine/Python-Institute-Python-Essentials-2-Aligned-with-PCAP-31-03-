"""
Name        : Sudoku
Date        : 04/08/2024
Author      : Noureddine Bouyguir
Description : - improving the student's skills in operating with strings and lists;
              - converting strings into lists.
"""

#Grid creation 
grid=[]
for i in range(9):
    grid.append([int(c) for c in input()])

#Validty rows and cols and tiles
rows_v,cols_v,tiles_v=True,True,True

#Checking rows valid
for row in grid:
    for i in range(1,10):
        if row.count(i)>1:
            rows_v=False

#Checking colomns valid
colmns=[[row[i] for row in grid] for i in range(9)]

for col in colmns:
    for i in range(1,10):
        if col.count(i)>1:
            cols_v=False

#Checking tiles valid
tiles=[]
tiles.append([[grid[row][i+j] for row in range(3) for j in range(3)] for i in range(0,9,3) ])
tiles.append([[grid[row][i+j] for row in range(3,6) for j in range(3)] for i in range(0,9,3) ])
tiles.append([[grid[row][i+j] for row in range(6,9) for j in range(3)] for i in range(0,9,3) ])
tile_s=[tiles[k][j] for k in range(len(tiles)) for j in range(len(tiles[k]))]

for til in tile_s:
    for i in range(1,10):
        if til.count(i)>1:
            tiles_v=False
#printing results
if rows_v and cols_v and tiles_v:
    print("Yes")
else:
    print("No")