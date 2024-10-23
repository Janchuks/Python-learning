Contacts = {
    "Jānis": "23995895",
    "Agnese": "7458734",
    "Inta": "32059495"
}
while True:
    action=input("ko vēlies darīt dzēst. pievienot kontaktu vai zvanīt, vai x-iziet ")
    if action=="dzēst" or action=="dzest":
        print (Contacts)
        Contacts.pop(input("kuru kontaktu dzēsīsi?: "))
        print (Contacts)
    elif action == "pievienot" or action == "Pievienot":
        vards=input("Ievadi jaunu Kontaktu: ")
        numurs=input("Ievadi jaunu nummuru:")
        Contacts[vards] = numurs
        print("Ievadīts veiksmīgi!")
        print(Contacts)
    elif action == "zvanīt" or action == "zvanit":
        print(Contacts)
        zvans = input("Kam zvanīsi? ")
        Contacts = {
            "Jānis": "23995895",
            "Agnese": "7458734",
            "Inta": "32059495"
        }

        print(Contacts[zvans],"zvanam", zvans)
    elif action == "x":
        print("bye bye!")
        break