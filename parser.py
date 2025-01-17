import ply.yacc as yacc
from lexer import tokens

errors = []

# Seções de Classes
def p_classes(p):
    '''classes : defined_class 
               | defined_class classes
               | primitive_class 
               | primitive_class classes
               | closure_axiom 
               | closure_axiom classes
               '''
    if len(p) == 2:
        p[0] = [p[1]]  # Apenas uma classe
    else:
        p[0] = [p[1]] + p[2]  # Adiciona a nova classe à lista de classes

def p_primitive_class(p):
    '''primitive_class : CLASS CLASS_IDENTIFIER subclass_section disjoint_section individuals_section'''
    p[0] = {
        "type": "primitive_class",
        "name": p[2],
        "subclass_of": p[3],
        "disjoint_classes": p[4],
        "individuals": p[5],
    }

def p_subclass_section(p):
    '''subclass_section : SUBCLASSOF def_descriptions
                        | empty'''
    if len(p) == 3:
        p[0] = p[2]  
    else:
        p[0] = []  

def p_disjoint_section(p):
    '''disjoint_section : DISJOINTCLASSES disjoint_classes_list
                        | empty'''
    if len(p) == 3:
        p[0] = p[2] 
    else:
        p[0] = []  

def p_disjoint_classes_list(p):
    '''disjoint_classes_list : CLASS_IDENTIFIER
                             | CLASS_IDENTIFIER COMMA disjoint_classes_list'''
    if len(p) == 2:
        p[0] = [p[1]] 
    else:
        p[0] = [p[1]] + p[3] 


def p_defined_class(p):
    '''defined_class : CLASS CLASS_IDENTIFIER EQUIVALENTTO CLASS_IDENTIFIER AND def_descriptions individuals_section
                       | CLASS CLASS_IDENTIFIER EQUIVALENTTO CLASS_IDENTIFIER AND def_descriptions'''

    if len(p) == 8:
        p[0] = ('defined_class', p[2], p[4], p[6]) 
    else:
        p[0] = ('defined_class', p[2], p[4])


def p_closure_axiom(p):
    '''closure_axiom : PROPERTY_IDENTIFIER ONLY OPEN_PAREN def_descriptions CLOSE_PAREN'''
    p[0] = ('closure_axiom', p[1], p[4])  


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
                        | OPEN_PAREN def_descriptions CLOSE_PAREN
                        | PROPERTY_IDENTIFIER SOME CLASS_IDENTIFIER COMMA def_descriptions
                        | PROPERTY_IDENTIFIER SOME CLASS_IDENTIFIER COMMA PROPERTY_IDENTIFIER SOME CLASS_IDENTIFIER
                        | PROPERTY_IDENTIFIER ONLY OPEN_PAREN def_descriptions CLOSE_PAREN'''  

    if len(p) == 2:  
        p[0] = ('description', p[1])
    elif len(p) == 3:
        p[0] = ('namespace_type_description', p[1], p[2])
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
    elif len(p) == 4 and p[2] == ',':  
        p[0] = ('logical_op', p[1], 'AND', p[3]) 
    elif len(p) == 5 and p[2] == 'ONLY': 
        p[0] = ('closure_axiom', p[1], p[3])

# Comparação
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

# Tipo de Namespace
def p_namespace_type(p):
    '''namespace_type : NAMESPACE TYPE'''
    p[0] = ('namespace_type', p[1], p[2]) 

# Seção de Indivíduos
def p_individuals_section(p):
    '''individuals_section : INDIVIDUALS individuals
                           | empty'''
    if len(p) == 3:
        p[0] = p[2]  # Lista de indivíduos
    else:
        p[0] = []  # Seção vazia

def p_individuals(p):
    '''individuals : INDIVIDUAL_NAME
                   | INDIVIDUAL_NAME COMMA individuals'''
    if len(p) == 2:
        p[0] = [p[1]]  # Apenas um indivíduo
    else:
        p[0] = [p[1]] + p[3]  # Adiciona o indivíduo à lista

# Função para lidar com seções vazias
def p_empty(p):
    'empty :'
    pass

# Tratamento de erros
def p_error(p):
    if p:
        error_message = f"Erro Sintático: Linha {p.lineno}: Token inesperado '{p.value}'"
        errors.append(error_message)
    else:
        errors.append("Erro Sintático: Fim inesperado do arquivo")

def parse_input(input_string, lexer):
    global errors
    errors = []  # Limpa erros anteriores
    lexer.lineno = 1
    lexer.input(input_string)
    parser = yacc.yacc()
    
    # O resultado processado é retornado
    result = parser.parse(input_string, lexer=lexer)
    
    return result, errors  # Agora retornamos também o resultado
