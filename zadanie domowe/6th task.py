# Z6.
# Silniowy system pozycyjny to pozycyjny zapis liczb naturalnych, w którym mnożniki dla kolejnych
# pozycji definiowane są przez silnie kolejnych liczb naturalnych
# (𝑥)! = (𝑥𝑛𝑥𝑛−1𝑥𝑛−2 ⋯ 𝑥2𝑥1
# ) = 𝑥𝑛 ∙ 𝑛! + 𝑥𝑛−1 ∙ (𝑛 − 1)! + ⋯ + 𝑥2 ∙ 2! + 𝑥1 ∙ 1!
# W systemie silniowym współczynnik 𝑥𝑖 , który odpowiada mnożnikowi 𝑖!, spełnia zależność 0 ≤ 𝑥𝑖 ≤𝑖.
# Zapis każdej liczby w silniowym systemie pozycyjnym jest jednoznaczny, tj. każdą liczbę naturalną
# można zapisać dokładnie i tylko w jeden sposób.
# Przykład zamiany liczby w zapisie silniowym na liczbę w zapisie dziesiętnym
# (1220)! = 1 ∙ 4! + 2 ∙ 3! + 2 ∙ 2! + 0 ∙ 1! = (40)10
# Zamiana zapisu liczby 𝑥 w systemie dziesiętnym na zapis liczby w systemie silniowym może
# przebiegać wg następującego algorytmu: szukamy największej liczby 𝑘, której silnia nie przekracza 𝑥.
# Pierwsza jej cyfra to wynik dzielenia całkowitego 𝑥 przez 𝑘!. Kolejne cyfry zapisu silniowego
# (zaczynając od cyfr najbardziej znaczących) otrzymujemy przez wyznaczanie wyników dzielenia
# liczby 𝑥 przez (𝑘 − 1)!, (𝑘 − 2)!,⋯, 2!, 1!.
# Po wyznaczeniu cyfry 𝑥𝑖, odpowiadającej współczynnikowi 𝑖!, zmniejszamy wartość 𝑥 o liczbę odpowiadającą cyfrze 𝑥𝑖, czyli 𝑥𝑖∙ 𝑖.
# Oznacza to, że 𝑥 przyjmuje wartość 𝑥 𝑚𝑜𝑑 𝑘!.
# Przykład zamiany liczby dziesiętnej 1548 na zapis silniowy𝒙 𝒌 𝒙 𝒅𝒊𝒗 𝒌! 𝒙 𝒎𝒐𝒅 𝒌!

# Zatem (1548)10 = (204200)!.
# Na podstawie powyższych rozważań napisz w języku Python program, który w zależności od decyji
# użytkownika zamienia liczbę w zapisie silniowym na liczbę dziesiętną albo liczbę dziesiętną na
# odpowiadającą jej liczbę w systemie silniowym.


# table = [[int(input(f"T[{i}][{j}]=")) for j in range(n)] for i in range(m)]


def fact(num: int):
    f = 1
    for i in range(1, num + 1):
        f = f * i
    return f


number = int(input("Write a decimal number: "))


def max_fact(num: int) -> int:
    for i in range(1, num):
        if fact(i) < num < fact(i + 1):
            return i


def factor(x: int) -> int:
    result = 0
    k_start = max_fact(x)
    for k in range(k_start, 0, -1):
        y = int(x % fact(k))
        d = x // fact(k)
        x = y
        result = 10 * result + d
    return result


print(factor(int(number)))


number_reverse = int(input("Write a factorial number: "))


def reverse_factorial(num: int) -> int:
    o = str(num)
    result = 0
    for k in range(len(o), 0, -1):
        d = int(o[-k])
        result += d * fact(k)
    return result


print(reverse_factorial(number_reverse))
