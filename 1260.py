from collections import deque

N, M, S = map(int, input().split())
A = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)
    
for i in range(N+1):
    A[i].sort()
    
def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)
            
visited = [False] * (N+1)
DFS(S)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in A[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                
print()
visited = [False] * (N+1)
BFS(S)
