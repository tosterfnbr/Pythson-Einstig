






import math




moth = input("gebe deine monat :")
day = input("Gebe deinen tag :")
jahr = input("Gebe deinen jahr :")


w = ((int(day)+ (2.6 * ((int(moth) + 9) % 12 + 1) - 0.2) + int(jahr) % 100 + (int(jahr) % 100 / 4) + (int(jahr)/ 400) - 2 * math.floor(int(jahr) / 100) - 1) % 7 + 7) % 7 + 1;
print()
quit()