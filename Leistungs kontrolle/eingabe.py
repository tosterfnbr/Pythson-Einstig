









moth = input("gebe deine monat :")
day = input("Gebe deinen tag :")
jahr = input("Gebe deinen jahr :")
while True:
    if not moth.isdecimal() or not day.isdecimal():
        print("Deine angabe wahr leider nicht als zahl geschrieben gebe mir bitte noch mal deine werte,aber diese mal als zahl")
        moth = input("gebe deine monat als zahl ein  :")
        day = input("Gebe deinen tag als zahl ein  :")

    elif int(moth) >= 13 or int(day) >= 32:

       print("deine angabe ist leider nicht koregt")
       moth = input("gebe deine monat :")
       day = input("Gebe deinen tag :")


    else:
        print("deine angaben sind koregt")
        quit()