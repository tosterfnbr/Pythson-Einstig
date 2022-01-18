password = input("Setze Dein Passwort:")
score = 0


lowercase = False
for character in password:
    if character in "abcdefghijklmnopqrstuvwxyz":
        lowercase = True

if lowercase == True:
    print("Your password contains lowercase characters.")
