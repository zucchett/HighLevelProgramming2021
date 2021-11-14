import numpy as np

city_name = np.array(['Chicago', 'Springfield', 'Saint-Louis', 'Tulsa', 'Oklahoma City', 'Amarillo', 'Santa Fe', 'Albuquerque', 'Flagstaff', 'Los Angeles'])
city_distance = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
city_name = np.reshape(city_name, (-1, 1))
city_distance = np.reshape(city_distance, (-1, 1))
city_grid = np.append(city_name, city_distance, axis=1)
city_distance_km = city_distance * 1.61
city_grid_km = np.append(city_grid, city_distance_km, axis=1)

# print(city_distance_km)
# print(city_grid)
print(city_grid_km)