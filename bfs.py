
visited=[]
queue=[]
graph={
    '5':['3','7'],
    '3':['2','4'],
    '2':[],
    '7':['8'],
    '4':['8'],
    '8':[]
}
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for neig in graph[m]:
            if neig not in visited:
                visited.append(neig)
                queue.append(neig)

print("Following is Breadth First Search graph:")
bfs(visited,graph,'5')
