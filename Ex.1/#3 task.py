import math
def euclidean_distance(u, v):
    x = u
    y = v
    distance = math.sqrt(((x[0]-y[0])**2)+((x[1]-y[1])**2))
    print(distance)

euclidean_distance([3, 0], [0, 4])
