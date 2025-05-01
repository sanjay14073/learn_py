##Graphs
my_graph={
    0:[1,2],
    1:[0,2],
    2:[1,0]
}

visited=[False]*len(my_graph)

def dfs(my_graph,start,visited):
    print(start)
    visited[start]=True
    for i in my_graph[start]:
        if not visited[i]:
            dfs(my_graph,i,visited)

visited=[False]*len(my_graph)

def bfs(my_graph, start, visited):
    queue = [start]
    visited[start] = True

    while queue:
        s = queue.pop(0)
        print(s)

        for i in my_graph[s]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(my_graph,0,visited)
bfs(my_graph,0,visited)