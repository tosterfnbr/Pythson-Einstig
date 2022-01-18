var= input("wer das liest ist ein hund: ")



while 9 != len(var):

    var = input("Hier bitte die ISBN Nummer angeben: ")

isbn9 = int(var)

z9 = isbn9 % 10

z8 = isbn9 % 100 // 10

z7 = isbn9 % 1000 // 100

z6 = isbn9 % 10000 // 1000

z5 = isbn9 % 100000 // 10000

z4 = isbn9 % 1000000 // 100000

z3 = isbn9 % 10000000 // 1000000

z2 = isbn9 % 100000000 // 10000000

z1 = isbn9 % 1000000000 // 100000000


s = 1 * z1 + 2 * z2 + 3 * z3 + 4 * z4 + 5 * z5 + 6 * z6 + 7 * z7 + 8 * z8 + 9 * z9

r = s % 11

