primeiraNota = float(input("coloque sua nota: "))
segundaNota = float(input("coloque sua nota: "))
terceiraNota = float(input("coloque sua nota: "))
media = (primeiraNota + segundaNota + terceiraNota + quartaNota + quintaNota)/ 5
if media < 6:
    print("aprovada F")
elif media < 7:
    print("aprovada D ")
elif media < 8:
    print("aprovada C")
elif media < 9:
    print("reprovada B")
else:
    print("aprovada A")
