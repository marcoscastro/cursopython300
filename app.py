from flask import Flask

# instância da classe Flask
# __name__ é uma variável especial que especifica o arquivo que está executando
app = Flask(__name__)

# decorator serve para aplicar uma função em cima de outra
# aplicando a função route na função index
# a função route serve para definir uma rota para a página
@app.route("/")
def index():
    return "cursopython300"

# verifica se o usuário está executando o arquivo principal da aplicação
# é uma questão de segurança, só executa se esse for o arquivo principal
if __name__ == "__main__":
    app.run()
