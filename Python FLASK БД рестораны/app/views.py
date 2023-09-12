from app import app
from flask import render_template, flash, redirect, url_for
from app.models import User
from flask import request

from app import db
from app.forms import RegistrationForm, SearchForm, EditForm

@app.route('/')
@app.route('/index')
def index():
    result = User.query.all()
    return render_template('index.html', title='All restaurants', result=result)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    del_rest = User.query.get(id)
    db.session.delete(del_rest)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, spec=form.spec.data,adres=form.adres.data,web=form.web.data,phone=form.phone.data)
        db.session.add(user)
        db.session.commit()
        flash('Ресторан успешно добавлен!')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    edit_rest = User.query.get(id)
    form = EditForm(formdata=request.form, obj=edit_rest)
    if form.validate_on_submit():
        edit_rest.username = form.username.data
        edit_rest.spec = form.spec.data
        edit_rest.adres=form.adres.data
        edit_rest.web = form.web.data
        edit_rest.phone = form.phone.data
        db.session.commit()
        flash('Данные успешно изменены!')
        return redirect(url_for('index'))
    return render_template('edit.html', title='Edit', form=form, edit_rest=edit_rest)

@app.route('/search', methods=['GET','POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('search_results', query = form.search.data))
    return render_template('search.html', title='Search', form=form)

@app.route('/search_results/<query>')
def search_results(query):
    results = db.session.query(User).filter(User.spec == query).all() #Не смог я нормально реализовать поиск через whoosh_search,поэтому сделал так
    return render_template('search_results.html', title='Search', query = query, results = results)