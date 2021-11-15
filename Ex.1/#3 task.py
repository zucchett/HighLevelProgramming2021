import math
def euclidean_distance(u, v):
    distance = math.sqrt(((u[0]-v[0])**2)+((u[1]-v[1])**2))
    print(distance)

euclidean_distance([3, 0], [0, 4])
