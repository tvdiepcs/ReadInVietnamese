import WP7
def calculate_euclidean_distance_between_points(points):
    if(points.__len__()<2):
        print('ValueError: The list MUST contain at least 2 points')
        return
    return sum([calculate_euclidean_distance_between_2_points(points[i],points[i+1]) for i in range(0,len(points)-1)])
        
calculate_euclidean_distance_between_points([(0, 0), (3, 4), (-1, -1)])
calculate_euclidean_distance_between_points([(1, 1)])
calculate_euclidean_distance_between_points([])