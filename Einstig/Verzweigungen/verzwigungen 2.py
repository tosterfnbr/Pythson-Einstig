

#aufgabe 1 hundejahr
from random import randint

print("Aufgabe 1")
alter = int(input("Welches alter hat der Hund?\n"))
if alter == 1:
    print("Ein 1 jähriger Hund entspricht in etwa einem 14-jährigen Menschen")
elif alter == 2:
    print("Ein 2 jähriger Hund entspricht in etwa einem 22-jährigen Menschen")
else:
    print("Ein", alter, "jähriger Hund entspricht in etwa einem ", (alter - 2) * 5 + 22, "-jährigen Menschen")



#aufgabe 2 tipp aufgabe
print("Aufgabe 2")
t1 = randint(0, 15)
t2 = randint(0, 15)
tt1 = int(input("Was glaubst du wie viele punkte macht das 1 Team?"))
tt2 = int(input("Und das 2 Team?"))
if t1 == t2 and tt1 == tt2:
    if t1 == tt1 and t2 == tt2:
        print("Ergebnis: ", t1, ":", t2, "Tipp ", tt1, ":", tt2, " -> Punkte 3")
    else:
        print("Ergebnis: ", t1, ":", t2, "Tipp ", tt1, ":", tt2, " -> Punkte 1")

if t1 <= t2 and tt1 <= tt2:
    if t1 == tt1 and t2 == tt2:
        print("Ergebnis: ", t1, ":", t2, "Tipp ", tt1, ":", tt2, " -> Punkte 3")
    else:
        print("Ergebnis: ", t1, ":", t2, "Tipp ", tt1, ":", tt2, " -> Punkte 1")

if t1 >= t2 and tt1 >= tt2:
    if t1 == tt1 and t2 == tt2:
        print("Ergebnis: ", t1, ":", t2, "Tipp ", tt1, ":", tt2, " -> Punkte 3")
    else:
        print("Ergebnis: ", t1, ":", t2, "Tipp ", tt1, ":", tt2, " -> Punkte 1")

#aufgabe 3 Uhrzeitrechner


