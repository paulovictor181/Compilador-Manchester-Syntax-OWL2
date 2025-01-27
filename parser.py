import ply.yacc as yacc
from lexer import tokens

errors = []

# Seções de Classes
def p_classes(p):
    '''classes : defined_class 
               | defined_class classes
               | primitive_class 
               | primitive_class classes
               '''
    if len(p) == 2:
        p[0] = [p[1]]  # Apenas uma classe
    else:
        p[0] = [p[1]] + p[2]  # Adiciona a nova classe à lista de classes

def p_primitive_class(p):
    '''primitive_class : CLASS CLASS_IDENTIFIER subclass_section closure_axiom disjoint_section individuals_section'''
    p[0] = {
        "type": "primitive_class",
        "name": p[2],
        "subclass_of": p[3],
        "disjoint_classes": p[4],
        "individuals": p[5],
    }

def p_subclass_section(p):
    '''subclass_section : SUBCLASSOF def_descriptions
                        | SUBCLASSOF enum_class
                        | SUBCLASSOF covered_class
                        | SUBCLASSOF CLASS_IDENTIFIER 
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
    '''defined_class : CLASS CLASS_IDENTIFIER equivalentto_section subclass_section individuals_section
                       | CLASS CLASS_IDENTIFIER equivalentto_section'''

    if len(p) == 6:
        p[0] = {
            "type": "defined_class",
            "name": p[2],
            "equivalent_to": p[3],
            "subclass_of": p[4],
            "individuals": p[5],
        }
    elif len(p) == 4:
        p[0] = {
            "type": "defined_class",
            "name": p[2],
            "equivalent_to": p[3],
            "subclass_of": None,
            "individuals": None,
        }
    else:
        p[0] = {
            "type": "defined_class",
            "name": p[2],
            "equivalent_to": p[3],
            "aninhada": p[4],
            "subclass_of": None,
            "individuals": None,
        }

def p_enum_class(p):
    '''enum_class : OPEN_CURLY individuals CLOSE_CURLY'''
    if len(p) == 4:
        p[0] = {
            "type": "enum_class",
            "status": "Preenchida",
            "individuals": p[2],
        }
    else:
        p[0] = {
            "type": "enum_class",
            "status": "Vazia",
        }

def p_covered_class(p):
    '''covered_class : CLASS_IDENTIFIER OR covered_class
                     | CLASS_IDENTIFIER
                '''
    if len(p) == 3:
        p[0] = {
            "type": "covered_class",
            "Classes": p[3],
        }
    else:
        p[0] = {
            "type": "covered_class",
            "Classe": p[1],
        }
def p_closure_axiom(p):
    '''closure_axiom : ONLY OPEN_PAREN def_descriptions CLOSE_PAREN'''
    p[0] = ('closure_axiom', p[1], p[3])  


def p_aux_fechamento(p):
    '''aux_fechamento : OPEN_PAREN PROPERTY_IDENTIFIER aux_fechamento
                      | OR PROPERTY_IDENTIFIER aux_fechamento
                      | PROPERTY_IDENTIFIER CLOSE_PAREN'''
    if len(p) == 4 and p[1] == '(':
        p[0] = ('aux_fechamento', p[2], p[3])
    elif len(p) == 4 and p[1] == 'or':
        p[0] = ('aux_fechamento', 'or', p[2], p[3])
    else:
        p[0] = ('aux_fechamento', p[1], p[2])

#
#def p_ani_interno(p):
#    '''ani_fechamento : VALUE CLASS_IDENTIFIER CLOSE_PAREN
#                      | VALUE CLASS_IDENTIFIER CLOSE_PAREN ani_fechamento
#                        '''
#    if len(p) == 4:
#        p[0] = ('ani_fechamento', p[1], p[2])
#    elif len(p) == 5:
#        p[0] = ('ani_fechamento', p[1], p[2], p[4])
#    else:
#        p[0] = ('ani_fechamento', p[1])



def p_ani_abertura(p):
    '''ani_abertura : comma_and OPEN_PAREN def_descriptions CLOSE_PAREN quantifier ani_abertura
                    | comma_and OPEN_PAREN def_descriptions CLOSE_PAREN'''
    if len(p) == 3:
        p[0] = ('ani_abertura', p[2])
    else:
        p[0] = ('ani_abertura', p[2], p[4], p[5] )


def p_aninhada(p):
    '''aninhada : CLASS_IDENTIFIER ani_abertura
           '''
    if len(p) == 6:
        p[0] = ('aninhada', p[1], p[3], p[4], p[5])
    else:
        p[0] = ('aninhada', p[1], p[2], p[3])


def p_equivalentto_section(p):
    '''equivalentto_section : EQUIVALENTTO CLASS_IDENTIFIER comma_and def_descriptions
                            | EQUIVALENTTO enum_class
                            | EQUIVALENTTO covered_class
                            | EQUIVALENTTO aninhada
    '''
    p[0] = p[2]


def p_def_descriptions(p):
    '''def_descriptions : class_aux
                        | class_aux def_descriptions 
                        | quantifier_aux
                        | quantifier_aux def_descriptions
    '''  
    p[0] = p[1]


def p_class_aux(p):
    '''class_aux : CLASS_IDENTIFIER
                 | CLASS_IDENTIFIER OR class_aux
                 | CLASS_IDENTIFIER comma_and class_aux
                 | OPEN_PAREN class_aux CLOSE_PAREN
     '''
    p[0] = {
        'class': p[1]
    }

def p_quantifier_aux(p):
    '''quantifier_aux : PROPERTY_IDENTIFIER quantifier CLASS_IDENTIFIER
                      | PROPERTY_IDENTIFIER quantifier namespace_type
                      | OPEN_PAREN quantifier_aux CLOSE_PAREN
                      | quantifier_aux comma_and quantifier_aux
    '''
    p[0] = {
        'property': p[1],
        'quantifier': p[2],
        'target': p[3]
    }

# Comparação
def p_quantifier(p):
    '''quantifier : SOME
                  | ALL
                  | VALUE
                  | MAX
                  | MIN
                  | EXACTLY
                  | THAT
                  '''    
    p[0] = p[1]

# Comparação
def p_sizecheck(p):
    '''sizecheck : EQUAL CARDINALITY
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
    '''namespace_type : NAMESPACE TYPE
                      | NAMESPACE TYPE OPEN_BRACKET sizecheck CLOSE_BRACKET'''
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

def p_comma_and(p):
        '''comma_and : COMMA
                     | AND'''
        p[0] = [p[1]]

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
