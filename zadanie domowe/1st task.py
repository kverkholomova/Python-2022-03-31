# Z1.
# Napisz w języku Python program, który w zależności od decyzji użytkownika sprawdza, czy dana
# liczba trzycyfrowa jest liczbą Armstronga albo wypisuje wszystkie liczby Armstronga zawierające trzy
# cyfry (wersja trudniejsza). Liczba Armstronga, zwana również liczbą narcystyczną, to liczba, która
# jest sumą swoich cyfr podniesionych do potęgi równej ich liczbie. Przykładowo, najmniejsza liczba
# Armstronga to 153, która jest równa 1^3+5^3+3^3

def ppdi(num: int):
    a = int(num / 100)
    b = int(num % 100 / 10)
    c = int(num % 10)
    if (a * a * a + b * b * b + c * c * c) == num:
        return num
    else:
        return False


n = int(input("Write a number to check if it is a Armstrong number: "))

print(ppdi(int(n)), "jest liczbą Armstronga")

for i in range(100, 1000):

        if ppdi(i):
            print(i, "jest liczbą Armstronga")



input()
