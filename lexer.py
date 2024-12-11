import ply.lex as lex

errors = []

reserved = {
    'some': 'SOME',
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
    'CLASS_IDENTIFIER',
    'PROPERTY_IDENTIFIER',
    'PROPERTY_IDENTIFIER_SIMPLE',
    'INDIVIDUAL_NAME',
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
    'COMMA'
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
t_COMMA          = r','


def t_RESERVED(t):
    r'(some|all|value|min|max|exactly|that|not|and|or|Class:|EquivalentTo:|Individuals:|SubClassOf:|DisjointClasses:)'
    t.type = reserved[t.value]  # Mapeia o token reservado
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
    r'[A-Z][a-z]+[0-9]'
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
        print(f"Erro na linha {t.lineno}: Palavra inválida '{t.value}'")

# Contagem de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de errors
def t_error(t):
    errors.append(f"Linha {t.lineno}: Caractere inválido '{t.value[0]}'")
    t.lexer.skip(1)

# Função para inicializar o lexer
def build_lexer():
    lexer = lex.lex()
    lexer.errors = errors
    return lexer