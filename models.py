from quizcreator import db

# criação da classe usuário conectada com o banco de dados mysql
class tb_user(db.Model):
    cod_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_user = db.Column(db.String(50), nullable=False)
    password_user = db.Column(db.String(50), nullable=False)
    status_user = db.Column(db.Integer, nullable=False)
    login_user = db.Column(db.String(50), nullable=False)
    cod_usertype = db.Column(db.Integer, nullable=False)
    email_user = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

# criação da classe tipousuário conectada com o banco de dados mysql
class tb_usertype(db.Model):
    cod_usertype = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desc_usertype = db.Column(db.String(50), nullable=False)
    status_usertype = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.name    

# criação da classe tipousuário conectada com o banco de dados mysql
class tb_tipostatus(db.Model):
    cod_tipostatus = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desc_tipostatus = db.Column(db.String(50), nullable=False)
    status_tipostatus = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.name    

# criação da classe pesquisa conectada com o banco de dados mysql
class tb_pesquisa(db.Model):
    cod_pesquisa = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_pesquisa = db.Column(db.String(200), nullable=False)
    desc_pesquisa = db.Column(db.String(200), nullable=False)
    codext_pesquisa = db.Column(db.String(50), nullable=False)
    cod_tipostatus = db.Column(db.Integer, nullable=False)
    cod_user = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.name    

# criação da classe pergunta conectada com o banco de dados mysql
class tb_pergunta(db.Model):
    cod_pergunta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desc_pergunta = db.Column(db.String(200), nullable=False)
    status_pergunta = db.Column(db.Integer, nullable=False)
    ordem_pergunta = db.Column(db.Integer, nullable=False)
    cod_pesquisa = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.name    

# criação da classe pergunta conectada com o banco de dados mysql
class tb_resposta(db.Model):
    cod_resposta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desc_resposta = db.Column(db.String(200), nullable=False)
    status_resposta = db.Column(db.Integer, nullable=False)
    certa_resposta = db.Column(db.Integer, nullable=False)
    cod_pergunta = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.name 

# criação da classe respostauser conectada com o banco de dados mysql
class tb_respostauser(db.Model):
    cod_respostauser = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cod_pesquisa = db.Column(db.Integer, nullable=False)
    cod_pergunta = db.Column(db.Integer, nullable=False)
    cod_user = db.Column(db.Integer, nullable=False)
    cod_resposta = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.name 
