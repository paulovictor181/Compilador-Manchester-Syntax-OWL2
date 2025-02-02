import ply.yacc as yacc
from lexer import tokens

errors = []

aberturas = []
fechamentos = []

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
    '''primitive_class : CLASS CLASS_IDENTIFIER subclass_section disjoint_section individuals_section'''
    p[0] = {
        "type": "primitive_class",
        "name": p[2],
        "subclass_of": p[3],
        "disjoint_classes": p[4],
        "individuals": p[5],
    }

def p_subclass_section(p):
    '''subclass_section : SUBCLASSOF enum_class
                        | SUBCLASSOF CLASS_IDENTIFIER OR covered_class
                        | SUBCLASSOF CLASS_IDENTIFIER def_descriptions_axioma ONLY auxiliar_fechamento
                        | SUBCLASSOF CLASS_IDENTIFIER def_descriptions_axioma ONLY OPEN_PAREN auxiliar_fechamento CLOSE_PAREN
                        | SUBCLASSOF CLASS_IDENTIFIER 
                        | SUBCLASSOF quantifier_aux_axioma
                        '''
    if len(p) == 2:
        p[0] = p[2]  
    elif len(p) == 5:
        p[0] = p[4]


    global aberturas 
    global fechamentos


    if len(p) == 8:
        for t in aberturas[:]:
            if t in fechamentos:
                fechamentos.remove(t)
                aberturas.remove(t)

        if (len(fechamentos) == 0) and (len(aberturas) == 0):
            p[0] = 'Axioma'
        else:
            p_erro_fechamento('Erro CLASS_IDENTIFIER usadas no fechamento destoa da abertura')

    print('aberturas',aberturas,'fechados',fechamentos)


def p_erro_fechamento(p):
    print('Erro: ', p)


def p_auxiliar_fechamento(p):
    '''auxiliar_fechamento : CLASS_IDENTIFIER   
                        | CLASS_IDENTIFIER OR auxiliar_fechamento
    '''

    global fechamentos

    fechamentos.append(p[1])

def p_disjoint_section(p):
    '''disjoint_section : DISJOINTCLASSES quantifier_aux
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

    if len(p) == 5:
        p[0] = {
            "type": "defined_class\n",
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
    print('covered')

def p_equivalentto_section(p):
    '''equivalentto_section : EQUIVALENTTO enum_class
                            | EQUIVALENTTO CLASS_IDENTIFIER OR covered_class
                            | EQUIVALENTTO CLASS_IDENTIFIER only_defined
                            | EQUIVALENTTO CLASS_IDENTIFIER aninhada 
    '''
    print(len(p))
    if len(p) == 5:
        p[0] =  p[4]
    elif len(p) == 4: 
        p[0] = p[3]
        print(p[1],p[2],p[3])
    elif len(p) == 2: 
        p[0] = p[2]
    else: 
        p[0] = p[2]
    

def p_def_descriptions(p):
    '''def_descriptions : quantifier_aux            
    '''  
    p[0] = p[1]

def p_def_descriptions_axioma(p):
    '''def_descriptions_axioma : quantifier_aux_axioma            
    '''  
    print('axioma')
    p[0] = p[1]

def p_aninhada(p):
    '''aninhada : comma_and OPEN_PAREN OPEN_PAREN quantifier_aux_aninhada CLOSE_PAREN 
                | comma_and OPEN_PAREN PROPERTY_IDENTIFIER quantifier OPEN_PAREN quantifier_aux_aninhada_extra CLOSE_PAREN CLOSE_PAREN              
    '''
    print('aninhada')
    p[0] = 'aninhada'

def p_only_defined(p):
    '''only_defined : comma_and quantifier_aux           
    '''  
    print('only_definida')

def p_quantifier_aux_aninhada(p):
    '''quantifier_aux_aninhada  : comma_and quantifier_aux_aninhada
                                | PROPERTY_IDENTIFIER quantifier CLASS_IDENTIFIER quantifier_aux_aninhada
                                | PROPERTY_IDENTIFIER quantifier namespace_type
                                | PROPERTY_IDENTIFIER quantifier_number CARDINALITY namespace_type
                                | PROPERTY_IDENTIFIER quantifier_number CARDINALITY CLASS_IDENTIFIER
                                | quantifier_aux_aninhada comma_and quantifier_aux_aninhada
                                | CLASS_IDENTIFIER quantifier quantifier_aux_aninhada
                                | CLASS_IDENTIFIER OR quantifier_aux_aninhada
                                | PROPERTY_IDENTIFIER quantifier quantifier_aux_aninhada
                                | CLASS_IDENTIFIER comma_and quantifier_aux_aninhada
                                | OPEN_PAREN quantifier_aux_aninhada CLOSE_PAREN
                                | CLOSE_PAREN quantifier_aux_aninhada
                                | CLASS_IDENTIFIER
                                | PROPERTY_IDENTIFIER
    '''
 
    if len(p) == 5:
        p[0] = p[3]

    global aberturas

    if len(p) == 4 and p.slice[1].type == 'CLASS_IDENTIFIER':
        aberturas.append(p[1])

def p_quantifier_aux_aninhada_extra(p):
    '''quantifier_aux_aninhada_extra  : comma_and quantifier_aux_aninhada_extra
                                | PROPERTY_IDENTIFIER quantifier CLASS_IDENTIFIER quantifier_aux_aninhada_extra
                                | PROPERTY_IDENTIFIER quantifier namespace_type
                                | PROPERTY_IDENTIFIER quantifier_number CARDINALITY namespace_type
                                | PROPERTY_IDENTIFIER quantifier_number CARDINALITY CLASS_IDENTIFIER
                                | quantifier_aux_aninhada_extra comma_and quantifier_aux_aninhada_extra
                                | CLASS_IDENTIFIER quantifier quantifier_aux_aninhada_extra
                                | CLASS_IDENTIFIER OR quantifier_aux_aninhada_extra
                                | PROPERTY_IDENTIFIER quantifier quantifier_aux_aninhada_extra
                                | CLASS_IDENTIFIER comma_and quantifier_aux_aninhada_extra
                                | OPEN_PAREN quantifier_aux_aninhada_extra CLOSE_PAREN
                                | CLASS_IDENTIFIER
                                | PROPERTY_IDENTIFIER
    '''
 
    if len(p) == 5:
        p[0] = p[3]

    global aberturas

    if len(p) == 4 and p.slice[1].type == 'CLASS_IDENTIFIER':
        aberturas.append(p[1])

def p_quantifier_aux(p):
    '''quantifier_aux : comma_and quantifier_aux
                      | PROPERTY_IDENTIFIER quantifier CLASS_IDENTIFIER
                      | PROPERTY_IDENTIFIER quantifier CLASS_IDENTIFIER quantifier_aux
                      | PROPERTY_IDENTIFIER quantifier namespace_type
                      | PROPERTY_IDENTIFIER quantifier_number CARDINALITY namespace_type
                      | PROPERTY_IDENTIFIER quantifier_number CARDINALITY CLASS_IDENTIFIER
                      | quantifier_aux comma_and quantifier_aux
                      | CLASS_IDENTIFIER quantifier quantifier_aux
                      | CLASS_IDENTIFIER OR quantifier_aux
                      | PROPERTY_IDENTIFIER quantifier quantifier_aux
                      | CLASS_IDENTIFIER comma_and quantifier_aux
                      | OPEN_PAREN quantifier_aux CLOSE_PAREN
                      | CLASS_IDENTIFIER
                      | PROPERTY_IDENTIFIER
    '''
 
    if len(p) == 5:
        p[0] = p[3]

    global aberturas

    if len(p) == 4 and p.slice[1].type == 'CLASS_IDENTIFIER':
        aberturas.append(p[1])



def p_quantifier_aux_axioma(p):
    '''quantifier_aux_axioma : comma_and quantifier_aux_axioma
                            | OPEN_PAREN quantifier_aux_axioma CLOSE_PAREN
                            | PROPERTY_IDENTIFIER quantifier_number CARDINALITY namespace_type
                            | PROPERTY_IDENTIFIER quantifier_number CARDINALITY CLASS_IDENTIFIER
                            | PROPERTY_IDENTIFIER quantifier_geral CLASS_IDENTIFIER
                            | PROPERTY_IDENTIFIER quantifier_geral namespace_type                 
                            | quantifier_aux_axioma comma_and quantifier_aux_axioma
                            | CLASS_IDENTIFIER quantifier_geral quantifier_aux_axioma
                            | CLASS_IDENTIFIER OR quantifier_aux_axioma
                            | PROPERTY_IDENTIFIER quantifier_geral quantifier_aux_axioma
                            | CLASS_IDENTIFIER comma_and quantifier_aux_axioma
                            | CLASS_IDENTIFIER
                            | PROPERTY_IDENTIFIER
    '''
 
    if len(p) == 5:
        p[0] = p[3]

    global aberturas

    if len(p) == 4 and p.slice[1].type == 'CLASS_IDENTIFIER':
        aberturas.append(p[1])

   
    print(len(p))


# Comparação
def p_quantifier(p):
    '''quantifier : SOME
                  | ALL
                  | VALUE
                  | THAT
                  '''    
    p[0] = p[1]

def p_quantifier_number(p):
    '''quantifier_number : MAX
                  | MIN
                  | EXACTLY
                  '''    
    p[0] = p[1]

def p_quantifier_geral(p):
    '''quantifier_geral : SOME
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

    print('namespace_type')

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
