import os

BASEDIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASEDIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
# vscode://vscode.github-authentication/did-authenticate?windowid=1&code=6fc03d6584257e52c61c&state=c4d50756-81f0-452b-bd18-f1aaa4375426