from numpy import matrix
from collections import defaultdict

edges={(1, 'a'): [2, 3],
    (2, 'a'): [2],
    (3, 'b'): [4, 3],
    (4, 'c'): [5]}
accepting=[2, 5]


class MatrixFSMSolver:
    """
transform_matrix_collection is the matrix equivalent of the edges fsm below
    edges = { (1, 'a') : [2, 3],
              (2, 'a') : [2],
              (3, 'b') : [4, 3],
              (4, 'c') : [5] }
    accepting = [2, 5]
    """
    nfsm_length=0
    transform_matrix_collection={
        'a': matrix([[0, 1, 1, 0, 0],  # (1, 'a') : [2, 3]
            [0, 1, 0, 0, 0],  # (2, 'a') : [2]
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
        ),
        'b': matrix([[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],  # (3, 'b') : [4, 3]
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
        ),
        'c': matrix([[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],  # (4, 'c') : [5]
            [0, 0, 0, 0, 0]]
        ),

    }
    # accepting = matrix([0, 1, 0, 0, 1])  # accepting = [2, 5]

    def __init__(self, edges=edges, accepting=accepting):
        self.nfsm_length=self.elen(edges)
        self.transform_matrix_collection=self.transform_to_matrices(edges)
        self.accepting=matrix(
            '{:0{}b}'.format(sum(2**x for x in accepting)/2, self.nfsm_length).replace('', ' ')[::-1])

    def check_string(self, string, start_state):
        try:
            return (reduce(self.f, string, start_state) & self.accepting).any()
        except (KeyError, StopIteration):
            return False

    # @staticmethod
    def f(self, x, y):
        result=x*self.transform_matrix_collection[y]
        if result.any():
            return result
        else:
            raise StopIteration

    def elen(self, edges):
        hold=set(x[0] for x in edges) | set(y for x in edges.values() for y in x)
        return max(hold)


    def nfsmsim(self, string, current, edges, accepting):
        self.nfsm_length=self.elen(edges)
        self.transform_matrix_collection=self.transform_to_matrices(edges)
        # print self.transform_matrix_collection
        range=xrange(1, self.nfsm_length+1)
        start_state=matrix([x == current for x in range])
        self.accepting=matrix(
            '{:0{}b}'.format(sum(2**x for x in accepting)/2, self.nfsm_length-1).replace('', ' ')[::-1])
        # print('accccccep', self.accepting)
        return self.check_string(string, start_state)

    def transform_to_matrices(self, edges):
        result=defaultdict(lambda: matrix([[0]*self.nfsm_length]*self.nfsm_length))
        for e, l in edges:
            for d in edges[e, l]:
                result[l][e-1, d-1]=1
        return result

        # def initialize(self, edges):


# Test case
edges={(1, 'a'): [2, 3],
    (2, 'a'): [2],
    (3, 'b'): [4, 3],
    (4, 'c'): [5]}
accepting=[2, 5]
edges2={(1, 'a'): [2, 3],
    (2, 'a'): [2],
    (3, 'b'): [4, 2],
    (4, 'c'): [5]}
fsm=MatrixFSMSolver()
nfsmsim=fsm.nfsmsim


# print nfsmsim("abc", 1, edges2, accepting)
start_state=([1, 0, 0, 0, 0])
# print "Test case 1 passed: " + str(fsm.check_string("abc", start_state))
# print "Test case 2 passed: " + str(fsm.check_string("aaa", start_state))
# print "Test case 3 passed: " + str(fsm.check_string("abbbc", start_state))
# print "Test case 4 passed: " + str(fsm.check_string("aaaacaaa", start_state) == False)
# print "Test case 5 passed: " + str(fsm.check_string("", start_state) == False)
# # print
# print "Test case 1 passed: " + str(nfsmsim("abc", 1, edges, accepting) == True)
# print "Test case 2 passed: " + str(nfsmsim("aaa", 1, edges, accepting) == True)
# print "Test case 3 passed: " + str(nfsmsim("abbbc", 1, edges, accepting) == True)
# print "Test case 4 passed: " + str(nfsmsim("aabc", 1, edges, accepting) == False)
# print "Test case 5 passed: " + str(nfsmsim("", 1, edges, accepting) == False)


def nfsmsim(string, current, edges, accepting):
    return (reduce(lambda y, l: y and # makes code faster; not needed
                                sum(set(1<<x for c in [i for i, e in enumerate(bin(y)[::-1]) # unpacks y
                                                      if e == '1']
                                             for x in edges.get((c, l), []))),
                   string, 1<<current) &
            sum(set(1<<x for x in accepting)))


def nfsmsim(string, current, edges, accepting):
    return bool(reduce(fsm_reduce,
                       string,
                       ba(current)) & ba(accepting))

def fsm_reduce(y, l):
    return y and ba(x
                    for c in get_edges(y)
                    for x in edges.get((c, l), []))

def get_edges(y):
    return [i for i, e in enumerate(bin(y)[::-1]) if e == '1']

def ba(y): # binary array made from number(s)
    return sum(2**y for y in y) if not isinstance(y, int) else 2**y

temp=nfsmsim("abc", 1, edges, accepting)
# print temp & ba(accepting), bin(temp), 'get edges', get_edges(temp), ba(accepting)
print 'lll'
print "Test case 1 passed: "+str(nfsmsim("abc", 1, edges, accepting))
print "Test case 2 passed: "+str(nfsmsim("aaa", 1, edges, accepting))
print "Test case 3 passed: "+str(nfsmsim("abbbc", 1, edges, accepting))
print "Test case 4 passed: "+str(nfsmsim("aabc", 1, edges, accepting) == False)
print "Test case 5 passed: "+str(nfsmsim("", 1, edges, accepting) == False)

edges={(1, 'a'): [2, 3],
    (2, 'a'): [2],
    (3, 'b'): [4, 2],
    (4, 'c'): [5]}
accepting=[5]
# ... accepts exactly one string: "abc". By contrast, this
# non-deterministic machine:
edges2={(1, 'a'): [1],
    (2, 'a'): [2]}
accepting2=[2]


def nfsmaccepts(current, edges, accepting, visited):
    '''nfsm = MatrixFSMSolver(edges,accepting)
    def trying(current, edges, accepting, visited):
        # edges = dict(nfsm.transform_to_matrices(edges))
        r = ''
        if not isinstance(current, matrix):
            current = matrix([x == current for x in range(1, nfsm.nfsm_length + 1)])
        if (current & accepting).any():
            return r
        for l, mat in edges.items():
            # print 'lll', current * mat
            if (current * mat).any() and l not in visited:
                s = trying(current * mat, edges, accepting, visited + [l])
                r = l + s if s != None else None
        return r
    result = trying(current, nfsm.transform_matrix_collection, nfsm.accepting, visited)
    # nfsm = MatrixFSMSolver(edges, accepting)
    print result, edges, nfsm.accepting, current
    # print nfsm.nfsmsim(result, current, edges, accepting)
    return nfsm.check_string(result, current) and result


    return reduce(lambda x, y: x + l for t, l in edges
                                    for e in edges[t, l])'''

    if current in accepting:
        visited.append(current)
        return ''
    elif current not in visited:
        visited.append(current)
        for edge, string in edges:
            if edge == current:
                for e in edges[(edge, string)]:
                    r=nfsmaccepts(e, edges, accepting, visited)
                    if isinstance(r, str):
                        return string+r


print nfsmaccepts(1, edges, accepting, [])
print "Test 1: "+str(nfsmaccepts(1, edges, accepting, []) == "abc")
print "Test 2: "+str(nfsmaccepts(1, edges, [4], []) == "ab")
print "Test 3: "+str(nfsmaccepts(1, edges2, accepting2, []) == None)
print "Test 4: "+str(nfsmaccepts(1, edges2, [1], []) == "")