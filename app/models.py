from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash #senha hash

    # blueprint for auth routes in our app
   # from .auth import auth as auth_blueprint
   # app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
   # from .main import main as main_blueprint
    #app.register_blueprint(main_blueprint)

   # return app


@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin): #usuarios
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(70), nullable=False, unique=True)
    password = db.Column(db.String(2048), nullable=False)


#class receitapost(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
 #   title = db.Column(db.String(200))
 #   content = db.Column(db.Text)
  #  passo = db.Column(db.Text)
   # ingredientes = db.Column(db.Text)
   # date_posted = db.Column(db.DateTime)
    #userid = db.Column(db.Integer, ForeignKey('User.id'))
   # user = db.relationship('User', foreign_keys=userid)
   # imagem = db.Column(db.LargeBinary, nullable =False)

#class perfil(db.Model, UserMixin):
   # user_id = Column(db.Integer, ForeignKey('User.id'), nullable=False)
    #name = Column(db.String, ForeignKey('User.name'), nullable=False)
   # email = Column(db.String, ForeignKey('User.email'), nullable=False)
   # imagem = db.Column(db.LargeBinary, nullable =False)
    #Caso o usuário queira redefinir a senha, redirecione para a tela de login e clique em "Esqueci minha senha"

#class Receitas(db.Model):
 #   id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  #  titulo = db.Column(db.String(50), nullable=False)
   # desc = db.Column(db.String(100), nullable=False)
    #tempo_preparo = db.Column(db.DateTime(), nullable=False)
    #rendimento = db.Column(db.String(50), nullable=False)
    #imagem = db.Column(db.LargeBinary, nullable =False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def __str__(self):
        return f'Usuário {self.name} tem o e-mail {self.email}'





