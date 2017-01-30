# configurações da nossa aplicação
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'banco.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
