def print_grid(g):
    for r in g:
        print(" ".join(map(str, r)))

def is_safe(g, r, c, n):
    if n in g[r]:
        return False
    for i in range(9):
        if g[i][c] == n:
            return False
    sr, sc = r - r % 3, c - c % 3
    for i in range(3):
        for j in range(3):
            if g[sr + i][sc + j] == n:
                return False
    return True

def find_empty(g):
    for i in range(9):
        for j in range(9):
            if g[i][j] == 0:
                return i, j
    return None

def solve(g):
    e = find_empty(g)
    if not e:
        return True
    r, c = e
    for n in range(1, 10):
        if is_safe(g, r, c, n):
            g[r][c] = n
            if solve(g):
                return True
            g[r][c] = 0
    return False

grid = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

if solve(grid):
    print_grid(grid)
