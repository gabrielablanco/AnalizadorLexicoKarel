import ply.lex as lex

tokens = ['START_PROGRAM', 'END_PROGRAM', 'START_EXECUTION', 'END_EXECUTION', 'TURNOFF', 'MOVE', 'TURNLEFT', 'PICKBEEPER', 'PUTBEEPER', '2POINTS']

t_2POINTS = r'\;'
t_START_PROGRAM = r'iniciar-programa'
t_END_PROGRAM = r'finalizar-programa'
t_START_EXECUTION = r'inicia-ejecucion'
t_END_EXECUTION = r'termina-ejecucion'
t_TURNOFF = r'apagate'
t_MOVE = r'avanza'
t_TURNLEFT = r'gira-izquierda'
t_PICKBEEPER = r'coge-zumbador'
t_PUTBEEPER = r'deja-zumbador'

def t_error(t):
    print("Caracter invalido '%s'" % t.value[0])
    t.lexer.skip(1)

def abrir_archivo(nombre):
    archivo = open(nombre, 'r')
    return archivo.read()

lex.lex()

lex.input(abrir_archivo("archivo.txt"))
while True:
    tok = lex.token()
    if not tok: break
    print (str(tok.value) + " - " + str(tok.type))