from flask import Flask, render_template, request  # Importa Flask e funções para templates e requisições

app = Flask(__name__)  # Cria a aplicação Flask

def cria_mensagem(nome, idade, altura_texto, estado_civil):
    """
    Cria a mensagem formatada a partir dos dados recebidos.
    Converte altura para float e formata com 2 casas decimais.
    """
    altura = float(altura_texto.replace(',', '.'))
    return f"Olá, meu nome é {nome}, tenho {idade} anos, minha altura é de {altura:.2f} metros, e estou {estado_civil}."

@app.route('/', methods=['GET', 'POST'])
def perfil():
    mensagem = None  # Inicializa variável para mensagem de resposta

    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        idade = request.form.get('idade', '').strip()
        altura_texto = request.form.get('altura', '').strip()
        estado_civil = request.form.get('estado_civil', '').strip()

        # Validação básica dos campos
        if not nome or not idade or not altura_texto or not estado_civil:
            mensagem = "Por favor, preencha todos os campos corretamente."
            return render_template('perfil.html', mensagem=mensagem)

        if not idade.isdigit():
            mensagem = "Por favor, informe uma idade válida (apenas números)."
            return render_template('perfil.html', mensagem=mensagem)

        try:
            # Tenta criar a mensagem com altura convertida
            mensagem = cria_mensagem(nome, idade, altura_texto, estado_civil)
        except ValueError:
            mensagem = "Erro: A altura precisa ser um número válido, ex: 1.75 ou 1,75."
        except Exception as e:
            mensagem = f"Erro inesperado: {e}"

        return render_template('perfil.html', mensagem=mensagem)

    # Se for método GET, apenas renderiza o formulário sem mensagem
    return render_template('perfil.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Roda o servidor no modo debug
