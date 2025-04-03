import sys
from collections import deque

sys.setrecursionlimit(10**8)

input = sys.stdin.readline
n = int(input())   # 행, 열
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maxHeight = 0

for i in range(n):
  arr = list(map(int, input().split()))
  maxHeight = max(max(arr), maxHeight)
  graph.append(arr)

def dfs(x, y, height):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] > height:
      visited[nx][ny] = True
      dfs(nx, ny, height)

answer = 0

for i in range(0, maxHeight+1):
  visited = [[False] * (n+1) for _ in range(n+1)]
  count = 0
  
  for j in range(n):
    for k in range(n):
      if graph[j][k] > i and not visited[j][k]:
        count += 1
        visited[j][k] = True
        dfs(j, k, i)
  answer = max(answer, count)

print(answer)