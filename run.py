from flask import Flask, jsonify
from functions import search_by_title, search_by_release_year, search_by_rating, search_by_genre

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def main_page():
    return 'ДЗ № 14, приложение, для поиска фильмов и сериалов по различным параметрам из netflix.db'


@app.route('/movie/<title>/')
def search_by_title_page(title):
    results = search_by_title.get_by_title(title)
    return jsonify(results)


@app.route('/movie/<int:year_1>/to/<int:year_2>/')
def movie_by_year(year_1, year_2):
    result = search_by_release_year.search_by_years(year_1, year_2)
    return jsonify(result)


@app.route('/rating/<rating>')
def movies_by_rating(rating):
    result = search_by_rating.get_films_by_rating(rating)
    return jsonify(result)


@app.route('/genre/<genre>/')
def movies_by_genre(genre):
    result = search_by_genre.film_by_genre(genre)
    return jsonify(result)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


if __name__ == '__main__':
    app.run()
