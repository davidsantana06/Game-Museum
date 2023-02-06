from app import db


class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    plataform = db.Column(db.String(30), nullable=False)
    mushrooms = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Users(db.Model):
    username = db.Column(db.String(12), primary_key=True)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
