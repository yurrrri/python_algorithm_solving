from collections import deque

def solution(board):
    n = len(board)
    INF = 1e9
    
    # 방향: 상(0), 좌(1), 하(2), 우(3)
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    # 3차원 거리 배열: [x][y][dir]
    distance = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

    # 초기 위치에서 네 방향 모두 시작 가능하므로 모든 후보지에 대한 distance 배열 초기화 및 큐에 추가한다.
    q = deque([])
    for i in range(4):
        distance[0][0][i] = 0
        q.append((0, 0, i, 0))  # x, y, 방향, 비용

    def calculate_cost(direction, prev_direction, cost):
        if (prev_direction - direction) % 2 == 0:
            return cost + 100
        else:
            return cost + 600

    while q:
        x, y, direction, cost = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:  # 유효한 범위에 있고, 도로를 세울 수 있는 영역일 경우
                next_cost = calculate_cost(i, direction, cost)
                if distance[nx][ny][i] > next_cost:  # 아직 방문하지 않았거나 지금 계산한 비용이 기존 최소 비용보다 더 작다면,
                    distance[nx][ny][i] = next_cost   # distance 배열 갱신 후
                    q.append((nx, ny, i, next_cost))   # 새로운 후보지를 큐에 추가한다.

    return min(distance[n - 1][n - 1])