from app import db


class Aula(db.Model):
    __tablename__ = 'aulas'

    # campos da tabela
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(80))
    url = db.Column(db.String(50))
    descricao = db.Column(db.Text)

    # construtor da classe - serve para inicializar os campos
    def __init__(self, titulo, url, descricao):
        self.titulo = titulo
        self.url = url.replace('watch?v=', 'embed/')
        self.descricao = descricao

    # representação do objeto
    def __repr__(self):
        return '<Titulo %r>' % self.titulo


class ComentarioAula(db.Model):
    __tablename__ = 'comentarios_aulas'

    id = db.Column(db.Integer, primary_key=True)
    # se não passar um número para String, então aloca-se o máximo permitido
    nome = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    comentario = db.Column(db.Text)

    # id da aula faz referência à tabela das aulas
    # esse id tem que existir na tabela das aulas
    # trata-se de uma chave estrangeira ou foreign key
    id_aula = db.Column(db.Integer, db.ForeignKey('aulas.id'))

    # relacionamento para obter mais facilmente os dados de uma aula
    # a partir do comentario da aula é possível pegar informações da aula
    # isso facilita para que não precise fazer outra pesquisa
    aula = db.relationship('Aula', foreign_keys=id_aula)

    def __init__(self, nome, email, comentario, id_aula):
        self.nome = nome
        self.email = email
        self.comentario = comentario
        self.id_aula = id_aula

    def __repr__(self):
        return '<ID %r>' % self.id
