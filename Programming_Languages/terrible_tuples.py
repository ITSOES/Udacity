# Terrible Tuples
#
# Focus: Units 3 and 4, Grammars and Parsing
#
# In this problem you will use context-free grammars to specify some
# expression for part of a new programming language. We will specify tuples
# and lists, as in Python. We will consider four types of expressions.
#
# 1. An expression can be a single NUMBER token. In this case, your parser
# should return ("number",XYZ) where XYZ is the value of the NUMBER
# token.
#
# 2. An expression can be LPAREN expression RPAREN . In this case, your
# parser should return the value of the expression inside the parentheses.
#
# 3. An expression can be LPAREN "a list of more than one comma-separated
# expressions" RPAREN. This should remind you of tuples in Python:
#
#               (1,2,3) 
#
# The inner expressions are 1 2 and 3, and they are separated by commas.
# In this case, your parser should return ("tuple", ...) where ... is a
# list of the child expression values. For example, for (1,2) you should
# return ("tuple",[("number",2),("number",3)]). 
#
# 4. An expression can be LBRACKET "a list of one or more comma-separated
# expressions" RBRACKET. This should remind you of lists in Python:
#
#               [7,8,9] 
#
# These parse exactly like tuples, except that they use square brackets
# instead of parentheses, and singleton lists like [7] are valid. Your
# parser should return ("list", ...) as above, so [7,8] would return
# ("list",[("number",7),("number",8)]). 
#
# Complete the parser below.  

import ply.lex as lex
import ply.yacc as yacc

start = 'exp'    # the start symbol in our grammar

#####
#

# Place your grammar definition rules here.


#
#####

def p_error(p):
        raise SyntaxError


# We have provided a lexer for you. You should not change it.

tokens = ('LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'NUMBER', 'COMMA')

def t_NUMBER(token):
        r"[0-9]+"
        token.value = int(token.value)
        return token

t_ignore        = ' \t\v\r'
t_COMMA         = r'\,'
t_LPAREN        = r'\('
t_RPAREN        = r'\)'
t_LBRACKET      = r'\['
t_RBRACKET      = r'\]'

def t_error(t):
  print "Lexer: unexpected character " + t.value[0]
  t.lexer.skip(1)

def p_exp(p):
    'exp : NUMBER'
    # print 'p', p[1]
    p[0] = ("number", p[1])

def p_exp_tuple(p):
    'exp : LPAREN expcomma RPAREN'
    # p[0] = ("tuple", p[1])
    # print 'p[2]', list(p), len(p)
    if len(p[2]) == 1:
        print 'ITY WRH'#, len(p[2])
        p[0] = p[2][0]
    else:
        p[0] = ('tuple', p[2])
        print list(p)

def p_expcomma(p):
    'expcomma : expcomma COMMA exp'
    # print 'fdgsdfgsdfgsdfgsd', list(p)
    p[0] = p[1] + [p[3]]

def p_expcomma_none(p):
    'expcomma : exp'
    p[0] = [p[1]]

def p_exp_list(p):
    'exp : LBRACKET expcomma RBRACKET'
    p[0] = ("list", p[2])
# We have included some testing code to help you check your work. Since
# this is the final exam, you will definitely want to add your own tests.
lexer = lex.lex() 

def test(input_string):
  lexer.input(input_string)
  parser = yacc.yacc()
  try:
    # print 'input_string', input_string
    parse_tree = parser.parse(input_string, lexer=lexer) 
    return parse_tree 
  except:
    # parse_tree = parser.parse(input_string, lexer=lexer)
    return "error" 

# question1 = " 123 "
# answer1 = ('number', 123)
# ans1 = test(question1)
# print ans1 == answer1
# print test(question1)
#
# question2 = " (123) "
# print
# print 'Question 2!'
# ans2 = test(question2)
# print ans1 == answer1
# print question2
# print test(question2)
# print


print 'Question 3!'
question3 = " ( 1, 2, 3 ) "
answer3 = ('tuple', [('number', 1), ('number', 2), ('number', 3)])
ans3 = test(question3)
print ans3 == answer3
print 'q is', question3
print 'should be', answer3
print 'what?', ans3
print

question4 = " [123] " 
answer4 = ('list', [('number', 123)])
print test(question4) == answer4

question5 = " [1,2,3] " 
answer5 = ('list', [('number', 1), ('number', 2), ('number', 3)])
print test(question5) == answer5

question6 = " [(1,2),[3,[4]]] "
answer6 = ('list', [('tuple', [('number', 1), ('number', 2)]), ('list', [('number', 3), ('list', [('number', 4)])])])
print test(question6) == answer6 

question7 = " (1,2) [3,4) " 
answer7 = "error"
print test(question7) == answer7


