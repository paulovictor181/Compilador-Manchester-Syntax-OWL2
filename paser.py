import ply.yacc as yacc
from lexer import tokens 

def p_classe_definida(p):
    '''classe : CLASS CLASS_IDENTIFIER EQUIVALENTTO def_descriptions'''
    if len(p) == 8:
        p[0] = ('classe_definida', p[2], p[4], p[6])  # Classe com indivíduos
    else:
        p[0] = ('classe_definida', p[2], p[4])  # Classe sem indivíduos

# Produção para descrições equivalentes (def_descriptions)
def p_def_descriptions(p):
    '''def_descriptions : CLASS_IDENTIFIER
                        | CLASS_IDENTIFIER AND def_descriptions
                        | CLASS_IDENTIFIER OR def_descriptions
                        | PROPERTY_IDENTIFIER SOME CLASS_IDENTIFIER
                        | PROPERTY_IDENTIFIER ALL CLASS_IDENTIFIER
                        | PROPERTY_IDENTIFIER VALUE CLASS_IDENTIFIER
                        | PROPERTY_IDENTIFIER MIN CARDINALITY CLASS_IDENTIFIER
                        | PROPERTY_IDENTIFIER MAX CARDINALITY CLASS_IDENTIFIER
                        | PROPERTY_IDENTIFIER EXACTLY CARDINALITY CLASS_IDENTIFIER
                        | OPEN_PAREN def_descriptions CLOSE_PAREN'''
    if len(p) == 2:
        p[0] = ('description', p[1])
    elif len(p) == 4 and p[2] in ('AND', 'OR'):
        p[0] = ('logical_op', p[1], p[2], p[3])
    elif len(p) == 4:
        p[0] = ('quantifier', p[1], p[2], p[3])
    elif len(p) == 5:
        p[0] = ('cardinality', p[1], p[2], p[3], p[4])
    elif len(p) == 6:
        p[0] = ('cardinality', p[1], p[2], p[3], p[4], p[5])
    elif len(p) == 4 and p[1] == '(':
        p[0] = p[2]


def p_individuals_section(p):
    '''individuals_section : INDIVIDUALS INDIVIDUAL_NAME COMMA
                           | INDIVIDUALS INDIVIDUAL_NAME AND
                           | empty '''
    if len(p) == 4:
        p[0] = p[3]  # Lista de indivíduos
    else:
        p[0] = []  # Sem indivíduos

def p_error(p):
    error_message = f"Erro de sintaxe no token {p.value} na linha {p.lineno}"
    print(error_message)
    errors.append(error_message)


# Construir o parser
parser = yacc.yacc()

# No parser.py
def parse_input(input_string):
    global errors  # Usando uma variável global para armazenar erros
    errors = []  # Limpa erros anteriores
    parser.parse(input_string)
    return errors