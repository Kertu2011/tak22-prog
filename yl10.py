username = input("Sisesta kasutajanimi:")
print("Tere " + username)

liv = input("Sisesta oma elukoht:")
if liv == "Saaremaa":
    print("Saaremaa on ilus")

age = int(input("Sisesta oma vanus:"))
if age < 18:
    print("Oled liiga noor, et autot juhtida")
elif age == 18:
    print("Palju õnne 18 saamise puhul")
else:
    print("Oled piisavalt vana, et autot juhtida")