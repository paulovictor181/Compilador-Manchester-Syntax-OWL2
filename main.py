import tkinter as tk
from tkinter import filedialog, messagebox
from lexer import build_lexer
from paser import parse_input


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

    # Exibe os erros encontrados
    resultado_erros.delete(1.0, tk.END)
    if lexer.errors:
        resultado_erros.insert(tk.END, "\n".join(lexer.errors))
    else:
        resultado_erros.insert(tk.END, "Nenhum erro encontrado.")

    lexer.errors.clear()

    # Aqui você pode adicionar a chamada ao seu analisador sintático
    sintatico_erros = parse_input(code)

    # Exibe erros sintáticos
    if sintatico_erros:
        resultado_erros.insert(tk.END, "\nErros sintáticos encontrados:\n")
        resultado_erros.insert(tk.END, "\n".join(sintatico_erros))
    else:
        resultado_erros.insert(tk.END, "\nNenhum erro sintático encontrado.")


# Criar a janela principal
janela = tk.Tk()
janela.title("Processador de Tokens")

# Botão para selecionar o arquivo
botao_selecionar = tk.Button(janela, text="Selecionar Arquivo", command=process_file)
botao_selecionar.pack(pady=10)

# Área de texto para exibir os tokens
resultado_tokens = tk.Text(janela, wrap=tk.WORD, height=10, width=60)
resultado_tokens.pack(padx=10, pady=10)

# Área de texto para exibir os erros
resultado_erros = tk.Text(janela, wrap=tk.WORD, height=10, width=60)
resultado_erros.pack(padx=10, pady=10)

# Executar a aplicação
janela.mainloop()
