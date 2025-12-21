num1 = int(input())
num2 = int(input())

answer = []
cnt = 0
for i in str(num2)[::-1]:
    temp = int(i)*num1
    print(temp)
    answer.append(temp*(10**cnt))
    cnt += 1
print(sum(answer))