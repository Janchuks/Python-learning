import random#modulis

izveles = ["akmens", "šķēres", "papīrs"]
dators = random.choice(izveles)
while True:
    print("Vai vēlaties spēlēt akmens šķēres papīrīts?")
    atb = input("jā/nē: ")
    if atb == "jā":
        while True:
            try:
                print("izvēlies savu gājienu (akmens, šķēŗes vai papīrs)")
                gajiens=input()
                x = "akmens" in gajiens or "šķēres" in gajiens or "papīrs" in gajiens
                print("jūsu gājiens - ", gajiens)
                print("datora gājiens - ",dators)
                if gajiens==dators:
                    print("neizšķirts")
                if gajiens!=dators:
                    if dators=="akmens" and "šķēres" in gajiens:
                        print("jūs zaudējāt!")
                    elif dators=="šķēres" and "papīrs" in gajiens:
                        print("jūs zaudējāt!")
                    elif dators=="papīrs" and "akmens" in gajiens:
                        print("jūs zaudējāt!")
                    else:
                        print("jūs uzvarējāt!")
                            
                if not x:
                    print("ievadiji nepareizi")
                else:
                    break
                
            except :
                print("nav ok")
    else:
        print("ko tad tu te meklē?")
        break
           
           
              
           