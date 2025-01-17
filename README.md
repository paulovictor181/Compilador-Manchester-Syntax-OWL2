# Compilador-Manchester-Syntax-OWL2

Esse projeto tem como objetivo construir um compilador para reconhecimento da linguagem OWL2 (Web Ontology Language) no formato Manchester Syntax.

# Índice 

* [Compilador](##Compilador)
* [Analisador léxico](#analisador-léxico)
* [Analisador sintático](#analisador-sintático)
* [Analisador semântico](#analisador-semântico)
* [Ply](##Ply)
* [Requisitos](##Requisitos/Como-usar)


## Compilador 

Um compilador é um programa de computador que traduz nossos códigos-fontes, escrito em uma linguagem de programação de alto nível (como C, Java, Python), para uma linguagem de baixo nível ou linguagem de máquina, que o computador pode entender e executar. 

## Analisador Léxico

A análise léxica é o estágio inicial no planejamento do compilador. Um lexema
é um agrupamento de caracteres distintos dentro de um conjunto de tokens. A análise léxica é executada para examinar todo o código-fonte do desenvolvedor. 

O analisador léxico é utilizado para realizar a varredura do programa em seu código-fonte, caractere por caractere, a fim de distingui-los na tabela de símbolos. Um agrupamento de caracteres que não podem ser scaneados é considerado um erro léxico. 

```
BARBOSA, Cynthia da S.; LENZ, Maikon L.; LACERDA, Paulo S. Pádua de; et al. Compiladores. Porto Alegre: SAGAH, 2021. E-book. p.57. ISBN 9786556902906.
```
## Analisador Sintático

A análise sintática é o processo após a análise léxica de uma compilação.
O analisador sintático é o coração da compilação, pois os demais processos pós-análise sintática, como analisador semântico e gerador de código intermediário, são guiados pelas ações da etapa de análise sintática.

```
BARBOSA, Cynthia da S.; LENZ, Maikon L.; LACERDA, Paulo S. Pádua de; et al. Compiladores. Porto Alegre: SAGAH, 2021. E-book. p.90. ISBN 9786556902906. 
```

O analisador sintático verifica a estrutura do código e se ele segue a gramática da linguagem de programação. Organizando os tokens em uma árvore sintática que representa a hierarquia do código, .

## Analisador Semântico

O compilador verifica se o código faz sentido, ou seja, se as operações são válidas de acordo com as regras da linguagem, como tipos de dados compatíveis ou variáveis declaradas corretamente.

## Ply - Python

### Introdução 

PLY é uma implementação Python pura das populares ferramentas de construção de compiladores lex e yacc. O principal objetivo do PLY é permanecer razoavelmente fiel à maneira como as ferramentas tradicionais lex/yacc funcionam. Isso inclui suporte à análise sintática LALR(1), bem como fornecer validação de entrada extensiva, relatórios de erros e diagnósticos. Portanto, se você usou yacc em outra linguagem de programação, deve ser relativamente simples usar o PLY.

### Lex e Yacc

PLY consiste em dois módulos separados; lex.py e yacc.py , ambos encontrados em um pacote Python chamado ply . O módulo lex.py é usado para quebrar o texto de entrada em uma coleção de tokens especificados por uma coleção de regras de expressão regular. yacc.py é usado para reconhecer a sintaxe da linguagem que foi especificada na forma de uma gramática livre de contexto.

### Lex 

lex.py é usado para tokenizar uma string de entrada. Por exemplo, suponha que você esteja escrevendo uma linguagem de programação e um usuário forneceu a seguinte string de entrada:

```
x = 3 + 42 * (s - t)
```
Um tokenizador divide a string em tokens individuais

```
'x','=', '3', '+', '42', '*', '(', 's', '-', 't', ')'
```
Tokens geralmente são definidos por nomes e são inseridos junto com os valores na tabela de lexemas . Por exemplo:

```
('ID','x'), ('IGUAL A','='), ('NÚMERO','3'),
('MAIS','+'), ('NÚMERO','42), ('VEZES','*'),
('EPARENTE','('), ('ID','s'), ('MENOS','-'),
('ID','t'), ('DPARENTE',')'
```

### Lex exemplo

```
importar ply.lex como lex

# Lista de nomes de tokens. Isso é sempre necessário
tokens = (
   'NÚMERO',
   'MAIS',
   'MENOS',
   'TEMPOS',
   'DIVIDIR',
   'EPARENTE',
   'DPARENTE',
)

# Regras de expressão regular para tokens simples
t_PLUS = r'\+'
t_MENOS = r'-'
t_TEMPOS = r'\*'
t_DIVIDIR = r'/'
t_EPARENTE = r'\('
t_DPARENTE = r'\)'

# Uma regra de expressão regular com algum código de ação
def t_NUMBER(t):
    r'\d+'
    t.valor = int(t.valor)    
    retornar t

# Defina uma regra para que possamos rastrear números de linha
definição t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.valor)

# Uma string contendo caracteres ignorados (espaços e tabulações)
t_ignore = ' \t'

# Regra de tratamento de erros
definição t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.pular(1)

# Construir o analisador léxico
lexer = lex.lex()

# Para usar o lexer, primeiro você precisa alimentá-lo com algum texto de #
# entrada usando seu método input() . Depois disso, chamadas repetidas 
# para token() produzem tokens. O código a seguir mostra como isso funciona:


# Dê alguma entrada ao analisador léxico
lexer.input(dados)

# Tokenizar
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)


```
### Especificação de tokens

Cada token é especificado escrevendo uma regra de expressão regular compatível com o módulo re do Python . Cada uma dessas regras é definida fazendo declarações com um prefixo especial t_ para indicar que ele define um token. Para tokens simples, a expressão regular pode ser especificada como strings como esta (nota: strings brutas do Python são usadas, pois são a maneira mais conveniente de escrever strings de expressão regular):

```
t_PLUS = r'\+'
```

Neste caso, o nome após o t_ deve corresponder exatamente a um dos nomes fornecidos em tokens . Se algum tipo de ação precisa ser executada, uma regra de token pode ser especificada como uma função. Por exemplo, esta regra corresponde a números e converte a string em um inteiro Python.

```
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    retornar t
```


### Fichas descartadas
Para descartar um token, como um comentário, basta definir uma regra de token que não retorne nenhum valor. Por exemplo:
```
def t_COMMENT(t):
    r'\#.*'
    pass
    # Nenhum valor de retorno. Token descartado
```

### Tratamento de erros
A função t_error() é usada para manipular erros de lexing que ocorrem quando caracteres ilegais são detectados. Nesse caso, o atributo t.value contém o restante da string de entrada que não foi tokenizada. No exemplo, a função de erro foi definida da seguinte forma:

```
# Regra de tratamento de erros
def t_error(t):
    print("Invalido caractere '%s'" % t.value[0])
    t.lexer.skip(1)
```

### Yacc

O módulo ply.yacc implementa o componente de análise do PLY. O nome "yacc" significa "Yet Another Compiler Compiler" e é emprestado da ferramenta Unix de mesmo nome.

### Yacc exemplo

Suponha que você queira fazer uma gramática para expressões aritméticas simples: 

```
import ply.yacc as yacc

# Obtenha o mapa de token do lexer. Isso é obrigatório. 
de calclex importar tokens 

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Regra de erro para erros de sintaxe 
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = raw_input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)

```

Neste exemplo, cada regra gramatical é definida por uma função Python onde a docstring para essa função contém a especificação gramatical livre de contexto apropriada. As instruções que compõem o corpo da função implementam as ações semânticas da regra. Cada função aceita um único argumento p que é uma sequência contendo os valores de cada símbolo gramatical na regra correspondente. Os valores de p[i] são mapeados para símbolos gramaticais conforme mostrado aqui:

```
    def p_expression_plus(p):
        'expression : expression PLUS term'
        #   ^            ^        ^    ^
        #  p[0]         p[1]     p[2] p[3]

        p[0] = p[1] + p[3]
```

### Combinando funções de regras gramaticais (Rules) 
Quando as regras gramaticais são semelhantes, elas podem ser combinadas em uma única função. Por exemplo, considere as duas regras em nosso exemplo anterior:

```
    def p_expression_plus(p):
        'expression : expression PLUS term'
        p[0] = p[1] + p[3]

    def p_expression_minus(t):
        'expression : expression MINUS term'
        p[0] = p[1] - p[3]
```

Em vez de escrever duas funções, você pode escrever uma única função como esta:


```
    def p_expression(p):
        '''expression : expression PLUS term
                    | expression MINUS term'''
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
```

### Produções Vazias
yacc.py pode manipular produções vazias definindo uma regra como esta:
```
    def p_empty(p):
        'empty :'
        pass
```
Agora, para usar a produção vazia, basta usar 'empty' como símbolo. Por exemplo:
```
    def p_optitem(p):
        'optitem : item'
        '        | empty'
        ...
```


### O arquivo parser.out

O yacc.py usa o algoritmo de análise sintática LR(1), que lê a entrada da esquerda para a direita e faz uma derivação à direita. Durante a análise, podem ocorrer conflitos shift/reduce (quando o parser não sabe se deve deslocar ou reduzir) e reduce/reduce (quando há múltiplas opções de redução para o mesmo conjunto de tokens). Quando esses conflitos acontecem, o yacc.py gera um arquivo de depuração chamado parser.out, que contém informações detalhadas sobre os conflitos, facilitando a depuração e o ajuste da gramática.

## Requisitos/Como usar

Para rodar o projeto é recomendado a utilização do WSL ou uso direto do Linux, pois a maioria das distros já possuem o Python3 instalado.

Link de como instalar o WSL: [Link](https://learn.microsoft.com/pt-br/windows/wsl/install)

### Requisitos obrigatórios

- Python 3.x
- PIP
- PLY (Python Lex-Yacc)

Caso sua Distro não tenha Python por padrão:

```
// BASE DEBIAN
sudo apt update
sudo apt install python3

// BASE FEDORA 
sudo dnf install python3

// BASE ARCH
sudo pacman -S python
```

Instale o PIP usando:

```
sudo apt update
sudo apt install python3-pip
```

Instale o venv usando:

```
sudo apt install python3.12-venv
```

Entre na pasta do projeto e execute o seguinte comanda para iniciar ambiente virtual:

```
python3 -m venv nomeDoAmbiente
```

Ative o ambiente virtual:

```
source nomeDoAmbiente/bin/activate
```

Instale o PLY usando o `pip`:

```
pip install ply
```

Instale o Tkinter usando:

```
sudo apt-get install python3-tk
```

### Comandos para rodar o projeto

```
python3 main.py
```

### Ferramentas para rodar e analisar o projeto
- [VS Code](https://code.visualstudio.com/download)  
- Extensões para o VS Code
    - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)  
    - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)  
    - [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)  

