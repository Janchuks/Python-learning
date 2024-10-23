
vards = input("kā tevi sauc? ")
emotion = input("kā tu juties ")
energy=100
class Cilveks:
    #kopigas
    hot_stuff = True 
    legs = 2
    def __init__(self, name, emotions, energy):
        self.emotions = emotions
        self.name=name
        self.energy = energy
    
    def skriet(self):
        usr = input("iesi skiret?")
        if usr == "yes" or usr == "jā":
            self.energy -=50
            print("Tev maz enerģija:", self.energy)
        else:
            print("Tu neesi skrējis. Enerģija:", self.energy)
    def gulet(self):
        print("Tu tagad gulēsi.")
        if self.energy ==100:
            self.energy =100
        else:
            self.energy += 30
        print("Tava enerģija:", self.energy)

    def introduce(self):
        print("hey, nice to meet",self.name)


vards = Cilveks(vards,emotion, energy)
vards.introduce()

vards.skriet()
vards.gulet()
print("jūtas",vards.emotions,"cilvēks",vards.name)
