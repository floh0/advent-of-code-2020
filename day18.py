from ply import yacc
from ply import lex

with open("day18.txt", "r") as f:
	i = f.readlines()

t_PLUS = r"\+"
t_TIMES = r"\*"
t_LEFTP = r"\("
t_RIGHTP = r"\)"

def t_NUM(t):
     r"\d+"
     t.value = int(t.value)    
     return t
     
t_ignore = " \n"

tokens = ["PLUS","TIMES","LEFTP","RIGHTP","NUM"]


def p_value(p):
	'''
	value : sum
	      | product
	      | NUM
	'''
	p[0] = p[1]

def p_parerthesis(p):
	'value : LEFTP value RIGHTP'
	p[0] = p[2]

def p_sum(p):
	'sum : value PLUS value'
	p[0] = p[1]+p[3]

def p_product(p):
	'product : value TIMES value'
	p[0] = p[1]*p[3]

lex.lex()

precedence = (
     ('left', 'PLUS', 'TIMES'),
)
yacc.yacc()

part1 = sum([yacc.parse(e) for e in i])	
print(part1)

precedence = (
     ('left', 'TIMES'),
     ('left', 'PLUS'),
)
yacc.yacc()

part2 = sum([yacc.parse(e) for e in i])	
print(part2)