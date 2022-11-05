import sqlite3
import json


def get_films_by_options(genre, year, type_of):
    """
    Функция ищет картины по жанру, году выпуска, типу (TV Show, Movie)
    :param genre: str - Horror Movies
    :param year: int - 2008
    :param type_of: str - Movie
    :return: отдает json словарь, который состоит из show_id, title, description
    """
    genre = f'%{genre}%'

    with sqlite3.connect('./data/netflix.db') as connection:
        cur = connection.cursor()
        sqlite_query = """
                    SELECT show_id, title, description
                    FROM netflix n 
                    WHERE listed_in LIKE ?
                    AND release_year = ?
                    AND "type" = ?
        """
        cur.execute(sqlite_query, (genre, year, type_of))
        execute_result = cur.fetchall()

    result_list = []
    for item in execute_result:
        result_list.append({'show_id': item[0], 'title': item[1], 'description': item[2]})

    return json.dumps(result_list)
