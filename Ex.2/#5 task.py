import math

densities = {"Al": [0.5, 1, 2], "Fe": [3, 4, 5], "Pb": [15, 20, 30]}
density = {"Al": 2.7, "Fe": 7.8, "Pb": 11.3}
radii = [1, 2, 3]


def volume_cylinder(thickness, radius):
    def circumference(radius):
        circumf_l = 2 * math.pi * radius
        return circumf_l

    volume_c = math.pi * thickness * thickness * circumference(radius)
    return volume_c

def weight_cylinder(ele, thickness, radius):
    for key in density:
        if ele in density:
            mass = volume_cylinder(thickness, radius) * density[key]
            return mass

def get_value_list(pos):
    requested_values_from_pos = [ele[pos] for ele in densities.values()]
    return requested_values_from_pos

def all_circle_weight(*args, **kwargs):
    i = 0
    circle_weight_list = []
    list_of_values = get_value_list(i)
    for key in density:
        circle_weight_list.append(weight_cylinder(key, list_of_values[i], 1))
        i += 1
    return circle_weight_list

def all_disk_weight(*args, **kwargs):
    i = 0
    disk_weight_list = []
    list_of_values = get_value_list(1)
    for key in density:
        disk_weight_list.append(weight_cylinder(key, list_of_values[i], 2))
        i += 1
    return  disk_weight_list


# print(first_result)
# print(weight_cylinder("Al", first_value))
print(all_circle_weight())
print(all_disk_weight())
