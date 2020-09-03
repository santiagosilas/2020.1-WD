
print('\nLoad configurations ..\n')


DEBUG = True

# Para prover segurança das sessões client-side
SECRET_KEY = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!'

SQLALCHEMY_DATABASE_URI = 'sqlite:///finances.db'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/finances_db'

# SQLAlchemy monitorará modificações de objetos
SQLALCHEMY_TRACK_MODIFICATIONS = False