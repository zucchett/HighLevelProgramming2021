import numpy as np

def mult_table(n):
    rng = np.arange(1, n+1)
    return rng * rng[:, None]
arr = mult_table(10)
trace_number = mult_table(10).trace()
anti_diag = np.fliplr(arr).diagonal()
diag_upward = arr.diagonal(offset=1)
print(arr)
print(trace_number)
print(anti_diag)
print(diag_upward)

