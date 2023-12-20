import unittest
from task_1 import Movie, UserHistory, RecommendationSystem, load_movies, load_user_histories

class TestRecommendationSystem(unittest.TestCase):
    def setUp(self):
        # Создаем тестовые данные
        movies_data = [
            (1, "Мстители: Финал"),
            (2, "Хатико"),
            (3, "Дюна"),
            (4, "Унесенные призраками"),
        ]

        histories_data = [
            [2, 4],
            [1, 4, 3],
            [2, 2, 2, 2, 2, 3],
        ]

        self.movies = [Movie(movie_id, title) for movie_id, title in movies_data]
        self.user_histories = [UserHistory(movie_ids) for movie_ids in histories_data]

    def test_recommend_movie(self):
        recommendation_system = RecommendationSystem(self.movies, self.user_histories)

        # Тест 1: Пользователь просмотрел "Хатико" и "Дюна"
        test_user_history_1 = UserHistory([2, 3])
        recommendation_1 = recommendation_system.recommend_movie(test_user_history_1)
        self.assertIn(recommendation_1, ["Мстители: Финал", "Унесенные призраками"])

        # Тест 2: Пользователь просмотрел "Унесенные призраками"
        test_user_history_2 = UserHistory([4])
        recommendation_2 = recommendation_system.recommend_movie(test_user_history_2)
        self.assertIn(recommendation_2, ["Мстители: Финал", "Хатико", "Дюна"])

        # Тест 3: Пользователь просмотрел "Хатико" и "Дюна", но также у него есть дополнительные просмотры
        test_user_history_3 = UserHistory([2, 3, 1])
        recommendation_3 = recommendation_system.recommend_movie(test_user_history_3)
        self.assertIn(recommendation_3, ["Унесенные призраками"])

    def test_load_movies(self):
        # Тест загрузки фильмов из файла
        test_movies = load_movies("test_films.txt")
        self.assertEqual(len(test_movies), 4)

    def test_load_user_histories(self):
        # Тест загрузки историй просмотров из файла
        test_user_histories = load_user_histories("test_history.txt")
        self.assertEqual(len(test_user_histories), 3)


if __name__ == "__main__":
    unittest.main()
