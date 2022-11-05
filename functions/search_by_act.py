import sqlite3


def search_by_actors(first_actor, second_actor):
    """
    Функиця получает в качестве аргумента имена двух актеров, сохраняет всех актеров из колонки cast и возвращает список
    тех, кто играел с ними в паре больше 2 раз.
    :param first_actor: str - name #1
    :param second_actor: str - name #2
    :return: list с им. актёров. Прим.: Rose McIver и Ben Lamb, Jack Black и Dustin Hoffman.
    """
    first_actor = f'%{first_actor}%'
    second_actor = f'%{second_actor}%'
    with sqlite3.connect('./data/netflix.db') as connection:
        cur = connection.cursor()
        sqlite_query = """
                SELECT "cast"
                from netflix
                WHERE "cast" LIKE ?
                AND "cast" LIKE ?
        """
        cur.execute(sqlite_query, (first_actor, second_actor,))
        execute_result = cur.fetchall()

    # список, в который идут все актеры и из колонки CAST
    cast = []
    for i in range(len(execute_result)):
        for item in execute_result[i][0].split(', '):
            cast.append(item)

    cast_tuple = tuple(cast)

    # словарик с именем и количеством повторений, все что больше 2-х - искомые актеры
    dl = {}
    for i in range(len(cast_tuple)):
        for j in cast_tuple:
            dl[j] = cast_tuple.count(j)

    # сохраняем в result_list_with_act имена актеров, которые снимались с first_actor и second_actor более 2-х раз
    result_list_with_act = []
    for item, value in dl.items():
        if value > 2 and item not in first_actor + second_actor:
            result_list_with_act.append(item)

    return result_list_with_act
