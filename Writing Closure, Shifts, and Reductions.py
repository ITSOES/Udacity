# Writing Closure

# We are currently looking at chart[i] and we see x => ab . cd from j

# Write the Python procedure, closure, that takes five parameters:

# grammar: the grammar using the previously described structure
#   i: a number representing the chart state that we are currently looking at
#   x: a single nonterminal
#   ab and cd: lists of many things

# The closure function should return all the new parsing states that we want to
# add to chart position i

# Hint: This is tricky. If you are stuck, do a list comphrension over the grammar rules.

def closure(grammar, i, x, ab, cd):
    return [(x, [], g[1], i) for g in grammar if g[0] == cd[0]]


grammar = [
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ("t", ["I", "like", "t"]),
    ("t", [""])
]

print(closure(grammar, 0, "exp", ["exp", "+"], ["exp"]) == [('exp', [], ['exp', '+', 'exp'], 0),
                                                            ('exp', [], ['exp', '-', 'exp'], 0),
                                                            ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['num'], 0)])
print(closure(grammar, 0, "exp", [], ["exp", "+", "exp"]) == [('exp', [], ['exp', '+', 'exp'], 0),
                                                              ('exp', [], ['exp', '-', 'exp'], 0),
                                                              ('exp', [], ['(', 'exp', ')'], 0),
                                                              ('exp', [], ['num'], 0)])
print(closure(grammar, 0, "exp", ["exp"], ["+", "exp"]) == [])


# Writing Shift

# We are currently looking at chart[i] and we see x => ab . cd from j. The input is tokens.

# Your procedure, shift, should either return None, at which point there is
# nothing to do or will return a single new parsing state that presumably
# involved shifting over the c if c matches the ith token.

def shift(tokens, i, x, ab, cd, j):
    return (x, ab + [cd[0]], cd[1:], j) if cd and ab + cd == tokens else None


print(shift(["exp", "+", "exp"], 2, "exp", ["exp", "+"], ["exp"], 0) == ('exp', ['exp', '+', 'exp'], [], 0))
print(shift(["exp", "+", "exp"], 0, "exp", [], ["exp", "+", "exp"], 0) == ('exp', ['exp'], ['+', 'exp'], 0))
print(shift(["exp", "+", "exp"], 3, "exp", ["exp", "+", "exp"], [], 0) == None)
print(shift(["exp", "+", "ANDY LOVES COOKIES"], 2, "exp", ["exp", "+"], ["exp"], 0) == None)

print()
print('reductions:')
def reductions(chart, i, x, ab, cd, j):
    return [(jstate[0], jstate[1] + [x], jstate[2][1:], jstate[3])
        for jstate in chart[j] if cd ==[] and jstate[2]!=[] and jstate[2][0] == x]

chart = {
    0: [('exp', ['exp'], ['+', 'exp'], 0),
             ('exp', [], ['num'], 0),
             ('exp', [], ['(', 'exp', ')'], 0),
             ('exp', [], ['exp', '-', 'exp'], 0),
             ('exp', [], ['exp', '+', 'exp'], 0)],

    1: [('exp', ['exp', '+'], ['exp'], 0)],
    2: [('exp', ['exp', '+', 'exp'], [], 0)]
    }

print(reductions(chart, 2, 'exp', ['exp', '+', 'exp'], [], 0) == [
    ('exp', ['exp'], ['-', 'exp'], 0), ('exp', ['exp'], ['+', 'exp'], 0)])
