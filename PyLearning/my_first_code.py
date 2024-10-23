import math

while True:    
    atb = input("Vai vēlies izmantot Pitagora teorēmu? (jā/nē): ")

    if atb == "jā":
        aprekini = input("Ievadi, kuru malu vēlies aprēķināt trijstūrim: ")
        if aprekini == "c":
            while True:
                print("Lai aprēķinātu malu c, ievadi malu a un b!")
                try:
                    a = float(input("Ievadi malu a: "))    
                    b = float(input("Ievadi malu b: "))
                    squareb = a ** 2                       
                    squarec = b ** 2                 
                    print(math.sqrt(squareb + squarec))   
                    break

                except ValueError:                       
                    print("Ievadi skaitli!")
        elif aprekini == "a":                          
            print("Lai aprēķinātu malu a, ievadi malu b un c!")
            try:
                b = float(input("Ievadi malu b: "))
                c = float(input("Ievadi malu c: "))
                squareb = b ** 2
                squarec = c ** 2 
                print(math.sqrt(squarec - squareb))
            except ValueError:
                print("Ievadi skaitli!")

        elif aprekini == "b":
            try:
                print("Lai aprēķinātu malu b, ievadi malu a un c!")
                a = float(input("Ievadi malu a: "))
                c = float(input("Ievadi malu c: "))
                squarea = a ** 2
                squarec = c ** 2 
                print(math.sqrt(squarec - squarea))
            except ValueError:
                print("Ievadi skaitli!")

        elif aprekini == "pabeidzu":      
            print("Uz drīzu tikšanos!")
            break

        else:                            
            print("Ievadi a, b vai c!")

    elif atb == "nē":
        print("Varbūt kādu citu reizi! :)")
        break                             

    else:
        print("Ievadi jā vai nē!")