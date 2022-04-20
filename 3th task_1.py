# Z3.
# Liczbę naturalną nazywamy osiągalną, jeżeli istnieje takie 𝑘, że 𝑛 = 𝑘 + 𝑠(𝑘), gdzie 𝑘 jest liczbą
# naturalną, a 𝑠(𝑘) jest sumą cyfr liczby 𝑘 w zapisie dziesiętnym. Przykładowo, liczba 𝑛 = 28 jest
# osiągalna, ponieważ istnieje 𝑘 = 23, w której 𝑠(𝑘) = 5, zaś 23 + 5 = 28. Podobnie osiągalną liczbą
# jest 𝑛 = 505, bo istnieje takie 𝑘 = 491 oraz 𝑠(𝑘) = 14, że 491 + 14 = 505. Natomiast np. liczby
# 20 i 31 nie są osiągalne. Na podstawie powyższych informacji napisz program w języku Python, który
# w zależności od decyzji użytkownika sprawdza, czy podana przez użytkownika liczba z przedziału
# [10; 9999] jest osiągalna albo generuje wszystkie liczby osiągalne z tego zakresu .

n = input('n=')


def is_reachable_number(num: int):
    for k in range(1, num):
        sum_of_numbers = sum([int(digit) for digit in str(k)])
        if k + sum_of_numbers == num:
            print(f'{num} = {k} + {sum_of_numbers}')
            return True
    print(f'{num} IS NOT')
    return False


print(is_reachable_number(int(n)))

for i in range(10, 9999):
    if is_reachable_number(i):
        pass
        # print(i)

input()
