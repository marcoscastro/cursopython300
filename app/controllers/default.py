from app import app, db
from app.models.tables import Aula
from flask import render_template, request, redirect, url_for

# decorator serve para aplicar uma função em cima de outra
# aplicando a função route na função index
# a função route serve para definir uma rota para a página
@app.route('/')
def index():
    aula = Aula.query.filter_by(id=1).first()
    return render_template('index.html', aula=aula)

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
    if request.method == 'POST':
        titulo = request.form['titulo_aula']
        url = request.form['url_aula']
        desc = request.form['desc_aula']
        if titulo and url and desc:
            aula = Aula(titulo=titulo, url=url, descricao=desc)
            db.session.add(aula)
            db.session.commit()
            return render_template('adicionar_aula.html', sucesso=True)
        return render_template('adicionar_aula.html', sucesso=False)
    return render_template('adicionar_aula.html', sucesso=None)

@app.route('/aula/<aula_id>')
def aula(aula_id):
    aula = Aula.query.filter_by(id=aula_id).first()
    if aula is None:
        return redirect(url_for('index'))
    return render_template('aula.html', aula=aula)
