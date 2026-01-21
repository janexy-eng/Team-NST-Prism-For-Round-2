import math
def display_grid(g,k):
    for r in g:
        for c in range(0,k,int(k**(0.5))):
            print(" ".join(map(str,r[c:c+int(k**0.5)])),end="|")
        print()
def check(g,r,c,n,k):
    if n in g[r]:
        return False
    for i in range(k):
        if g[i][c]==n:
            return False
    starting_r=r-(r%(int(k**0.5)))
    starting_c=c-(c%(int(k**0.5)))
    for i in range(int(k**0.5)):
        for j in range(int(k**0.5)):
            if g[starting_r+i][starting_c+j]==n:
                return False
    return True
def find_null(g,k):
    for i in range(k):
        for j in range(k):
            if g[i][j]==0:
                return (i,j)
    return None
def validate(g,k):
    if not math.isqrt(k):
        return False
    for i in range(k):
        for j in range(k):
            num=g[i][j]
            if num not in [1,2,3,4,5,6,7,8,9,0]:
                return False
            if num!=0:
                for row in range(k):
                    if g[row][j]==num and row!=i:
                        return False
                for col in range(k):
                    if g[i][col]==num and col!=j:
                        return False
                box_r=i//int(k**0.5)
                box_c=j//int(k**0.5)
                for r in range(box_r*(int(k**0.5)),(box_r*(int(k**0.5)))+int(k**0.5)):
                    for c in range(box_c*(int(k**0.5)),(box_c*(int(k**0.5)))+(int(k**0.5))):
                            if (r!=i or c!=j) and g[r][c]==num:
                                return False
    return True
def main_solver(g,k):
    if validate(g,k)==False:
        return False
    empty_cell=find_null(g,k)
    if empty_cell==None:
        return True
    row,col=empty_cell
    for i in range(1,k+1):
        if check(g,row,col,i,k):
            g[row][col]=i
            if main_solver(g,k):
                return True
        g[row][col]=0
    return False
unsolved_sudoku=grid = [
    [1, 0, 3],
    [0, 1, 0],
    [2, 0, 1]
]
print("\n================Unsolved board:======================")
display_grid(unsolved_sudoku,3)
if main_solver(unsolved_sudoku,3):
    print("\n================Solved board:======================")
    display_grid(unsolved_sudoku,3)
else:
    print("\nInvalid board")
