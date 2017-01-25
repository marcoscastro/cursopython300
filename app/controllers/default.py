from app import app
from flask import render_template, request, redirect, url_for

# decorator serve para aplicar uma função em cima de outra
# aplicando a função route na função index
# a função route serve para definir uma rota para a página
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/admin/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['password']
        if email == 'admin' and senha == 'admin':
            return redirect(url_for('adicionar_aula'))
        return render_template('admin.html', sucesso=False)
    return redirect(url_for('admin'))

@app.route('/admin/adicionar_aula', methods=['POST', 'GET'])
def adicionar_aula():
    return render_template('adicionar_aula.html')
