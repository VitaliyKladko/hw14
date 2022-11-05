import sqlite3
import json


def search_by_years(start_year, end_year):
    """
    Функция отдает результаты поиска по диапазону лет выпуска лент
    :param start_year: int - start_year
    :param end_year: int - end_year
    :return: json c title, release_year
    """
    with sqlite3.connect('./data/netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = """
                    SELECT title, release_year
                    FROM netflix
                    WHERE release_year BETWEEN ? AND ?
                    ORDER BY release_year ASC
                    LIMIT 800
                    """
        cursor.execute(sqlite_query, (start_year, end_year))
        executed_query = cursor.fetchall()

        res_list = []
        for item in executed_query:
            dl = {'title': item[0],'release_year': item[1]}
            res_list.append(dl)

        result = json.dumps(res_list)
        return result
