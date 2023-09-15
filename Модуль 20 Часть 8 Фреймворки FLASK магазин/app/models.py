from app import db,login

@login.user_loader
def load_user(id):
    return Seller.query.get(int(id))

class Buyer(db.Model):
    __tablename__ = 'buyer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    surname = db.Column(db.String(64), index=True, unique=False)
    phone = db.Column(db.BigInteger, index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    def __repr__(self):
        return 'Имя: {}/ Фамилия: {}/ Контактный телефон: {}/ Email: {}'.format(self.name,self.surname,self.phone,self.email)

class Seller(db.Model):
    __tablename__ = 'seller'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    surname = db.Column(db.String(64), index=True, unique=False)
    phone = db.Column(db.BigInteger, index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    date_start = db.Column(db.Date, index=True, unique=False)
    position = db.Column(db.String(64), index=True, unique=False)
    def __repr__(self):
        return 'Имя: {}/ Фамилия: {}/ Контактный телефон: {}/ Email: {}/ Дата приёма на работу: {}/ Позиция в фирме: {}'.format(self.name,self.surname,self.phone,self.email,self.date_start,self.position)

class InfoGood(db.Model):
    __tablename__ = 'infoGood'
    id = db.Column(db.Integer, primary_key=True)
    nameGood = db.Column(db.String(120), index=True, unique=False)
    aboutGood = db.Column(db.String, index=True, unique=False)

    def __repr__(self):
        return 'Название товара: {}/ Описание товара: {}'.format(self.nameGood, self.aboutGood)

class InfoSales(db.Model):
    __tablename__ = 'infoSales'
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('buyer.id'))
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'))
    good_id = db.Column(db.Integer, db.ForeignKey('infoGood.id'))
    date_sel = db.Column(db.Date, index=True, unique=False)
    price_sel = db.Column(db.Float, index=True, unique=False)

    def __repr__(self):
        return 'ID покупателя: {}/ ID продавца: {}/ ID товара: {}/ дата продажи: {}/ цена товара: {}'.format(self.buyer, self.seller, self.good, self.date_sel, self.price_sel)