def display_grid(g):
    for r in g:
        for c in range(0,9,3):
            print(" ".join(map(str,r[c:c+3])),end="|")
        print()

def check(g,r,c,n):
    if n in g[r]:
        return False
    for i in range(9):
        if g[i][c]==n:
            return False
    starting_r=r-(r%3)
    starting_c=c-(c%3)
    for i in range(3):
        for j in range(3):
            if g[starting_r+i][starting_c+j]==n:
                return False
    return True

def find_null(g):
    for i in range(9):
        for j in range(9):
            if g[i][j]==0:
                return (i,j)
    return None

def validate(g):
    for i in range(9):
        for j in range(9):
            num=g[i][j]
            if num not in [1,2,3,4,5,6,7,8,9,0]:
                return False
            if num!=0:
                for row in range(9):
                    if g[row][j]==num and row!=i:
                        return False
                for col in range(9):
                    if g[i][col]==num and col!=j:
                        return False
                box_r=i//3
                box_c=j//3
                for r in range(box_r*3,(box_r*3)+3):
                    for c in range(box_c*3,(box_c*3)+3):
                            if (r!=i or c!=j) and g[r][c]==num:
                                return False
    return True

def main_solver(g):
    if validate(g)==False:
        return False
    empty_cell=find_null(g)
    if empty_cell==None:
        return True
    row,col=empty_cell
    for i in range(1,10):
        if check(g,row,col,i):
            g[row][col]=i
            if main_solver(g):
                return True
        g[row][col]=0
    return False

unsolved_sudoku=[
    [0, 4, 0, 0, 0, 0, 0, 0, 7],
[0, 0, 6, 0, 0, 0, 8, 0, 0],
[0, 0, 0, 3, 0, 4, 1, 0, 0],
[8, 0, 0, 7, 1, 0, 0, 0, 0],
[7, 0, 0, 9, 0, 0, 0, 0, 0],
[5, 6, 2, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 7, 0, 5, 2],
[0, 0, 0, 0, 2, 0, 0, 0, 0],
[0, 8, 0, 0, 5, 0, 0, 6, 6],]
print("\n================Unsolved board:======================")
display_grid(unsolved_sudoku)
if main_solver(unsolved_sudoku):
    print("\n================Solved board:======================")
    display_grid(unsolved_sudoku)
else:
    print("\nInvalid board")

