# Z4.
# Kod Graya, znany również pod nazwą kodu refleksyjnego lub odzwierciedlonego binarnie, jest formą
# kodowania binarnego, w którym dwie kolejne liczby różnią się od siebie tylko jednym bitem.
# Napisz w języku Python program, który przekształca kod binarny do kodu Graya i odwrotnie.

binary = input("Write a binary number: ")


def binary_to_gray(num: int) -> str:
    b4 = num // 1000
    b3 = num % 1000 // 100
    b2 = int(num % 100 / 10)
    b1 = int(num % 10)
    a4 = b4
    a3 = b4 ^ b3
    a2 = b3 ^ b2
    a1 = b2 ^ b1
    a = str(a4) + str(a3) + str(a2) + str(a1)
    # a = 1000 * a4 + 100 * a3 + 10 * a2 + a1
    return a



print("We are turning binary", str(binary), "into gray:", binary_to_gray(int(binary)))
gray = input("Write a gray number: ")


def gray_to_binary(num: int) -> str:
    b4 = num // 1000
    b3 = num % 1000 // 100
    b2 = int(num % 100 / 10)
    b1 = int(num % 10)
    a4 = b4
    a3 = a4 ^ b3
    a2 = a3 ^ b2
    a1 = a2 ^ b1
    a = str(a4) + str(a3) + str(a2) + str(a1)
    # a = 1000 * a4 + 100 * a3 + 10 * a2 + a1
    return a


print("We are turning gray", gray, "into binary:", gray_to_binary(int(gray)))

input()
