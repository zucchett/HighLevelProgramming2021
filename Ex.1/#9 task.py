a = tuple(range(1, 10))
def normalization(*args):
    norm = [float(i) / sum(a) for i in a]
    return norm
print(normalization())