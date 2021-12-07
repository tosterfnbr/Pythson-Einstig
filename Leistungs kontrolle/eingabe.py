




import math




moth = input("gebe deine monat :")
day = input("Gebe deinen tag :")
jahr = input("Gebe deinen jahr :")

w = ((int(day) + (2.6 * ((int(moth) + 9) % 12 + 1) - 0.2) + int(jahr) % 100 + (int(jahr) % 100 / 4) + (
        int(jahr) / 400) - 2 * (int(jahr) / 100) - 1) % 7 + 7) % 7 + 1;

w = math.floor(w)


while True:
    if not moth.isdecimal() or not day.isdecimal():
        print("Deine angabe wahr leider nicht als zahl geschrieben gebe mir bitte noch mal deine werte,aber diese mal als zahl")
        moth = input("gebe deine monat als zahl ein  :")
        day = input("Gebe deinen tag als zahl ein  :")

    elif int(moth) >= 13 or int(day) >= 32:

       print("deine angabe ist leider nicht koregt")
       moth = input("gebe deine monat :")
       day = input("Gebe deinen tag :")

    elif w == 0:
            print("sonntag")
            w + 1
            quit()

    elif w == 1:
            print("montag")
            w + 1
            quit()

    elif w == 2:
            print("dinstag")
            w + 1
            quit()

    elif w == 3:
            print("mittwoch")
            w + 1
            quit()

    elif w == 4:
            print("donnerstag")
            w + 1
            quit()
    elif w == 5:
            print("freitag")
            w + 1
            quit()
    elif w == 6:
             print("sammtag")
             w + 1
             quit()











