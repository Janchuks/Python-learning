
f = open("demofi3le.txt", "w")
f.write("Personiga datora sastavdalas")

print("apskatīt vērtības")
#apskata
Veids = "RAM"
modelis = "Corsair Vengeance LPX 16GB"
cena = "99,99"
print("Veids: ",Veids)
print("Modelis: ",modelis)
print("Cena: ",cena)
#labo informāciju
print("Mainīt vērtības")

jVeids = input("Veids: ")
jModelis = input("Modelis: ")
jcena = input("Cena: ")
print("Jaunās vērtības")
print("Veids: ",jVeids)
print("Modelis: ",jModelis)
print("Cena: ",jcena)
dati = "labdien"

f.write("Veids: ",dati)

f.close()