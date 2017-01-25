#from app import app
# modificado a forma de execução da aplicação com o manager
from app import manager


# verifica se o usuário está executando o arquivo principal da aplicação
# é uma questão de segurança, só executa se esse for o arquivo principal
if __name__ == "__main__":
    #app.run()
    manager.run() # no terminal: python3 run.py runserver
