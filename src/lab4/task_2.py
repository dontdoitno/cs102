class AgeGroup:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.respondents = []

    def add_respondent(self, respondent):
        self.respondents.append(respondent)

    def __str__(self):
        if self.end == float('inf'):
            return f"{self.start}+: " + ', '.join(str(respondent) for respondent in self.respondents)
        else:
            return f"{self.start}-{self.end}: " + ', '.join(str(respondent) for respondent in self.respondents)


class Respondent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        if self.age == other.age:
            return self.name < other.name
        return self.age > other.age

    def __str__(self):
        return f"{self.name} ({self.age})"


def process_files(age_file_path, people_file_path):
    age_groups = []
    respondents = []

    # чтение рамок возраста из age.txt
    with open(age_file_path, 'r') as age_file:
        age_ranges = list(map(int, age_file.readline().split()))

    # создание возрастных групп с корректными границами
    start_age = float('inf')  # начинаем с бесконечной верхней границы
    for end_age in reversed(age_ranges):
        age_groups.append(AgeGroup(end_age + 1, start_age))
        start_age = end_age

    # добавляем последнюю группу
    age_groups.append(AgeGroup(0, start_age))

    # чтение людей из people.txt
    with open(people_file_path, 'r') as people_file:
        for line in people_file:
            if line.strip() == 'END':
                break
            name, age = map(str.strip, line.split(','))
            respondents.append(Respondent(name, int(age)))  # Преобразование возраста в целое число

    # распределение людей по возрастным группам
    for respondent in respondents:
        for age_group in age_groups:
            if age_group.start <= respondent.age <= age_group.end:
                age_group.add_respondent(respondent)
                break

    # фильтрация и сортировка возрастных групп
    result = [str(age_group) for age_group in age_groups if age_group.respondents]

    return result


if __name__ == "__main__":
    age_file_path = "age.txt"
    people_file_path = "people.txt"

    result = process_files(age_file_path, people_file_path)

    for line in result:
        print(line)
