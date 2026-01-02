lst = []
for _ in range(9):
    n = int(input())
    lst.append(n)
lst_max = max(lst)
idx = lst.index(lst_max)

print(lst_max)
print(idx+1)