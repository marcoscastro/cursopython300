# configurações da nossa aplicação
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instância da classe Flask
# __name__ é uma variável especial que especifica o arquivo que está executando
app = Flask(__name__)

# configuração para conexão com o banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'

# instância do banco, recebe o nosso app
db = SQLAlchemy(app)

# importação é feita depois porque precisa da variável app
from app.controllers import default
