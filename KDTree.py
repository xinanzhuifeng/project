#1，2，3，5

class KDTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class KDTree:
    def __init__(self, data_list):
        k = len(data_list[0]) # number of dimensions

        def build_subtree(data_sublist, depth):
            if not data_sublist:
                return None

            axis = depth % k # the current axis to use for partitioning
            data_sublist.sort(key=lambda x: x[axis])
            median = len(data_sublist) // 2

            return KDTreeNode(data_sublist[median],
                              build_subtree(data_sublist[:median], depth+1),
                              build_subtree(data_sublist[median+1:], depth+1))

        self.root = build_subtree(data_list, 0)



    def insert(self, point):
        """Insert a point into the KDTree.
        """
        def insert_subtree(node, point, depth):
            if not node:
                return KDTreeNode(point)

            axis = depth % k
            if point[axis] < node.data[axis]:
                node.left = insert_subtree(node.left, point, depth+1)
            else:
                node.right = insert_subtree(node.right, point, depth+1)
            return node

        self.root = insert_subtree(self.root, point, 0)


    def range(self, lower_bound, upper_bound):
        """Return all points in the KDTree that are within a given range.
        """
        def range_subtree(node, lower_bound, upper_bound, depth, result):
            if not node:
                return

            axis = depth % k
            if lower_bound[axis] <= node.data[axis] <= upper_bound[axis]:
                result.append(node.data)

            if lower_bound[axis] <= node.data[axis]:
                range_subtree(node.left, lower_bound, upper_bound, depth+1, result)

            if node.data[axis] <= upper_bound[axis]:
                range_subtree(node.right, lower_bound, upper_bound, depth+1, result)

        result = []
        range_subtree(self.root, lower_bound, upper_bound, 0, result)
        return result

    def nearest_neighbor(self, point):
        """Return the point in the KDTree closest to a given point.
        """
        best_point = None
        best_distance = float('inf')

        def nearest_neighbor_subtree(node, point, depth):
            nonlocal best_point
            nonlocal best_distance

            if not node:
                return

            axis = depth % k
            next_best, next_branch = None, None
            if point[axis] < node.data[axis]:
                next_branch = node.left
                if point[axis] >= node.data[axis]:
                    next_best = node.data
            else:
                next_branch = node.right
                if point[axis] < node.data[axis]:
                    next_best = node.data
            nearest_neighbor_subtree(next_branch, point, depth+1)

            distance = euclidean_distance(point, node.data)
            if distance < best_distance:
                best_distance = distance
                best_point = node.data

            if next_best:
                distance = euclidean_distance(point, next_best)
                if distance < best_distance:
                    best_distance = distance
                    best_point = next_best
        
        nearest_neighbor_subtree(self.root, point, 0)
        return best_point



#4
import matplotlib.pyplot as plt
import random
import time

def generate_random_points(n):
    return [(random.random(), random.random()) for _ in range(n)]

def naive_range_query(points, lower_bound, upper_bound):
    return [p for p in points if lower_bound[0] <= p[0] <= upper_bound[0] and lower_bound[1] <= p[1] <= upper_bound[1]]

points_sizes = [10, 50, 100, 500, 1000, 5000, 10000]
naive_times = []
kdtree_times = []

for n in points_sizes:
    points = generate_random_points(n)
    lower_bound = (0, 0)
    upper_bound = (1, 1)

    # Measure time for naive method
    start_time = time.time()
    naive_range_query(points, lower_bound, upper_bound)
    end_time = time.time()
    naive_times.append(end_time - start_time)

    # Measure time for k-d tree method
    kdtree = KDTree(points)
    start_time = time.time()
    kdtree.range(lower_bound, upper_bound)
    end_time = time.time()
    kdtree_times.append(end_time - start_time)

# Plot results
plt.plot(points_sizes, naive_times, label='Naive method')
plt.plot(points_sizes, kdtree_times, label='K-d tree method')
plt.xlabel('Number of points')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()



