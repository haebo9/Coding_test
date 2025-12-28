import sys

t = int(sys.stdin.readline().rstrip())

for i in range(1, t+1):
    a, b = map(int, sys.stdin.readline().split())
    c = a+b
    print(f'Case #{i}: {a} + {b} = {c}')