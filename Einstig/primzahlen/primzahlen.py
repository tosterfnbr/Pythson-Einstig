
ANT = int(input("NENE MIR EINE ZAHL :"))

for Zahl in range(1, ANT):
    is_primz = True
    for ZUMTeilen in range(2, int(Zahl / 2) + 1):
        if Zahl % ZUMTeilen == 0 and ZUMTeilen < Zahl:
            is_primz = False
            break

    if is_primz:
        print(str(Zahl) + " ist eine Primzahl")

