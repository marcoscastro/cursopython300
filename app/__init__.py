# configurações da nossa aplicação

from flask import Flask

# instância da classe Flask
# __name__ é uma variável especial que especifica o arquivo que está executando
app = Flask(__name__)

# verifica se o usuário está executando o arquivo principal da aplicação
# é uma questão de segurança, só executa se esse for o arquivo principal
if __name__ == "__main__":
    app.run()
