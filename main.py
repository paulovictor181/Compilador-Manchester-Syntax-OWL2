import tkinter as tk
from tkinter import filedialog, messagebox
from lexer import build_lexer
from parser import parse_input


def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        messagebox.showerror("Erro", f"O arquivo '{file_name}' não foi encontrado.")
        return None


def process_file():
    file_name = filedialog.askopenfilename(
        title="Selecione um arquivo",
        filetypes=(("Arquivos de texto", "*.txt"), ("Todos os Arquivos", "*.*"))
    )
    if not file_name:
        return

    code = read_file(file_name)
    if code is None:
        return

    lexer = build_lexer()
    lexer.input(code)

    tokens = []
    for token in lexer:
        tokens.append(f"Token({token.type}, '{token.value}', Linha {token.lineno})")

    # Exibe os tokens encontrados
    resultado_tokens.delete(1.0, tk.END)
    resultado_tokens.insert(tk.END, "\n".join(tokens))

    # Exibe erros léxicos
    resultado_erros_lexicos.delete(1.0, tk.END)
    if lexer.errors:
        resultado_erros_lexicos.insert(tk.END, "\n".join(lexer.errors))
    else:
        resultado_erros_lexicos.insert(tk.END, "Nenhum erro léxico encontrado.")

    lexer.errors.clear()

    # Análise sintática
    sintatico_erros = parse_input(code)

    # Exibe erros sintáticos
    resultado_erros_sintaticos.delete(1.0, tk.END)
    if sintatico_erros:
        resultado_erros_sintaticos.insert(tk.END, "\n".join(sintatico_erros))
    else:
        resultado_erros_sintaticos.insert(tk.END, "Nenhum erro sintático encontrado.")


# Criar a janela principal
janela = tk.Tk()
janela.title("Processador de Tokens")

# Botão para selecionar o arquivo
botao_selecionar = tk.Button(janela, text="Selecionar Arquivo", command=process_file)
botao_selecionar.pack(pady=10)

# Área de texto para exibir os tokens
label_tokens = tk.Label(janela, text="Tokens Encontrados:")
label_tokens.pack()
resultado_tokens = tk.Text(janela, wrap=tk.WORD, height=10, width=60)
resultado_tokens.pack(padx=10, pady=5)

# Área de texto para exibir os erros léxicos
label_erros_lexicos = tk.Label(janela, text="Erros Léxicos:")
label_erros_lexicos.pack()
resultado_erros_lexicos = tk.Text(janela, wrap=tk.WORD, height=10, width=60)
resultado_erros_lexicos.pack(padx=10, pady=5)

# Área de texto para exibir os erros sintáticos
label_erros_sintaticos = tk.Label(janela, text="Erros Sintáticos:")
label_erros_sintaticos.pack()
resultado_erros_sintaticos = tk.Text(janela, wrap=tk.WORD, height=10, width=60)
resultado_erros_sintaticos.pack(padx=10, pady=5)

# Executar a aplicação
janela.mainloop()
