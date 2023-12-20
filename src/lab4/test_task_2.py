import unittest
from task_2 import process_files, AgeGroup, Respondent

class TestProgram(unittest.TestCase):
    def test_process_files(self):
        # Тест с входными данными из первого примера
        age_file_content = "18 25 35 45 60 80 100"
        people_file_content = """Кошельков Захар Брониславович,105
Ярилова Розалия Трофимовна,29
Соколов Андрей Сергеевич,15
Дьячков Нисон Иринеевич,88
Старостин Ростислав Ермолаевич,50
Егоров Алан Петрович,7
Иванов Варлам Якунович,88
END
"""

        with open('age_test.txt', 'w') as age_file, open('people_test.txt', 'w') as people_file:
            age_file.write(age_file_content)
            people_file.write(people_file_content)

        result = process_files('age_test.txt', 'people_test.txt')

        expected_result = [
            "101+: Кошельков Захар Брониславович (105)",
            "81-100: Дьячков Нисон Иринеевич (88), Иванов Варлам Якунович (88)",
            "46-60: Старостин Ростислав Ермолаевич (50)",
            "26-35: Ярилова Розалия Трофимовна (29)",
            "0-18: Соколов Андрей Сергеевич (15), Егоров Алан Петрович (7)"
        ]

        self.assertEqual(result, expected_result)

        # Тест с другими входными данными
        age_file_content = "10 20 30"
        people_file_content = """Иванов Иван,15
Петров Петр,25
Сидоров Сидор,35
END
"""

        with open('age_test.txt', 'w') as age_file, open('people_test.txt', 'w') as people_file:
            age_file.write(age_file_content)
            people_file.write(people_file_content)

        result = process_files('age_test.txt', 'people_test.txt')

        expected_result = [
            "31+: Сидоров Сидор (35)",
            "21-30: Петров Петр (25)",
            "11-20: Иванов Иван (15)"
        ]

        self.assertEqual(result, expected_result)

    def test_age_group_creation(self):
        age_group = AgeGroup(30, 40)
        self.assertEqual(age_group.start, 30)
        self.assertEqual(age_group.end, 40)
        self.assertEqual(age_group.respondents, [])

    def test_respondent_creation(self):
        respondent = Respondent("Новиков Новик", 22)
        self.assertEqual(respondent.name, "Новиков Новик")
        self.assertEqual(respondent.age, 22)


if __name__ == '__main__':
    unittest.main()
