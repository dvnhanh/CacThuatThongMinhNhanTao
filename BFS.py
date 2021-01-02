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