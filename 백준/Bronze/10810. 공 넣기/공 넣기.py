n, m = map(int, input().split())
balls = [0]*n
for _ in range(m):
    i, j, k = map(int, input().split())
    for t in range(i-1, j):
        balls[t] = k

print(' '.join(map(str, balls)))