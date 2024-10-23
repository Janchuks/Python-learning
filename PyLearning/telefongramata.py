

names = ["jančuks", "Samie", "Kitija", "Nikola", "munai"]
phone_numbers = [234543555, 234345355, 252345355, 278878789, 25988497]
for i in range(5): 
    print(names[i]+":",phone_numbers[i])
while True:
    print("kam vēlaties zvanīt?(skaitlis)")
    zvans=int(input("1- Jānis, 2- Pēreris, 3- Agnese 0- iziet!"))
    telefomgramata = {
    1: 395090,
    2: 9395395,
    3: 28490834 
    }
    if zvans ==0:
        print("bye bye!")
        break
    print(telefomgramata[zvans],"Zvanam")


