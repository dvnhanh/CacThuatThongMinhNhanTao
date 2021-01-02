
import numpy as np
from math import sqrt
# vẽ map
def get_color_coded_background(i):
    return "\033[4{}m {} \033[0m".format(i+1, i)
def print_a_ndarray(map, row_sep=" "):
    n, m = map.shape
    fmt_str = "\n".join([row_sep.join(["{}"]*m)]*n)
    print(fmt_str.format(*map.ravel()))
matrix=np.loadtxt("input.txt",dtype='i',delimiter=',')




start="------- Start=1"
end="    End=2"
key="    Key=3"
energy="   Energy=4  ------"

def astar(lab):
    (i_s, j_s) = [[(i, j) for j, cell in enumerate(row) if cell == 2] for i, row in enumerate(lab) if 2 in row][0][0]
    (i_e, j_e) = [[(i, j) for j, cell in enumerate(row) if cell == 3] for i, row in enumerate(lab) if 3 in row][0][0]
    width = len(lab[0])
    height = len(lab)
    heuristic = lambda i, j: abs(i_e - i) + abs(j_e - j)
    comp = lambda state: state[2] + state[3]
    fringe = [((i_s, j_s), list(), 0, heuristic(i_s, j_s))]
    visited = {}
    while True:
        state = fringe.pop(0)
        (i, j) = state[0]
        if lab[i][j] == 3:
            path = [state[0]] + state[1]
            path.reverse()
            return path
        visited[(i, j)] = state[2]
        neighbor = list()
        if i > 0 and lab[i-1][j] > 0:
            neighbor.append((i-1, j))
        if i < 10 and lab[i + 1][j] > 0:
            neighbor.append((i + 1, j))
        if j > 0 and lab[i][j-1] > 0:
            neighbor.append((i, j-1))
        if j < width and lab[i][j+1] > 0:
            neighbor.append((i, j+1))
        for n in neighbor:
            next_cost = state[2] + 1
            if n in visited and visited[n] >= next_cost and n==3:
                continue
            print('[(', i, j,')]')  # xuat ra duong di
            matrix[i][j]="X" # danh dau duong di
            fringe.append((n, [state[0]] + state[1], next_cost, heuristic(n[0], n[1])))
        fringe.sort(key=comp)
num_rows = len(matrix)
num_cols = len(matrix[0])
goal_state = (num_rows - 1, num_cols - 1)
def dfs(current_path):
    row, col = current_path[-1]
    if (row, col) == goal_state:
        return True

    for direction in [(row, col + 1),  (row + 1, col),(row+1,col)]:
        new_row, new_col = direction

        if (0 <= new_row < num_rows and 0 <= new_col < num_cols and
                matrix[new_row][new_col] ==0 and
                (new_row, new_col) not in current_path):
            current_path.append((new_row, new_col))
            matrix[new_row, new_col] == 'X'  # danh dau duong di
            print('[(', new_row, new_col, ')]')
            if dfs(current_path):
                return True
            else:
                current_path.pop()
def bfs(matrix, row, col, visited):
    nodes = [(row, col)]
    while nodes:
        row, col = nodes.pop(0)
        if row >= len(matrix) or col >= len(matrix[0]) or row < 0 or col < 0 and matrix[row][col]==3:
            continue
        if (row, col) not in visited:
            if matrix[row][col] == 0:
                visited.append((row, col))
                nodes.append((row + 1, col))
                nodes.append((row, col + 1))
                nodes.append((row, col - 1))
def bfs_wrapper(matrix):
    visited = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if (i, j) not in visited:
                bfs(matrix, i, j, visited)
                matrix[i, j] == 9  # danh dau duong di
                print('[(', i, j, ')]')

    return visited

dirs = [
    lambda x, y, z, p: (x, y + 1, z + 1, p + [(x, y)]),
    lambda x, y, z, p: (x - 1, y, z + 1, p + [(x, y)]),
    lambda x, y, z, p: (x + 1, y, z + 1, p + [(x, y)]),
    lambda x, y, z, p: (x - 1, y - 1, z + sqrt(2), p + [(x, y)]),
    lambda x, y, z, p: (x + 1, y - 1, z + sqrt(2), p + [(x, y)]),
    lambda x, y, z, p: (x - 1, y + 1, z + sqrt(2), p + [(x, y)]),
    lambda x, y, z, p: (x + 1, y + 1, z + sqrt(2), p + [(x, y)])
]
def valid(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

def adjacent(grid, frontier):
    for (x, y, z, p) in frontier:
        for d in dirs:
            nx, ny, nz, np = d(x, y, z, p)
            if valid(grid, nx, ny):
                yield (nx, ny, nz, np)
def flood(grid, frontier):
    res = list(adjacent(grid, frontier))
    for (x, y, z, p) in frontier:
        grid[x][y] = 1
    return res

def UCS(grid, start, end):
    start, end = tuple(start), tuple(end)
    frontier = [(start[0], start[1], 0, [])]
    res = []
    while frontier and grid[end[0]][end[1]] == 0:
        frontier = flood(grid, frontier)
        for (x, y, z, p) in frontier:
            matrix[x, y] == 'X'  # danh dau duong di
            print('[(', x, y, ')]')
            if (x, y) == end:
                res.append((z, p + [(x, y)]))
    if not res:
        return ()
    return sorted(res)[0]


back_map_modified = np.vectorize(get_color_coded_background)(matrix)
print("-------------------------------------------------------")
print_a_ndarray(back_map_modified, row_sep="")
print("-------------------------------------------------------")
print(start,end,key,energy)
print("-------------------------------------------------------")
print("------ 1.DFS       2.BFS      3.UCS       4.A*     ----")
print("-------------------------------------------------------")
number=input('Nhap loai thuat toan muon chay: ')



if number=="1":
    print("đường đi:")
    dfs([(0,0)])
if number=="2":
    print("đường đi:")
    bfs_wrapper(matrix)
if number=="3":
    print("đường đi:")
    astar(matrix)
if number=="4":
    print("đường đi:")
    UCS(matrix, (0, 0), (9, 9))

 # NGUỒN THAO KHẢO CHÍNH https://stackoverflow.com/