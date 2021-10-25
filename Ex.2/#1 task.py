ans = []
for i in range(3):
    for j in range(4):
        ans.append((i, j))
print(ans)

ans = [(i, j) for i in range(3) for j in range(4)]
print(ans)

ans = [(lambda x: x*x)(x) for x in range(10) if x % 2 == 1]
print(ans)

ans = map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))
print(list(ans))