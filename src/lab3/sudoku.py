import pathlib
import random
import typing as tp

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    matrix = [[0] * n for _ in range(n)]  # Создаем пустую матрицу с нулями

    pos = 0  # текущая позиция в списке
    # заполняем пустую матрицу нужными значениями
    for i in range(n):
        for j in range(n):
            matrix[i][j] = values[pos]
            pos += 1

    return matrix


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    row, col = pos

    return grid[row]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    row, col = pos

    res = []
    for r in range(len(grid[0])):
        res.append(grid[r][col])

    return res


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    row, col = pos
    size = len(grid)

    # Находим размер блока (квадрата)
    block_size = int(size**0.5)

    # Находим номер блока (квадрата) в матрице
    block_row = row // block_size
    block_col = col // block_size

    # Вычисляем координаты верхнего левого угла блока
    start_row, start_col = block_row * block_size, block_col * block_size

    # Собираем значения из блока
    block_values = []
    for i in range(start_row, start_row + block_size):
        for j in range(start_col, start_col + block_size):
            block_values.append(grid[i][j])

    return block_values


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    row, col = len(grid[0]), len(grid)  # длина строк и столбцов в судоку

    for r in range(row):
        for c in range(col):
            if grid[r][c] == '.':
                return r, c  # возвращаем кортеж


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    size = len(grid)

    # Собираем значения из строки, столбца и блока
    row_values = set(get_row(grid, pos))
    col_values = set(get_col(grid, pos))
    block_values = set(get_block(grid, pos))

    # Объединяем значения из строки, столбца и блока
    all_values = row_values | col_values | block_values

    # Возвращаем разность множеств (все возможные значения за исключением уже заполненных)
    return set(map(str, range(1, size + 1))) - all_values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """

    empty_position = find_empty_positions(grid)

    # Если нет свободных позиций, пазл уже решен
    if not empty_position:
        return grid

    row, col = empty_position

    # Находим все возможные значения для свободной позиции
    possible_values = find_possible_values(grid, empty_position)

    # Пытаемся установить каждое возможное значение
    for value in possible_values:
        # Устанавливаем значение на позицию
        grid[row][col] = value

        # Рекурсивно вызываем solve для оставшейся части пазла
        solution = solve(grid)

        # Если найдено решение, возвращаем пазл
        if solution:
            return solution

        # Если не найдено решение, отменяем установку значения
        grid[row][col] = '.'

    # Если ни для одного из возможных значений не найдено решение
    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False
    >>> correct_solution = [
    ...     ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
    ...     ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    ...     ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    ...     ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    ...     ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    ...     ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
    ...     ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
    ...     ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
    ...     ['3', '4', '5', '2', '8', '6', '1', '7', '9']
    ... ]
    >>> check_solution(correct_solution)
    True

    >>> incorrect_solution = [
    ...     ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
    ...     ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    ...     ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    ...     ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    ...     ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    ...     ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
    ...     ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
    ...     ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
    ...     ['3', '4', '5', '2', '8', '6', '1', '7', '8']
    ... ]
    >>> check_solution(incorrect_solution)
    False
    """

    size = len(solution)

    def has_duplicates(values: tp.List[str]) -> bool:
        """Проверяет, есть ли повторяющиеся значения в списке"""
        seen = set()
        for value in values:
            if value != '.' and value in seen:
                return True
            seen.add(value)
        return False

    # Проверка строк
    for row in solution:
        if has_duplicates(row):
            return False

    # Проверка столбцов
    for col in range(size):
        column_values = get_col(solution, (0, col))
        if has_duplicates(column_values):
            return False

    # Проверка блоков
    block_size = int(size**0.5)
    for row in range(0, size, block_size):
        for col in range(0, size, block_size):
            block_values = get_block(solution, (row, col))
            if has_duplicates(block_values):
                return False

    # Если все проверки пройдены, возвращаем True
    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """

    # Создаем пустую сетку
    grid = [['.' for _ in range(9)] for _ in range(9)]

    # Решаем пустую сетку
    solution = solve(grid)

    # Оставляем N элементов
    cells_to_remove = 81 - N
    positions = [(row, col) for row in range(9) for col in range(9)]
    random.shuffle(positions)

    for pos in positions[:cells_to_remove]:
        row, col = pos
        grid[row][col] = '.'

    return grid

if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
