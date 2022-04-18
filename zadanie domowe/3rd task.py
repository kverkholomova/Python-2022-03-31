# Z3.
# Liczbę naturalną nazywamy osiągalną, jeżeli istnieje takie 𝑘, że 𝑛 = 𝑘 + 𝑠(𝑘), gdzie 𝑘 jest liczbą
# naturalną, a 𝑠(𝑘) jest sumą cyfr liczby 𝑘 w zapisie dziesiętnym. Przykładowo, liczba 𝑛 = 28 jest
# osiągalna, ponieważ istnieje 𝑘 = 23, w której 𝑠(𝑘) = 5, zaś 23 + 5 = 28. Podobnie osiągalną liczbą
# jest 𝑛 = 505, bo istnieje takie 𝑘 = 491 oraz 𝑠(𝑘) = 14, że 491 + 14 = 505. Natomiast np. liczby
# 20 i 31 nie są osiągalne. Na podstawie powyższych informacji napisz program w języku Python, który
# w zależności od decyzji użytkownika sprawdza, czy podana przez użytkownika liczba z przedziału
# [10; 9999] jest osiągalna albo generuje wszystkie liczby osiągalne z tego zakresu .


n = input()


def reachable_number(num: int):
    if int(num / 100) == 0:
        for k in range(1, num):
            k1 = int(k / 10)
            k2 = k % 10
            if k + (int(k1) + k2) == num:
                return num #and k

    elif int(num / 1000) == 0:
        for k in range(1, num):
            k1 = int(k / 100)
            k2 = int(k % 100 / 10)
            k3 = k % 10
            if k + (int(k1) + int(k2) + k3) == num:
                return num #and k

    else:
        for k in range(1, num):
            k1 = int(k / 1000)
            k2 = int(k % 1000 / 100)
            k3 = k % 100 / 1028
            k4 = k % 10
            if k + (int(k1) + int(k2) + int(k3) + k4) ==  num:
                return num #and k


print(reachable_number(int(n)))

for i in range(10, 9999):
    print(reachable_number(int(i)))

input()
