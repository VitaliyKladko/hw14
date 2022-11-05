import sqlite3
import json


def get_by_title(title):
    """
    Реализует поиск по названию ленты, если таких фильмов несколько, отдаст самый свежий
    :param title: str - title
    :return: json - title, country, release_year, listed_in, description
    """
    with sqlite3.connect('./data/netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = """
                    SELECT title, country, release_year, listed_in, description
                    FROM netflix
                    WHERE title = ?
                    ORDER BY release_year DESC
                    LIMIT 1
                    """
        cursor.execute(sqlite_query, (title,))
        executed_query = cursor.fetchone()
        answer_dict = {}
        dict_key = ['title', 'country', 'release_year', 'genre', 'description']
        if executed_query is None:
            return 'Фильм отсутствует в базе'

        for item in range(len(executed_query)):
            answer_dict[dict_key[item]] = executed_query[item]

        result = json.dumps(answer_dict)

        return result
