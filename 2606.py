N = int(input())
M = int(input())
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v):
    visited[v] = True
    for i in range(1, N+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)
# 1번 컴퓨터가 웜 바이러스에 걸렸으므로 dfs(1) 호출
dfs(1)
print(visited.count(True)-1)
