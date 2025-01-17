import ply.lex as lex

errors = []

reserved = {
    'some': 'SOME',
    'only': 'ONLY',
    'all': 'ALL',
    'value': 'VALUE',
    'min': 'MIN',
    'max': 'MAX',
    'exactly': 'EXACTLY',
    'that': 'THAT',
    'not': 'NOT',
    'and': 'AND',
    'or': 'OR',
    'Class:': 'CLASS',
    'EquivalentTo:': 'EQUIVALENTTO',
    'Individuals:': 'INDIVIDUALS',
    'SubClassOf:': 'SUBCLASSOF',
    'DisjointClasses:': 'DISJOINTCLASSES',
    'DisjointWith:': 'DISJOINtWITH'
}

VALID_TYPES = [
    'rational',
    'real',
    'langString',
    'PlainLiteral',
    'XMLLiteral',
    'Literal',
    'anyURI',
    'base64Binary',
    'boolean',
    'byte',
    'dateTime',
    'dateTimeStamp',
    'decimal',
    'double',
    'float',
    'hexBinary',
    'int',
    'integer',
    'language',
    'long',
    'Name',
    'NCName',
    'negativeInteger',
    'NMTOKEN',
    'nonNegativeInteger',
    'nonPositiveInteger',
    'normalizedString',
    'positiveInteger',
    'short',
    'string',
    'token',
    'unsignedByte',
    'unsignedInt',
    'unsignedLong',
    'unsignedShort'
]

# Lista de tokens
tokens = [
    'INDIVIDUAL_NAME',
    'CLASS_IDENTIFIER',
    'PROPERTY_IDENTIFIER',
    'PROPERTY_IDENTIFIER_SIMPLE',
    'CARDINALITY',
    'NAMESPACE',
    'TYPE',
    'OPEN_BRACKET',
    'CLOSE_BRACKET',
    'OPEN_CURLY',
    'CLOSE_CURLY',
    'OPEN_PAREN',
    'CLOSE_PAREN',
    'LESS_THAN',
    'GREATER_THAN',
    'COMMA',
    'EQUAL',
] + list(reserved.values())


# Ignorar espaços e tabulações
t_ignore = ' \t'

# Regular expression rules for simple tokens
t_OPEN_BRACKET   = r'\['
t_CLOSE_BRACKET  = r'\]'
t_OPEN_CURLY     = r'\{'
t_CLOSE_CURLY    = r'\}'
t_OPEN_PAREN     = r'\('
t_CLOSE_PAREN    = r'\)'
t_LESS_THAN      = r'\<'
t_GREATER_THAN   = r'\>'
t_EQUAL          = r'\='
t_COMMA          = r','

def t_RESERVED(t):
    r'(some|only|all|value|min|max|exactly|that|not|and|or|Class:|EquivalentTo:|Individuals:|SubClassOf:|DisjointClasses:|DisjointWith:)'
    t.type = reserved[t.value] 
    return t

def t_NAMESPACE(t):
    r'(owl|rdfs|xsd|rdf):'
    t.type = 'NAMESPACE'
    return t

def t_PROPERTY_IDENTIFIER(t):
    r'(has|is)[a-zA-Z0-9]+(Of)?'
    return t

def t_PROPERTY_IDENTIFIER_SIMPLE(t):
    r'[a-z][a-zA-Z]*'

    if t.value in VALID_TYPES:
        t.type = 'TYPE'
    else:
        t.type = 'PROPERTY_IDENTIFIER'
    return t

def t_INDIVIDUAL_NAME(t):
    r'[A-Z][a-z]*(?:[A-Z][a-z]*)*[0-9]+'
    return t

def t_CLASS_IDENTIFIER(t):
    r'[A-Z][a-zA-Z_]*'
    return t

def t_CARDINALITY(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_TYPE(t):
    r'[a-zA-Z]+'
    if t.value in VALID_TYPES:
        t.type = 'TYPE'
        return t
    else:
        errors.append(f"Erro Lexico: Erro na linha {t.lineno}: TYPE inválido '{t.value}'")
        t.lexer.skip(1)  # Pular o caractere inválido

# Contagem de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    t.lexer.errors.append(f"Erro Lexico: Linha {t.lineno}: Caractere inválido '{t.value[0]}'")
    t.lexer.skip(1)

# Função para inicializar o lexer
def build_lexer():
    lexer = lex.lex()
    lexer.errors = []  # Lista para armazenar os erros léxicos
    return lexer