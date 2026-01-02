n, m = map(int, input().split())
basket = list(range(1, n+1))
# print(basket)

for _ in range(m):
    i, j = map(int, input().split()) # number
    s, e = i-1, j-1 # number -> index
    basket[s:e+1] = basket[s:e+1][::-1]

basket = list(map(str, basket))
print(' '.join(basket))