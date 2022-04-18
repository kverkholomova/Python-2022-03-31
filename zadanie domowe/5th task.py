# Z5.
# Dana jest prostokątna tablica 𝑇𝑚𝑛, gdzie 𝑚 oznacza liczbę wierszy, a 𝑛 liczbę kolumn. Tablica
# wypełniona jest przez użytkownika wyłącznie zerami i jedynkami. Dla przykładu, użytkownik
# utworzył tablicę 𝑇56 i wypełnił ją zerami i jedynkami w następujący sposób:
# 1 1 1 0 1 0
# 0 1 1 1 0 1
# 1 1 0 0 0 1
# 0 1 1 1 0 1
# 1 0 0 1 0 1
# Ciąg jedynek przyległych w poziomie lub w pionie tworzy drogę. Należy sprawdzić, czy między
# wskazanym przez użytkownika punktem początkowym i końcowym (tutaj: punkt początkowy o
# współrzędnych 2,2 i końcowy o współrzędnych 5,4 zaznaczono dla ułatwienia podkreśleniem)
# istnieje droga. W powyższej tablicy droga taka istnieje i została oznaczona pogrubioną czcionką.
# Zadanie polega na opracowaniu algorytmu i zaimplementowaniu go w języku Python.

m = int(input("Write a number of rows: "))
n = int(input("Write a number of columns: "))

table = [[int(input(f"T[{i}][{j}]=")) for j in range(n)] for i in range(m)]

# for i in table:
#     print('\t'.join(map(str, i)))

# m = 5
# n = 6
#
# table = [
#     [1, 1, 1, 0, 1, 0],
#     [0, 1, 1, 1, 0, 1],
#     [1, 1, 0, 0, 0, 1],
#     [0, 1, 1, 1, 0, 1],
#     [1, 0, 0, 1, 0, 1]
# ]

for i in table:
    print('\t'.join(map(str, i)))

start_x = int(input("Write x to start your trip: "))
start_y = int(input("Write y to start your trip: "))

finish_x = int(input("Write x to finish your trip: "))
finish_y = int(input("Write y to finish your trip: "))


def check_input(t: list[list[int]], x1: int, y1: int, x2: int, y2: int):
    p1_valid = is_point_valid(t, x1, y1)
    p2_valid = is_point_valid(t, x2, y2)
    if not p1_valid:
        print("Start error")
        raise ValueError("Start error")
    if not p2_valid:
        print("End error")
        raise ValueError("End error")
    if p1_valid and p2_valid:
        print("OK")


def is_point_valid(t: list[list[int]], x: int, y: int) -> bool:
    return t[y][x] != 0


check_input(table, start_x, start_y, finish_x, finish_y)


def is_path(arr, x1, x2, y1, y2):
    # directions
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # queue
    # insert the start point.
    q = [(y1, x1)]

    # until queue is empty
    while len(q) > 0:
        p = q[0]
        q.pop(0)

        # mark as visited
        arr[p[0]][p[1]] = 0

        # destination is reached.
        if p == (y2, x2):
            return True

        # check all four directions
        for i in range(4):

            # using the direction array
            a = p[0] + directions[i][0]
            b = p[1] + directions[i][1]

            # not blocked and valid
            if (
                    len(arr) > a >= 0 != arr[a][b] and
                    0 <= b < len(arr[0])
            ):
                q.append((a, b))
    return False


print(is_path(table, start_x, finish_x, start_y, finish_y))
