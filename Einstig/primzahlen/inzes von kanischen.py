wert = int(input("Wie Viele hasen wilst den inces haben : "))
a= 1
b= 0
while wert != 0:
    print (b, end=" ")
    a, b = b, a+b
    wert -= 1