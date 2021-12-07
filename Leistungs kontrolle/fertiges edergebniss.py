import math




moth = input("gebe deine monat :")
day = input("Gebe deinen tag :")
jahr = input("Gebe deinen jahr :")


w = ((int(day)+ (2.6 * ((int(moth) + 9) % 12 + 1) - 0.2) + int(jahr) % 100 + (int(jahr) % 100 / 4) + (int(jahr)/ 400) - 2 * (int(jahr) / 100) - 1) % 7 + 7) % 7 + 1;

w= math.floor(w)

print(w)
quit()

if w == 0:
    print("sonntag")
    w + 1
    if w == 1:
        print("montag")
        w + 1
    if w == 2:
        print("dinstag")
        w + 1
    if w == 3:
        print("mittwoch")
        w + 1

    if w == 4:
        print("donnerstag")
        w + 1

    if w == 5:
        print("freitag")
        w + 1

    if w == 6:
        print("sammtag")
        w + 1


