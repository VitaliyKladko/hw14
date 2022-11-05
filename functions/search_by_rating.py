import sqlite3
import json


def get_films_by_rating(rating):
    """
    Функция показывает фильмы по рейтингу (children, family, adult)
    :param rating: str
    :return: json
    """
    with sqlite3.connect('./data/netflix.db') as connection:
        cur = connection.cursor()

        if rating == 'children':
            sqlite_query = """
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating = 'G'
            """
        elif rating == 'family':
            sqlite_query = """
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating IN ('G', 'PG', 'PG-13')
            """

        elif rating == 'adult':
            sqlite_query = """
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating IN ('R', 'NC-17')
            """

        else:
            return 'Категория не найдена'

        cur.execute(sqlite_query)
        executed_query = cur.fetchall()

        list_query = []
        for item in executed_query:
            dict_info = {'title': item[0], 'rating': item[1], 'description': item[2]}
            list_query.append(dict_info)

        result = json.dumps(list_query)
        return result
