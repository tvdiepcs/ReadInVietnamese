import math
def calculate_euclidean_distance_between_2_points(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
calculate_euclidean_distance_between_2_points((0, 0), (3, 4))