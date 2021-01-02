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