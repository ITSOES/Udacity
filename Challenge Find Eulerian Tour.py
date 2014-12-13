# Helper functions made for readability
# next_node abuses the -1 index wraparound of Python
from collections import Counter
use_harder_tests = True

next_node = lambda current, edge: edge[edge.index(current)-1]

# deepcopy()s but removes without
deepcopy = lambda x, without: [x for x in x if x is not without]
def find_eulerian_path(graph, all_paths=False):
    """
    If all_paths, then returns a list of all possible paths from position graph[0][0]
    else returns first path found. Returns an empty list if no paths possible.
    Assumes unique tuples for graph (although a change to deepcopy would allow repeated tuples).
    """
    # heap ==> [path, node, remaining]
    heap = [[[], graph[0][0], graph]]
    results = []

    while heap:
        c_path, current, remaining = heap.pop()
        c_path = c_path + [current]

        if not remaining:
            if all_paths:
                results.append(c_path)
            else: return c_path

        for edge in remaining:
            if current in edge:
                heap.append([c_path, next_node(current, edge), deepcopy(remaining, edge)])


    return results


def is_euler_tour(graph):
    tour = Counter()
    for i, j in graph: 
        tour[i] += 1
        tour[j] += 1
    for n in tour.values():
        #print('counts', tour, n)
        if n % 2 != 0:
            return False
    return True


def find_eulerian_tour(graph, all_paths=False, need_tour=True):
    
    """
    If all_paths, then returns a list of all possible paths from position graph[0][0]
    else returns first path found. Returns an empty list if no paths possible.
    Assumes unique tuples for graph (although a change to deepcopy would allow repeated tuples).
    """
    if need_tour and not is_euler_tour(graph):
        return []

    # heap ==> [path, node, old]
    heap = [[[], graph[0][0], []]]
    results = []
    while heap:
        c_path, current, old = reheap = heap.pop()

        if len(c_path) == len(graph):
            if all_paths:
                results.append(c_path  + [current])
            else: return c_path + [current]

        for edge in filter(lambda x: x not in old, graph):
            if current in edge:
                heap.append([c_path  + [current],
                             next_node(current, edge), old + [(edge)]])

    return results

hardtest1 = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 2), 
(4, 5), (5, 6), (6, 4), (6, 7), (7, 8), (8, 6), 
(8, 9), (9, 10), (10, 8), (10, 11), (11, 12), (12, 10), 
(12, 13), (13, 14), (14, 12), (14, 15), (15, 16), 
(16, 14), (16, 17), (17, 18), (18, 16), (18, 19), 
(19, 20), (20, 18), (20, 21), (21, 22), (22, 20), 
(22, 23), (23, 24), (24, 22), (24, 25), (25, 26), 
(26, 24), (26, 27), (27, 28), (28, 26), (28, 29), 
(29, 30), (30, 28), (30, 31), (31, 32), (32, 30), 
(32, 33), (33, 34), (34, 32), (34, 35), (35, 36), 
(36, 34), (36, 37), (37, 38), (38, 36), (38, 39), (39, 40), (40, 38), (40, 41), (41, 42), (42, 40), (42, 43), 
(43, 44), (44, 42), (44, 45), (45, 46), (46, 44), (46, 47), (47, 48), (48, 46), (48, 49), (49, 50), 
(50, 48), (50, 51), (51, 52), (52, 50), (52, 53), 
(53, 54), (54, 52), (54, 55), (55, 56), (56, 54), 
(56, 57), (57, 58), (58, 56), (58, 59), (59, 60), 
(60, 58), (60, 61), (61, 62), (62, 60), (62, 63), 
(63, 64), (64, 62), (64, 65), (65, 66), (66, 64), 
(66, 67), (67, 68), (68, 66), (68, 69), (69, 70), (70, 68),
(70, 71), (71, 72), (72, 70), (72, 73), (73, 74), (74, 72),
(74, 75), (75, 76), (76, 74), (76, 77), (77, 78), (78, 76),
(78, 79), (79, 80), (80, 78), (80, 81), (81, 82), (82, 80),
(82, 83), (83, 84), (84, 82), (84, 85), (85, 86), (86, 84),
(86, 87), (87, 88), (88, 86), (88, 89), (89, 90), (90, 88),
(90, 91), (91, 92), (92, 90), (92, 93), (93, 94), (94, 92),
(94, 95), (95, 96), (96, 94), (96, 97), (97, 98), (98, 96),
(98, 99), (99, 100), (100, 98)]
hardtest2 = [(0, 1), (1, 2), (2, 0),(2, 3), (3, 4), (4, 2),(4, 5), (5, 6), (6, 4),(6, 7), (7, 8), (8, 6), (8, 9), (9, 10), (10, 8), (10, 11), (11, 12), (12, 10), (12, 13), (13, 14), (14, 15), (15, 16), (16, 14), (16, 17), (17, 18), (18, 16), (18, 19), (19, 20), (20, 18), (20, 21), (21, 22), (22, 20), (22, 23), (23, 24), (24, 22), (24, 25), (25, 26), (26, 24),(26, 27), (27, 28), (28, 26), (28, 29), (29, 30), (30, 28),(30, 31), (31, 32), (32, 30), (32, 33), (33, 34), (34, 32), (34, 35), (35, 36), (36, 34), (36, 37), (37, 38), (38, 36), (38, 39), (39, 40), (40, 38), (40, 41), (41, 42), (42, 40), (42, 43), (43, 44), (44, 42), (44, 45), (45, 46), (46, 44), (46, 47), (47, 48), (48, 46), (48, 49), (49, 50), (50, 48), (50, 51), (51, 52), (52, 50), (52, 53), (53, 54), (54, 52), (54, 55), (55, 56), (56, 54), (56, 57), (57, 58), (58, 56), (58, 59), (59, 60), (60, 58), (60, 61), (61, 62), (62, 60), (62, 63), (63, 64), (64, 62), (64, 65), (65, 66), (66, 64), (66, 67), (67, 68), (68, 66), (68, 69), (69, 70), (70, 68),(70, 71), (71, 72), (72, 70), (72, 73), (73, 74), (74, 72),(74, 75), (75, 76), (76, 74), (76, 77), (77, 78), (78, 76),(78, 79), (79, 80), (80, 78), (80, 81), (81, 82), (82, 80),(82, 83), (83, 84), (84, 82), (84, 85), (85, 86), (86, 84),(86, 87), (87, 88), (88, 86), (88, 89), (89, 90), (90, 88),(90, 91), (91, 92), (92, 90), (92, 93), (93, 94), (94, 92),(94, 95), (95, 96), (96, 94), (96, 97), (97, 98), (98, 96),(98, 99), (99, 100), (100, 98)]
hardtest3 = [(0, 1), (1, 2), (2, 0),(0, 3), (3, 4), (4, 0),(0, 5), (5, 6), (6, 0),(0, 7), (7, 8), (8, 0),(0, 9), (9, 10), (10, 0),(0, 11), (11, 12), (12, 0),(0, 13), (13, 14), (14, 0)]


print (find_eulerian_tour([(1, 2), (2, 3), (3, 1)]))
print (find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5),(4, 8), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)], True))

print(find_eulerian_tour(hardtest1))
print(find_eulerian_tour(hardtest2))  # == []
print(find_eulerian_tour(hardtest3))
