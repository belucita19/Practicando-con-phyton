name = input("¿Cómo te llamas? ")
gender = input("¿cuál es tu sexo (M o H)? ")
if gender == "M":
 if name.lower() < "m":
        group ="A"
 else:
      group ="B"
else:
 if name.lower() > "n":
      group ="A"
 else:
     group = "B"
 print("Tu grupo es " + group)
