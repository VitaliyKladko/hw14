Урок 14. SQL. Домашнее задание (База данных netflix.db)
Маленькое приложение реализует 5 вьюшек и следующие функции:

- def get_by_title(title) - Реализует поиск по названию ленты, если таких фильмов несколько, отдаст самый свежий;
- def search_by_years(start_year, end_year) - Функция отдает результаты поиска по диапазону лет выпуска лент;
- def get_films_by_rating(rating) - Функция показывает фильмы по рейтингу (children, family, adult);
- def film_by_genre(genre) - Функция получает название жанра в качестве аргумента и возвращает 10 самых свежих фильмов в формате json;
- def search_by_actors(first_actor, second_actor) - Функиця получает в качестве аргумента имена двух актеров, сохраняет всех актеров из
колонки cast и возвращает список тех, кто играел с ними в паре больше 2 раз;
- def get_films_by_options(genre, year, type_of) - Функция ищет картины по жанру, году выпуска, типу (TV Show, Movie).