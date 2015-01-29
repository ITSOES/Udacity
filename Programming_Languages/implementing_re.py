# Implementing RE
# Challenge Problem 
#
# Focus: All Units
#
#
# In this problem you will write a lexer, parser and interpreter for
# strings representing regular expressions. Your program will output 
# a non-deterministic finite state machine that accepts the same language
# as that regular expression. 
#
# For example, on input 
#
# ab*c
#
# Your program might output
# 
# edges = { (1,'a')  : [ 2 ] ,
# (2,None) : [ 3 ] ,    # epsilon transition
#           (2,'b')  : [ 2 ] ,
#           (3,'c')  : [ 4 ] } 
# accepting = [4]
# start = 1
#
# We will consider the following regular expressions:
#
#       single characters       #       a       
#       regexp1 regexp2         #       ab
#       regexp *                #       a*
#       regexp1 | regexp2       #       a|b
#       ( regexp )              #       (a|b)* -- same as (?:a|b) 
#
# That's it. We won't consider [a-c] because it's just a|b|c, and we won't
# consider a+ because it's just aa*. We will not worry about escape
# sequences. Single character can be a-z, A-Z or 0-9 -- that's it. No need
# to worry about strange character encodings. We'll use ( ) for regular
# expression grouping instead of (?: ) just to make the problem simpler.
#
# Don't worry about precedence or associativity. We'll fully parenthesize
# all regular expressions before giving them to you. 
#
# You will write a procedure re_to_nfsm(re_string). It takes as input a
# single argument -- a string representing a regular expression. It returns
# a tuple (edges,accepting,start) corresponding to an NSFM that accepts the
# same language as that regular expression.
#
# Hint: Make a lexer and a paser and an interpreter. Your interpreter may
# find it handy to know the current state and the goal state. Make up as
# many new states as you need. 
# 
import ply.lex as lex
import ply.yacc as yacc

start = 're'
precedence = (
    # ('left', 'BAR'),
    ('left', 'CONCAT'),
    ('left', 'STAR'),
)

# ('concat',
#  ('group',
#   ('concat',
#    ('bar',
#     ('concat', ('string', 'i'), ('group', ('string', 'o'))),
#     ('string', 'h')),
#    ('group', ('string', 'd')))),
#  ('string', 'g'))

def p_re_bar(p):
    're : re BAR re'
    p[0] = ('bar', p[1], p[3])

# def p_re_to_bar(p):
#     're : bar'
#     p[0] = ('bar', p[1])

def p_re_string(p):
    're : STRING %prec CONCAT'
    p[0] = ('string', p[1])


def p_re_concat(p):
    're : re re %prec CONCAT'
    p[0] = ('concat', p[1], p[2])


def p_exp_star(p):
    're : re STAR'
    p[0] = ('star', p[1])


def p_exp_group(p):
    're : LPAREN re RPAREN'
    p[0] = ('group', p[2])


def p_exp_bracket(p):
    're : LBRACKET re RBRACKET'
    p[0] = ('bracket', p[2])


# def p_exp_count(p):
#     'count : STAR'
#     p[0] = p[1]

def p_error(p):
    print p
    raise SyntaxError


def t_error(t):
    print "Lexer: unexpected character " + t.value[0]
    t.lexer.skip(1)


tokens = ('STRING', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'BAR', 'STAR')

t_STRING = r"[0-9A-Za-z]+"
t_ignore = ' \t\v\r'
t_STAR = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_BAR = r'\|'

lexer = lex.lex()
parser = yacc.yacc()
f = 1
last_state = None
from collections import defaultdict
from pprint import pprint
from time import sleep

def next_match(tree):
    if tree[0] != 'string':
        return next_match(tree[1])
    return tree[1]

def interpret(tree):

    print 'interpret called'
    pprint (tree)
    global f
    states = defaultdict(list)

    f = 1

    def _interpret(tree, prev=None):
        global f
        p, next = tree[:2]
        if p == 'concat':
            _interpret(next, prev)
            next = tree[2]
            _interpret(next, prev)
        elif p == 'star':
            g = f
            prev = _interpret(next)
            prev = (g+1, prev)
            # if f not in states[prev]:
            #     print 'sdsjk', prev, f
            #     states[prev].append(f)
            states[f, None].append(g)
            states[g, None].append(f)
            return prev


        elif p == 'string':
            for l in next_match(tree):
                states[(f, l)].append(f + 1)
                f += 1  # Only place f increments
                next = tree
        elif p == 'group':
            return _interpret(tree[1])[-1]
        elif p == 'bar':
            f1 = f
            lst1 = _interpret(next)  # changes f
            f -= 1
            f2 = f
            _interpret(tree[2])  # changes f
            mtch2 = next_match(tree[2])[0]
            states[f1, mtch2].append(states[f2, mtch2].pop())
            print f2, lst1, f, f1
            # pprint(dict(states))
            sleep(.1)
            states[f2, lst1][-1] = f

        # print next_match(tree)
        # Each recursive call returns the last letter that was mapped
        return next_match(next)[-1]

    _interpret(tree)
    states = {x: y for x, y in states.items() if y}
    pprint(states)
    def optimize(states=states):
        fix, kill = {}, set()
        states = {x: y for x, y in states.items() if y}
        for state in states:
            if not state[1] and state[0] != 1:
                kill.add(state)
                for some, dest in states.items():
                    if state[0] in dest:
                        dest.extend(x for x in states[state] if x not in dest)
        for kill in kill:
            del states[kill]
        return states
    states = optimize()
    print 'f == ', f
    # pprint(dict(states))
    print
    return states, [f], 1

# {(1, 'a'): [2, 3], (2, 'b'): [3], (3, 'c'): [4]}
def re_to_nfsm(re_string):
    # Feel free to overwrite this with your own code.
    print 're_string: ', re_string
    lexer.input(re_string)
    parse_tree = parser.parse(re_string, lexer=lexer)
    return interpret(parse_tree)


# We have included some testing code ... but you really owe it to yourself
# to do some more testing here.

def nfsmaccepts(edges, accepting, current, string, visited):
    # If we have visited this state before, return false.
    if (current, string) in visited:
        return False
    visited.append((current, string))

    # Check all outgoing epsilon transitions (letter == None) from this
    # state.
    if (current, None) in edges:
        for dest in edges[(current, None)]:
            # print dest
            if nfsmaccepts(edges, accepting, dest, string, visited):
                return True

    # If we are out of input characters, check if this is an
    # accepting state.
    if string == "":
        return current in accepting

    # If we are not out of input characters, try all possible
    # outgoing transitions labeled with the next character.
    letter = string[0]
    rest = string[1:]
    if (current, letter) in edges:
        for dest in edges[(current, letter)]:
            if nfsmaccepts(edges, accepting, dest, rest, visited):
                return True
    return False


def test(re_string, e, ac_s, st_s, strings):
    # kk = re_to_nfsm(re_string)
    # print 'GRGGGG', kk, 'fyfuyi', re_string, 'len', len(kk)
    my_e, my_ac_s, my_st_s = re_to_nfsm(re_string)
    pprint(( 'my_e', my_e, my_ac_s, my_st_s))
    for string in strings:
        if not nfsmaccepts(e, ac_s, st_s, string, []) == \
              nfsmaccepts(my_e, my_ac_s, my_st_s, string, []):
            print
            print re_string
            print False, string, 'Should match?', nfsmaccepts(e, ac_s, st_s, string, [])
            print
    print 'END'
    print

edges = {(1, 'a') : [2],
         (2, None): [3],  # epsilon transition
         (2, 'b') : [2],
         (3, 'c') : [4]}
accepting_state = [4]
start_state = 1

test("a(b*)c", edges, accepting_state, start_state,
  [ "", "ab", "cd", "cddd", "c", "", "ad", "abcd", "abbbbbc", "ac" ]  )

edges = {(1, 'a'): [2],
         (2, 'b'): [1],
         (1, 'c'): [3],
         (3, 'd'): [1]}
accepting_state = [1]
start_state = 1

test("((ab)|(cd))*", edges, accepting_state, start_state,
  [ "", "ab", "cd", "cddd", "c", "", "ad", "abcd", "abbbbbc", "ac" ]  )


def test(input_string):
    lexer.input(input_string)
    parser = yacc.yacc()
    print input_string
    # try:
    # print 'input_string', input_string
    parse_tree = parser.parse(input_string, lexer=lexer)
    print parse_tree
    return interpret(parse_tree)
    # except:
    #   parse_tree = parser.parse(input_string, lexer=lexer)
    #   return "error"
print
print
pprint( test('(y(io)|(hd))*'))