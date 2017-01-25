from app import app
from flask import render_template

# decorator serve para aplicar uma função em cima de outra
# aplicando a função route na função index
# a função route serve para definir uma rota para a página
@app.route('/')
def index():
    return render_template('index.html')
