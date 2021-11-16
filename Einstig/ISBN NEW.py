

var = input("Bitte Geben sie uns ihre Nummer : ")



while 9 != len(var):

    var = input("Hier bitte die ISBN Nummer angeben: ")


ISBN_9 = int(var)

x9 = ISBN_9 % 10

x8 = ISBN_9 % 100 // 10

x7 = ISBN_9 % 1000 // 100

x6 = ISBN_9 % 10000 // 1000

x5 = ISBN_9 % 100000 // 10000

x4 = ISBN_9 % 1000000 // 100000

x3 = ISBN_9 % 10000000 // 1000000

x2 = ISBN_9 % 100000000 // 10000000

x1 = ISBN_9 % 1000000000 // 100000000

print("Die ISBN ist", x1, x2, x3, x4, x5, x6, x7, x8, x9)

s = 1 * x1 + 2 * x2 + 3 * x3 + 4 * x4 + 5 * x5 + 6 * x6 + 7 * x7 + 8 * x8 + 9 * x9

r = s % 11

print("Die prüff ziffer ist", r)

print("Die ISBN ist", x1, x2, x3, x4, x5, x6, x7, x8, x9, r)
