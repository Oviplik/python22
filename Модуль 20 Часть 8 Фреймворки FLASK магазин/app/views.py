from app import app
from flask import render_template, flash, redirect, url_for
from app.models import Buyer,Seller,InfoGood,InfoSales
from flask import request
from datetime import datetime
from app import db
from app.forms import RegistrationFormSeller,EditFormSeller,RegistrationFormBuyer,EditFormBuyer,RegistrationFormGood,EditFormGood,RegistrationFormSales,EditFormSales,SearchForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Main')

@app.route('/sellers')
def sellers():
    sellers = Seller.query.all()
    return render_template('index.html', title='Sellers', sellers=sellers)

@app.route('/register_seller', methods=['GET', 'POST'])
def register_seller():
    form = RegistrationFormSeller()
    if form.validate_on_submit():
        seller = Seller(name=form.name.data, surname=form.surname.data,phone=form.phone.data,email=form.email.data,date_start=datetime.strptime(form.date_start.data, '%Y-%m-%d').date(),position=form.position.data)
        db.session.add(seller)
        db.session.commit()
        flash('Продавец успешно зарегистрирован!')
        return redirect(url_for('index'))
    return render_template('register_seller.html', title='Register Seller', form=form)

@app.route('/delete_seller/<int:id>', methods=['GET', 'POST'])
def delete_seller(id):
    del_seller = Seller.query.get(id)
    db.session.delete(del_seller)
    db.session.commit()
    return redirect(url_for('sellers'))

@app.route('/edit_seller/<int:id>', methods=['GET', 'POST'])
def edit_seller(id):
    edit_seller = Seller.query.get(id)
    form = EditFormSeller(formdata=request.form, obj=edit_seller)
    if form.validate_on_submit():
        edit_seller.name = form.name.data
        edit_seller.surname = form.surname.data
        edit_seller.phone=form.phone.data
        edit_seller.email = form.email.data
        edit_seller.date_start = datetime.strptime(form.date_start.data, '%Y-%m-%d').date()
        edit_seller.position = form.position.data
        db.session.commit()
        flash('Данные успешно изменены!')
        return redirect(url_for('sellers'))
    return render_template('edit_seller.html', title='Edit seller', form=form, edit_seller=edit_seller)

@app.route('/buyers')
def buyers():
    buyers = Buyer.query.all()
    return render_template('index.html', title='Buyers', buyers=buyers)

@app.route('/register_buyer', methods=['GET', 'POST'])
def register_buyer():
    form = RegistrationFormBuyer()
    if form.validate_on_submit():
        buyer = Buyer(name=form.name.data, surname=form.surname.data,phone=form.phone.data,email=form.email.data)
        db.session.add(buyer)
        db.session.commit()
        flash('Покупатель успешно зарегистрирован!')
        return redirect(url_for('buyers'))
    return render_template('register_buyer.html', title='Register buyer', form=form)

@app.route('/delete_buyer/<int:id>', methods=['GET', 'POST'])
def delete_buyer(id):
    del_buyer = Buyer.query.get(id)
    db.session.delete(del_buyer)
    db.session.commit()
    return redirect(url_for('buyers'))

@app.route('/edit_buyer/<int:id>', methods=['GET', 'POST'])
def edit_buyer(id):
    edit_buyer = Buyer.query.get(id)
    form = EditFormBuyer(formdata=request.form, obj=edit_buyer)
    if form.validate_on_submit():
        edit_buyer.name = form.name.data
        edit_buyer.surname = form.surname.data
        edit_buyer.phone=form.phone.data
        edit_buyer.email = form.email.data
        db.session.commit()
        flash('Данные успешно изменены!')
        return redirect(url_for('buyers'))
    return render_template('edit_buyer.html', title='Edit buyer', form=form, edit_buyer=edit_buyer)

@app.route('/goods')
def goods():
    goods = InfoGood.query.all()
    return render_template('index.html', title='Goods', goods=goods)

@app.route('/register_good', methods=['GET', 'POST'])
def register_good():
    form = RegistrationFormGood()
    if form.validate_on_submit():
        good = InfoGood(nameGood=form.nameGood.data, aboutGood=form.aboutGood.data)
        db.session.add(good)
        db.session.commit()
        flash('Товар успешно зарегистрирован!')
        return redirect(url_for('goods'))
    return render_template('register_good.html', title='Register good', form=form)

@app.route('/delete_good/<int:id>', methods=['GET', 'POST'])
def delete_good(id):
    del_good = InfoGood.query.get(id)
    db.session.delete(del_good)
    db.session.commit()
    return redirect(url_for('goods'))

@app.route('/edit_good/<int:id>', methods=['GET', 'POST'])
def edit_good(id):
    edit_good = InfoGood.query.get(id)
    form = EditFormGood(formdata=request.form, obj=edit_good)
    if form.validate_on_submit():
        edit_good.nameGood = form.nameGood.data
        edit_good.aboutGood = form.aboutGood.data
        db.session.commit()
        flash('Данные успешно изменены!')
        return redirect(url_for('goods'))
    return render_template('edit_good.html', title='Edit good', form=form, edit_good=edit_good)

@app.route('/sales')
def sales():
    sales = InfoSales.query.all()
    return render_template('index.html', title='Sales', sales=sales)

@app.route('/register_sale', methods=['GET', 'POST'])
def register_sale():
    form = RegistrationFormSales()
    if form.validate_on_submit():
        sale = InfoSales(buyer_id=form.buyer_id.data, seller_id=form.seller_id.data, good_id=form.good_id.data, date_sel=datetime.strptime(form.date_sel.data, '%Y-%m-%d').date(), price_sel=form.price_sel.data)
        db.session.add(sale)
        db.session.commit()
        flash('Продажа успешно зарегистрирован!')
        return redirect(url_for('sales'))
    return render_template('register_sale.html', title='Register sale', form=form)

@app.route('/delete_sale/<int:id>', methods=['GET', 'POST'])
def delete_sale(id):
    del_sale = InfoSales.query.get(id)
    db.session.delete(del_sale)
    db.session.commit()
    return redirect(url_for('sales'))

@app.route('/edit_sale/<int:id>', methods=['GET', 'POST'])
def edit_sale(id):
    edit_sale = InfoSales.query.get(id)
    form = EditFormSales(formdata=request.form, obj=edit_sale)
    if form.validate_on_submit():
        edit_sale.buyer_id = form.buyer_id.data
        edit_sale.seller_id = form.seller_id.data
        edit_sale.good_id = form.good_id.data
        edit_sale.date_sel = datetime.strptime(form.date_sel.data, '%Y-%m-%d').date()
        edit_sale.price_sel = form.price_sel.data
        db.session.commit()
        flash('Данные успешно изменены!')
        return redirect(url_for('sales'))
    return render_template('edit_sale.html', title='Edit sale', form=form, edit_sale=edit_sale)

@app.route('/search_results_buyer/<query>')
def search_results_buyer(query):
    buyer = db.session.query(Buyer).filter(Buyer.id == query).all()
    sales = db.session.query(InfoSales).filter(InfoSales.buyer_id == query).all()
    return render_template('search_results_buyer.html', title='Search buyer', query = query, buyer = buyer, sales = sales)

@app.route('/search_results_seller/<query>')
def search_results_seller(query):
    seller = db.session.query(Seller).filter(Seller.id == query).all()
    sales = db.session.query(InfoSales).filter(InfoSales.seller_id == query).all()
    return render_template('search_results_seller.html', title='Search seller', query = query, seller = seller, sales = sales)
#
# @app.route('/search', methods=['GET','POST'])
# def search():
#     form = SearchForm()
#     if form.validate_on_submit():
#         return redirect(url_for('search_results', query = form.search.data))
#     return render_template('search.html', title='Search', form=form)
#
# @app.route('/search_results/<query>')
# def search_results(query):
#     results = db.session.query(User).filter(User.spec == query).all() #Не смог я нормально реализовать поиск через whoosh_search,поэтому сделал так
#     return render_template('search_results.html', title='Search', query = query, results = results)