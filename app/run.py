from app import app

# verifica se o usuário está executando o arquivo principal da aplicação
# é uma questão de segurança, só executa se esse for o arquivo principal
if __name__ == "__main__":
    app.run()
