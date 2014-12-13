# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]


# Helper functions made for readability
# next_node abuses the -1 index wraparound of Python
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

def test(x=0):
    testcase1 = [(1, 2), (2, 3), (3, 1)]
    testcase2 = [(0, 1), (1, 5), (1, 7), (4, 5),(4, 8), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
    testcase3 = [(8, 16), (8, 18), (16, 17), (18, 19),(3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),(1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),(6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
hardtest2 = [(0, 1), (1, 2), (2, 0),(2, 3), (3, 4), (4, 2),(4, 5), (5, 6), (6, 4),(6, 7), (7, 8), (8, 6), (8, 9), (9, 10), (10, 8), (10, 11), (11, 12), (12, 10), (12, 13), (13, 14), (14, 15), (15, 16), (16, 14), (16, 17), (17, 18), (18, 16), (18, 19), (19, 20), (20, 18), (20, 21), (21, 22), (22, 20), (22, 23), (23, 24), (24, 22), (24, 25), (25, 26), (26, 24),(26, 27), (27, 28), (28, 26), (28, 29), (29, 30), (30, 28),(30, 31), (31, 32), (32, 30), (32, 33), (33, 34), (34, 32), (34, 35), (35, 36), (36, 34), (36, 37), (37, 38), (38, 36), (38, 39), (39, 40), (40, 38), (40, 41), (41, 42), (42, 40), (42, 43), (43, 44), (44, 42), (44, 45), (45, 46), (46, 44), (46, 47), (47, 48), (48, 46), (48, 49), (49, 50), (50, 48), (50, 51), (51, 52), (52, 50), (52, 53), (53, 54), (54, 52), (54, 55), (55, 56), (56, 54), (56, 57), (57, 58), (58, 56), (58, 59), (59, 60), (60, 58), (60, 61), (61, 62), (62, 60), (62, 63), (63, 64), (64, 62), (64, 65), (65, 66), (66, 64), (66, 67), (67, 68), (68, 66), (68, 69), (69, 70), (70, 68),(70, 71), (71, 72), (72, 70), (72, 73), (73, 74), (74, 72),(74, 75), (75, 76), (76, 74), (76, 77), (77, 78), (78, 76),(78, 79), (79, 80), (80, 78), (80, 81), (81, 82), (82, 80),(82, 83), (83, 84), (84, 82), (84, 85), (85, 86), (86, 84),(86, 87), (87, 88), (88, 86), (88, 89), (89, 90), (90, 88),(90, 91), (91, 92), (92, 90), (92, 93), (93, 94), (94, 92),(94, 95), (95, 96), (96, 94), (96, 97), (97, 98), (98, 96),(98, 99), (99, 100), (100, 98)]




print (find_eulerian_path([(1, 2), (2, 3), (3, 1)]))
print (find_eulerian_path([(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]))
print(find_eulerian_path([(8, 16), (8, 18), (16, 17), (18, 19),
(3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),
(1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),
(6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)], all_paths=False))
print()


print(find_eulerian_path([(1, 2), (1,4), (1,3), (2,3), (2, 5), (3, 4), (3, 5)], True))
print(find_eulerian_path([(1,2),(2,3),(3,4),(4,1),(1,5),(5,6),(6,4)], True))



print(find_eulerian_path(hardtest2))

"""
[3]–––––––––––––––[4]––––––––––––––––[6]
 |                 |                  |
[2]–––––––––––––––[1]––––––––––––––––[5]
"""