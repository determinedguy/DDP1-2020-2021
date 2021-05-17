# Lab 9: Fantasi Terakhir
# Program ini dibuat oleh Muhammad Athallah (2020)

class Hero():
    def __init__(self, name, hp, attack):
        """
        Constructor untuk class Hero
        """
        self.__name = name
        self.__hp = hp
        self.__attack = attack

    # Getter
    def get_name(self):
        """
        Getter untuk atribut name
        """
        return self.__name

    def get_hp(self):
        """
        Getter untuk atribut hp
        """
        return self.__hp

    def get_attack(self):
        """
        Getter untuk atribut attack
        """
        return self.__attack

    # Setter
    def set_hp(self, hp):
        """
        Setter untuk atribut hp
        """
        if hp < 0:
            self.__hp = 0
        else:
            self.__hp = hp

    def attack(self, other):
        """
        Method untuk menyerang lawan
        """
        other.damaged(self.get_attack())

    def damaged(self, attack):
        """
        Method untuk mengubah status apabila diserang lawan
        """
        self.set_hp(self.get_hp() - attack)

    def is_alive(self):
        """
        Method untuk mengecek hp
        """
        if self.get_hp() == 0:
            return False
        else:
            return True

    def __str__(self):
        """
        Method untuk mengembalikan representasi String
        """
        return f"{self.get_name():20s}| {'HERO':10s}| {self.get_hp():5d}"


class Support(Hero):
    def __init__(self, name, hp, attack, heal_amount = 20):
        """
        Constructor untuk class Support
        """
        super().__init__(name, hp, attack)
        self.__heal_amount = heal_amount

    def get_heal_amount(self):
        """
        Getter untuk atribut heal_amount
        """
        return self.__heal_amount

    def heal(self, other):
        """
        Method untuk menambah hp hero lain
        """
        other.set_hp(other.get_hp() + self.get_heal_amount())

    def __str__(self):
        """
        Method untuk mengembalikan representasi String
        """
        return f"{self.get_name():20s}| {'Support':10s}| {self.get_hp():5d}"

    def __add__(self, other):
        """
        Method untuk melakukan operator overloading (+)
        """
        # Gabungkan data kedua karakter
        name = self.get_name() + '_' + other.get_name()
        hp = self.get_hp() + other.get_hp()
        attack = self.get_attack() + other.get_attack()
        heal_amount = self.get_heal_amount() + other.get_heal_amount()
        # Return dengan inisiasi karakter baru dengan kelas yang sama
        return Support(name, hp, attack, heal_amount)


class Warrior(Hero):
    def __init__(self, name, hp, attack, extra_attack = 20):
        """
        Constructor untuk class Warrior
        """
        super().__init__(name, hp, attack)
        self.__extra_attack = extra_attack

    def get_extra_attack(self):
        """
        Getter untuk atribut extra_attack
        """
        return self.__extra_attack
    
    def attack(self, other):
        """
        Method untuk menyerang lawan 
        """
        # Attack = Attack + Extra Attack
        other.damaged(self.get_attack() + self.get_extra_attack())

    def __str__(self):
        """
        Method untuk mengembalikan representasi String
        """
        return f"{self.get_name():20s}| {'Warrior':10s}| {self.get_hp():5d}"

    def __add__(self, other):
        """
        Method untuk melakukan operator overloading (+)
        """
        # Gabungkan data kedua karakter
        name = self.get_name() + '_' + other.get_name()
        hp = self.get_hp() + other.get_hp()
        attack = self.get_attack() + other.get_attack()
        extra_attack = self.get_extra_attack() + other.get_extra_attack()
        # Return dengan inisiasi karakter baru dengan kelas yang sama
        return Warrior(name, hp, attack, extra_attack)


class Tank(Hero):
    def __init__(self, name, hp, attack, shield = 20):
        """
        Constructor untuk class Tank
        """
        super().__init__(name, hp, attack)
        self.__shield = shield

    def get_shield(self):
        """
        Getter untuk atribut shield
        """
        return self.__shield

    def set_shield(self, shield):
        """
        Setter untuk atribut shield
        """
        # Jika hasil pengurangan shield masih positif
        if shield > 0:
            self.__shield = shield
        # Jika tidak, "habiskan" shield dan berikan sisa damage kepada HP
        else:
            self.__shield = 0
            self.set_hp(self.get_hp() + shield)

    def damaged(self, attack):
        """
        Method untuk mengubah status apabila diserang lawan
        """
        # Jika shield masih ada
        if self.get_shield() > 0:
            self.set_shield(self.get_shield() - attack)
        # Jika tidak, alihkan damage ke HP
        else:
            self.set_hp(self.get_hp() - attack)

    def __str__(self):
        """
        Method untuk mengembalikan representasi String
        """
        return f"{self.get_name():20s}| {'Tank':10s}| {self.get_hp():5d}"

    def __add__(self, other):
        """
        Method untuk melakukan operator overloading (+)
        """
        # Gabungkan data kedua karakter
        name = self.get_name() + '_' + other.get_name()
        hp = self.get_hp() + other.get_hp()
        attack = self.get_attack() + other.get_attack()
        shield = self.get_shield() + other.get_shield()
        # Return dengan inisiasi karakter baru dengan kelas yang sama
        return Tank(name, hp, attack, shield)

# NOTE: method main() & get_hero() tidak perlu diubah


def get_hero(name, list_hero):
    """
    Method untuk mengembalikan hero dengan name sesuai parameter
    """
    for hero in list_hero:
        if hero.get_name() == name:
            return hero


def main():
    list_hero = []

    banyak_hero = int(input("Masukkan jumlah hero : "))

    for i in range(banyak_hero):
        input_hero = input("Masukkan detail hero : ")
        detail_hero = input_hero.split()
        tipe = detail_hero[0]
        nama = detail_hero[1]
        hp = int(detail_hero[2])
        attack = int(detail_hero[3])
        atribut_tambahan = detail_hero[4]
        if tipe == "SUPPORT":
            if atribut_tambahan != "DEFAULT":
                list_hero.append(
                    Support(nama, hp, attack, int(atribut_tambahan)))
            else:
                list_hero.append(Support(nama, hp, attack))
        elif tipe == "WARRIOR":
            if atribut_tambahan != "DEFAULT":
                list_hero.append(
                    Warrior(nama, hp, attack, int(atribut_tambahan)))
            else:
                list_hero.append(Warrior(nama, hp, attack))
        elif tipe == "TANK":
            if atribut_tambahan != "DEFAULT":
                list_hero.append(Tank(nama, hp, attack, int(atribut_tambahan)))
            else:
                list_hero.append(Tank(nama, hp, attack))

    perintah = input("Masukkan perintah : ")
    list_perintah = perintah.split()
    while list_perintah[0] != "EXIT":
        if list_perintah[0] == "ATTACK":
            karakter1 = get_hero(list_perintah[1], list_hero)
            karakter2 = get_hero(list_perintah[2], list_hero)
            if (karakter1 != None and karakter2 != None):
                karakter1.attack(karakter2)
                if not karakter2.is_alive():
                    list_hero.remove(karakter2)
                print(f"{karakter1.get_name()} berhasil menyerang {karakter2.get_name()}")
                print(f"Nyawa {karakter2.get_name()} tersisa {karakter2.get_hp()}")
            else:
                print("Karakter tidak ditemukan")

        elif list_perintah[0] == "HEAL":
            karakter1 = get_hero(list_perintah[1], list_hero)
            karakter2 = get_hero(list_perintah[2], list_hero)
            if (karakter1 != None and karakter2 != None):
                if isinstance(karakter1, Support):
                    if karakter1 != karakter2:
                        karakter1.heal(karakter2)
                        print(f"{karakter1.get_name()} berhasil meng-heal {karakter2.get_name()}")
                        print(f"Nyawa {karakter2.get_name()} menjadi {karakter2.get_hp()}")
                    else:
                        print(f"{karakter1.get_name()} tidak dapat meng-heal dirinya sendiri")
                else:
                    print(f"{karakter1.get_name()} bukan merupakan Support")
            else:
                print("Karakter tidak ditemukan")

        elif list_perintah[0] == "GABUNGKAN":
            karakter1 = get_hero(list_perintah[1], list_hero)
            karakter2 = get_hero(list_perintah[2], list_hero)
            if type(karakter1) == type(karakter2):
                if (karakter1 != None and karakter2 != None):
                    combined_hero = karakter1 + karakter2
                    print(f"{karakter1.get_name()} berhasil bergabung dengan {karakter2.get_name()}", end=" ")
                    print(f"menjadi {combined_hero.get_name()}")
                    list_hero.remove(karakter1)
                    list_hero.remove(karakter2)
                    list_hero.append(combined_hero)
                else:
                    print("Karakter tidak ditemukan")
            else:
                print("Gagal menggabungkan karena tipe kedua karakter berbeda")

        perintah = input("Masukkan perintah : ")
        list_perintah = perintah.split()

    print("\nKarakter yang masih hidup:")
    print("-"*40)
    print("Nama                | Tipe      | HP   ")
    print("-"*40)
    for hero in list_hero:
        print(hero)


if __name__ == "__main__":
    main()
