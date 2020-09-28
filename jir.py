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
        print("Darah " + self.name + " tersisa \n\n" + str(self.health))
    
if __name__ == "__main__":
    # jalannya program sebaiknya dijalankan setelah main()
    seshomaru = Hero("Seshomaru", 1000, 40, 50)
    inuyasha = Hero("Inuyasha", 800, 90, 20)

    # pertarungan tanpa henti, dimulai!!!
    while True:
        seshomaru.Menyerang(inuyasha)
        inuyasha.Menyerang(seshomaru)
