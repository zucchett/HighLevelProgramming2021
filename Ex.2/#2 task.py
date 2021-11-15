def f(alist):
    new_list = alist + [x for x in range(5)]
    return new_list

alist = [1,2,3]
ans = f(alist)
print(ans)
print(alist)