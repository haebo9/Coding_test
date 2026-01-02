n = int(input())

scores = list(map(int, input().split()))
max_s = max(scores)
scores = list(map(lambda x: x/max_s * 100, scores))
print(sum(scores) /len(scores))