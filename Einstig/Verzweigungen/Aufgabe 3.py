a = 1
while a == 1:
    year = int(input("schaltjahr"))
    if year % 400 == 0:
        print("es handel sich jetzt um ein schaltjahr ")
    if year % 4 == 0:
        if  year % 100 == 0:

            print("es ist kein schalt jahr")
        else:
            print("es ist ein schalt jahr")

    else: print("es ist ein normales jahr")

