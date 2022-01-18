import math

day = input("Gebe deinen tag :")
moth = input("gebe deine monat :")
jahr = input("Gebe deinen jahr :")

w = ((int(day) + (2.6 * ((int(moth) + 9) % 12 + 1) - 0.2) + int(jahr) % 100 + (int(jahr) % 100 / 4) + (
        int(jahr) / 400) - 2 * (int(jahr) / 100) - 1) % 7 + 7) % 7 + 1;

w = math.floor(w)

def jahr(year):
    if year % 400 == 0:

        return True
    else:
        if year % 4 == 0:
            if year % 100 == 0:
                return False

            else:
                return True
        else:
            return False
while True:

    if int(moth) >= 13 or int(day) >= 32:

        print("deine angabe ist leider nicht koregt")
        moth = input("gebe deine monat :")
        day = input("Gebe deinen tag :")

    if w == 0:
            print("sonntag")
            quit()

    if w == 1:
            print("montag")
            quit()

    if w == 2:
            print("dinstag")
            quit()

    if w == 3:
            print("mittwoch")
            quit()

    if w == 4:
            print("donnerstag")
            quit()
    if w == 5:
            print("freitag")
            quit()
    if w == 6:
             print("sammtag")
             quit()




