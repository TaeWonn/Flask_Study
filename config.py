import os

BASEDIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASEDIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
