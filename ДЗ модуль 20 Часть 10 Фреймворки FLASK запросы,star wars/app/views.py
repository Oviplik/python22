from app import app
from flask import render_template,request,redirect,url_for
import requests
@app.route('/')
@app.route('/index')
def index():
    listFilms = []
    listPeoples = []
    listPlanets = []
    listStarships = []
    films = requests.get('https://swapi.dev/api/films/').json()
    peoples = requests.get('https://swapi.dev/api/people/').json()
    planets = requests.get('https://swapi.dev/api/planets/').json()
    starships = requests.get('https://swapi.dev/api/starships/').json()
    countFilm = films['count']
    for i in range(countFilm):
        title_film = films['results'][i]['title']
        listFilms.append(title_film)
    for i in peoples['results']:
        listPeoples.append(i['name'])
    for i in planets['results']:
        listPlanets.append(i['name'])
    for i in starships['results']:
        listStarships.append(i['name'])
    return render_template('index.html', title='Main', listFilms=listFilms, listPeoples=listPeoples, listPlanets=listPlanets, listStarships=listStarships)


@app.route('/about_film/<id>')
def about_film(id):
    film = requests.get('https://swapi.dev/api/films/'+id).json()
    title_this_film = film['title']
    return render_template('index.html', title='About film', id = id, film = film, title_this_film = title_this_film)

@app.route('/about_people/<id>')
def about_people(id):
    people = requests.get('https://swapi.dev/api/people/'+id).json()
    name_this_people = people['name']
    return render_template('index.html', title='About people', id = id, people = people, name_this_people = name_this_people)

@app.route('/about_planet/<id>')
def about_planet(id):
    planet = requests.get('https://swapi.dev/api/planets/'+id).json()
    name_this_planet = planet['name']
    return render_template('index.html', title='About planet', id = id, planet = planet, name_this_planet = name_this_planet)

@app.route('/about_starship/<id>')
def about_starship(id):
    starship = requests.get('https://swapi.dev/api/starships/'+id).json()
    name_this_starship = starship['name']
    return render_template('index.html', title='About starship', id = id, starship = starship, name_this_starship = name_this_starship)