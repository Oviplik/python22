from app import db,login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=False)
    spec = db.Column(db.String(64), index=True, unique=False)
    adres = db.Column(db.String(64), index=True, unique=False)
    web = db.Column(db.String(64), index=True, unique=False)
    phone = db.Column(db.String(64), index=True, unique=False)


    def __repr__(self):
        return 'Название ресторана: {}/ Национальная кухня: {}/ Где находиться: {}/ Веб-сайт: {}/ Номер контактного телефона: {}'.format(self.username,self.spec,self.adres,self.web,self.phone,self.id)