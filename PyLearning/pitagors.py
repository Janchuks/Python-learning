import math
print("Pitagora teorēma")
print("Kuru vērtību vēlaties aprēķināt?(a,b,c)")
izv=input("a,b vai c: ");
if (izv == "c") :
    print("Lai aiprēķinātu hipotenūzu ievadīet malas")
    a=int(input("Mala a:"))
    b=int(input("Mala b:"))
    kvadra= float (a*a)
    kvadrb= float (b*b)
    print (math.sqrt(kvadra+kvadrb), "hipotenūza")
if (izv == "a") :
    print("Lai aprēķinātu malu a ievadiet malas")
    b=int(input("Mala b:"))
    c=int(input("Mala c:"))
    kvadrb= float (b*b)
    kvadrc= float (c*c)
    print (math.sqrt(kvadrc-kvadrb), "mala a")

if (izv == "b") :
    print("Lai aprēķinātu malu b ievadiet malas")
    a=int(input("Mala a:"))
    c=int(input("Mala c:"))
    kvadra= float (a*a)
    kvadrc= float (c*c)
    print (math.sqrt(kvadrc-kvadra), "mala b")
print("Paldies!")

