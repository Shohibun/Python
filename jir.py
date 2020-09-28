class Hero:
    def __init__(self, name, health, attack_power, armor_defence):
        self.name = name 
        self.health = health
        self.attack_power = attack_power
        self.armor_defence = armor_defence

    def Menyerang(self, lawan):
        print(self.name + " Menyerang " + lawan.name)
        lawan.diserang(self, self.attack_power)
    
    def diserang(self, lawan, attack_power_lawan):
        print(self.name + " Diserang " + lawan.name)
        attack_diterima = attack_power_lawan - self.armor_defence
        print("Serangan terasa : " + str(attack_diterima))
        self.health -= attack_diterima
        print("Darah " + self.name + " tersisa " + str(self.health))

seshomaru = Hero("Seshomaru", 1000, 40, 50)
inuyasha = Hero("Inuyasha", 800, 90, 20)

seshomaru.Menyerang(inuyasha)
print("\n")
inuyasha.Menyerang(seshomaru)
def Menyerang(self, lawan):
    
if __name__ == "__main__":
    def Menyerang(self, lawan):
    