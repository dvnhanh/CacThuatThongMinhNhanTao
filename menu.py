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