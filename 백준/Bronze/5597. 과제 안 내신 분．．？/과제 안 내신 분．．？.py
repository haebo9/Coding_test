student = [1]*30

for _ in range(28):
    n = int(input())
    student[n-1] = 0

answer = [i+1 for i,x in enumerate(student) if x==1]
print(min(answer))
print(max(answer))