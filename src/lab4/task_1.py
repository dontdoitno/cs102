class Movie:
    def __init__(self, movie_id, title):
        self.movie_id = movie_id
        self.title = title

class UserHistory:
    def __init__(self, movie_ids):
        self.movie_ids = movie_ids

class RecommendationSystem:
    def __init__(self, movies, user_histories):
        self.movies = movies
        self.user_histories = user_histories

    def recommend_movie(self, user_history):
        user_movies_set = set(user_history.movie_ids)
        candidates = []

        for other_user_history in self.user_histories:
            if len(set(other_user_history.movie_ids) & user_movies_set) >= len(user_movies_set) / 2:
                candidates.extend(set(other_user_history.movie_ids) - user_movies_set)

        candidates = list(set(candidates) - user_movies_set)

        if not candidates:
            return "Нет рекомендаций"

        movie_views_count = {}
        for other_user_history in self.user_histories:
            for movie_id in candidates:
                if movie_id in other_user_history.movie_ids:
                    movie_views_count[movie_id] = movie_views_count.get(movie_id, 0) + 1

        recommended_movie_id = max(movie_views_count, key=movie_views_count.get)
        return next((movie.title for movie in self.movies if movie.movie_id == recommended_movie_id), "Фильм не найден")


def load_movies(file_path):
    movies = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")
            movie_id, movie_title = int(parts[0]), parts[1]
            movies.append(Movie(movie_id, movie_title))
    return movies

def load_user_histories(file_path):
    user_histories = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            movie_ids = list(map(int, line.strip().split(",")))
            user_histories.append(UserHistory(movie_ids))
    return user_histories


if __name__ == "__main__":
    # Загрузка данных из файлов
    movies = load_movies("list_films.txt")
    user_histories = load_user_histories("history.txt")

    # Создание объекта RecommendationSystem
    recommendation_system = RecommendationSystem(movies, user_histories)

    # Ввод истории просмотров текущего пользователя
    user_history_input = input("Введите идентификаторы просмотренных фильмов через запятую: ")
    user_history = UserHistory(list(map(int, user_history_input.strip().split(","))))

    # Рекомендация фильма
    recommendation = recommendation_system.recommend_movie(user_history)
    print("Рекомендация:", recommendation)
