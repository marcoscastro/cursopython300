# configurações da nossa aplicação
from flask import Flask

# instância da classe Flask
# __name__ é uma variável especial que especifica o arquivo que está executando
app = Flask(__name__)

# importação é feita depois porque precisa da variável app
from app.controllers import default
