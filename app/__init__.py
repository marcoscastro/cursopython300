from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# instância da classe Flask
# __name__ é uma variável especial que especifica o arquivo que está executando
app = Flask(__name__)

# configuração da aplicação
app.config.from_object('config')

# instância do banco, recebe o nosso app
db = SQLAlchemy(app)

# migrate recebe o app e a instância do banco
migrate = Migrate(app, db)

# o manager é o controle de informações que passamos na execução
manager = Manager(app)

# adicionamos ao manager o comando db
# exemplo: python3 run.py db init -> cria a pasta migrations
# a pasta migrations salva informações das migrações
# comando para fazer migrações: python3 run.py db migrate
# o comando acima pega o que está definido no nosso banco e compara
# com o que já existe para verificar o que precisa alterar
# com o comando migrate ele cria o arquivo de banco se for sqlite
# a migração é aplicada com o comando: python3 run.py db upgrade
# após o comando upgrade pela primeira vez serão criadas as nossas tabelas
# o comando migrate e upgrade são utilizados quando alteramos o banco de dados
manager.add_command('db', MigrateCommand)

# importação é feita depois porque precisa da variável app
from app.controllers import default
from app.models import tables
