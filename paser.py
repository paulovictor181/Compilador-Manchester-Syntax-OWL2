import ply.yacc as yacc
from lexer import tokens  # Supondo que os tokens já estejam definidos no lexer.py

# Lista de produções
def p_classe_primitiva(p):
    '''classe : CLASS_IDENTIFIER 'SubClassOf:' subclasse_list 'DisjointClasses:' disjoint_list 'Individuals:' individual_list'''
    p[0] = ('classe_primitiva', p[1], p[3], p[5], p[7])

def p_subclasse_list(p):
    '''subclasse_list : propriedade_expression
                      | subclasse_list ',' propriedade_expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_propriedade_expression(p):
    '''propriedade_expression : PROPERTY_IDENTIFIER 'some' CLASS_IDENTIFIER'''
    p[0] = ('propriedade_expression', p[1], p[3])

def p_disjoint_list(p):
    '''disjoint_list : CLASS_IDENTIFIER
                     | disjoint_list ',' CLASS_IDENTIFIER'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_individual_list(p):
    '''individual_list : INDIVIDUAL_NAME
                       | individual_list ',' INDIVIDUAL_NAME'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

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