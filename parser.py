import ply.yacc as yacc
from lexer import tokens 

def p_classes(p):
    '''classes : classe_definida 
               | classe_definida classes'''
    if len(p) == 2:
        p[0] = [p[1]]  # Apenas uma classe
    else:
        p[0] = [p[1]] + p[2]  # Adiciona a nova classe à lista de classes


def p_classe_definida(p):
    '''classe_definida : CLASS CLASS_IDENTIFIER EQUIVALENTTO CLASS_IDENTIFIER AND def_descriptions individuals_section
                       | CLASS CLASS_IDENTIFIER EQUIVALENTTO CLASS_IDENTIFIER AND def_descriptions'''

    if len(p) == 8:
        p[0] = ('classe_definida', p[2], p[4], p[6])  # Classe com indivíduos
    else:
        p[0] = ('classe_definida', p[2], p[4])  # Classe sem indivíduos

def p_def_descriptions(p):
    '''def_descriptions : CLASS_IDENTIFIER
                        | namespace_type
                        | CLASS_IDENTIFIER AND def_descriptions
                        | CLASS_IDENTIFIER OR def_descriptions
                        | PROPERTY_IDENTIFIER SOME CLASS_IDENTIFIER
                        | PROPERTY_IDENTIFIER SOME namespace_type
                        | PROPERTY_IDENTIFIER SOME namespace_type OPEN_BRACKET comparison CLOSE_BRACKET
                        | PROPERTY_IDENTIFIER ALL CLASS_IDENTIFIER
                        | PROPERTY_IDENTIFIER ALL namespace_type
                        | PROPERTY_IDENTIFIER VALUE CLASS_IDENTIFIER
                        | PROPERTY_IDENTIFIER VALUE namespace_type
                        | PROPERTY_IDENTIFIER MIN CARDINALITY CLASS_IDENTIFIER
                        | PROPERTY_IDENTIFIER MIN CARDINALITY namespace_type
                        | PROPERTY_IDENTIFIER MAX CARDINALITY CLASS_IDENTIFIER
                        | PROPERTY_IDENTIFIER MAX CARDINALITY namespace_type
                        | PROPERTY_IDENTIFIER EXACTLY CARDINALITY CLASS_IDENTIFIER
                        | PROPERTY_IDENTIFIER EXACTLY CARDINALITY namespace_type
                        | OPEN_PAREN def_descriptions CLOSE_PAREN'''
    if len(p) == 2:  # Exemplo: CLASS_IDENTIFIER
        p[0] = ('description', p[1])
    elif len(p) == 3:  # Exemplo: namespace_type (NAMESPACE TYPE)
        p[0] = ('namespace_type_description', p[1], p[2])
    elif len(p) == 4 and p[2] in ('AND', 'OR'):  # Exemplo: CLASS_IDENTIFIER AND def_descriptions
        p[0] = ('logical_op', p[1], p[2], p[3])
    elif len(p) == 4:  # Exemplo: PROPERTY_IDENTIFIER SOME CLASS_IDENTIFIER
        p[0] = ('quantifier', p[1], p[2], p[3])
    elif len(p) == 5:  # Exemplo: PROPERTY_IDENTIFIER MIN CARDINALITY CLASS_IDENTIFIER
        p[0] = ('cardinality', p[1], p[2], p[3], p[4])
    elif len(p) == 6:  # Exemplo: PROPERTY_IDENTIFIER EXACTLY CARDINALITY namespace_type
        p[0] = ('cardinality', p[1], p[2], p[3], p[4], p[5])
    elif len(p) == 4 and p[1] == '(':  # Exemplo: (def_descriptions)
        p[0] = p[2]

# Adicionando uma produção para lidar com a comparação no contexto de restrição de propriedades
def p_comparison(p):
    '''comparison : EQUAL CARDINALITY
                  | GREATER_THAN CARDINALITY
                  | LESS_THAN CARDINALITY
                  | GREATER_THAN EQUAL CARDINALITY
                  | LESS_THAN EQUAL CARDINALITY'''
    if p[1] == '=':
        p[0] = ('equal', p[2])
    elif p[1] == '>':
        p[0] = ('greater_than', p[2])
    elif p[1] == '<':
        p[0] = ('less_than', p[2])
    elif p[1] == '>=':
        p[0] = ('greater_equal', p[2])
    elif p[1] == '<=':
        p[0] = ('less_equal', p[2])


def p_namespace_type(p):
    '''namespace_type : NAMESPACE TYPE'''
    p[0] = ('namespace_type', p[1], p[2])  # Associa o NAMESPACE com o TYPE


def p_individuals_section(p):
    '''individuals_section : INDIVIDUALS individuals
                           | empty'''
    if len(p) == 3:
        p[0] = p[2]  # Lista de indivíduos
    else:
        p[0] = []  # Seção vazia


def p_individuals(p):
    '''individuals : INDIVIDUAL_NAME
                   | INDIVIDUAL_NAME COMMA individuals
                   '''
    if len(p) == 2:
        p[0] = [p[1]]  # Apenas um indivíduo
    else:
        p[0] = [p[1]] + p[3]  # Adiciona o indivíduo atual à lista


def p_empty(p):
    'empty :'
    pass

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