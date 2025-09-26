primeiraNota = float(input("coloque sua nota: "))
segundaNota = float(input("coloque sua nota: "))
terceiraNota = float(input("coloque sua nota: "))
media = (primeiraNota + segundaNota + terceiraNota )/ 3
if media < 5:
    print("reprovada")
elif media < 10:
    print("aprovada")
else:
    print("aprovada com merito")
