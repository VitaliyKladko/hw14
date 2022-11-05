import sqlite3
import json


def film_by_genre(genre):
    """
    Функция получает название жанра в качестве аргумента и возвращает 10 самых свежих фильмов в формате json.
    :param genre: str - название
    :return: json
    """
    genre = f'%{genre}%'
    with sqlite3.connect('./data/netflix.db') as connect:
        cur = connect.cursor()
        sqlite_query = """
                SELECT title, release_year, listed_in, description
                from netflix n 
                WHERE listed_in LIKE ?
                ORDER BY release_year DESC 
                LIMIT 10
        """

        cur.execute(sqlite_query, (genre,))
        execute_result = cur.fetchall()

        list_result = []
        for item in execute_result:
            dict_info = {'title': item[0], 'release_year': item[1], 'listed_in': item[2], 'description': item[3]}
            list_result.append(dict_info)
        result = json.dumps(list_result)

        return result
