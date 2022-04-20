# Z2.
# Napisz w języku Python program, który w zależności od decyzji użytkownika sprawdza, czy dana
# liczba jest obfita albo wyświetli liczby obfite z zakresu podanego przez użytkownika oraz obliczy ich
# obfitość. Liczba obfita jest liczbą, dla której suma jej dzielników właściwych jest większa od niej
# samej. Wartość, o jaką suma dzielników przekracza liczbę, nazywamy obfitością. Na przykład liczba
# 12 jest liczbą obfitą, bo suma jej dzielników właściwych wynosi 1 + 2 + 3 + 4 + 6 = 16, a jej
# obfitość wynosi 16 − 12 = 4.

n = int(input("Write a number: "))


def divs(num: int):
    sum = 0
    for i in range(1, num, 1):
        if num % i == 0:
            sum += i
    return sum


def dif(numb: int, func: int):

    if numb < func:
        diff = func - numb
        return diff
    else:
        return 0

if dif(int(n), int(divs(int(n)))) > 0:
    print("Liczba ", n, " jest obfita.", " A jej obfitość jest ", dif(int(n), int(divs(int(n)))))


a = input()
b = input()

def range_num(a: int, b: int):
    for i in range(a, b+1):
        if dif(i, divs(i)) > 0:
            print("Liczba ", i, " jest obfita.", " A jej obfitość jest ", dif(i, divs(i)))
        else:
            print("Liczba ", i, " nie jest obfita.")

range_num( int(a), int(b))


input()
