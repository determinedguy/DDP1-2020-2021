# Lab 8: Dampak Pemrograman Berbasis Objek
# Dibuat oleh Muhammad Athallah (2020)
# Dibuat berdasarkan file template

class Anemo:
    def __init__(self, name, hp, atk, em):
        ## TODO
        # Lengkapi constructor ini
        self.name = name
        self.atk = atk
        self.hp = hp
        self.em = em
    
    def attack(self, other):
        ## TODO
        # Implementasikan attack
        other.hp -= self.atk
    
    def elemental_skill(self, other):
        ## TODO
        # Implementasikan reaksi elemen
        if not isinstance(other, Anemo) and self.em > other.em:
            other.hp -= self.em + other.em
    
    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        ## TODO
        # Implementasikan cetak
        res = f"{self.name:20}| {self.hp:<5}"
        return res
        

class Pyro:
    def __init__(self, name, hp, atk, em):
        ## TODO
        # Lengkapi constructor ini
        self.name = name
        self.atk = atk
        self.hp = hp
        self.em = em

    def attack(self, other):
        ## TODO
        # Implementasikan attack
        other.hp -= self.atk

    def elemental_skill(self, other):
        ## TODO
        # Implementasikan reaksi elemen
        if self.em > other.em:
            if isinstance(other, Anemo):
                other.hp -= self.em + other.em
            elif isinstance(other, Hydro):
                other.hp -= int(1.5 * self.em)
    
    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        ## TODO
        # Implementasikan cetak
        res = f"{self.name:20}| {self.hp:<5}"
        return res


class Hydro:
    def __init__(self, name, hp, atk, em):
        ## TODO
        # Lengkapi constructor ini
        self.name = name
        self.atk = atk
        self.hp = hp
        self.em = em

    def attack(self, other):
        ## TODO
        # Implementasikan attack
        other.hp -= self.atk

    def elemental_skill(self, other):
        ## TODO
        # Implementasikan reaksi elemen
        if self.em > other.em:
            if isinstance(other, Anemo):
                other.hp -= self.em + other.em
            elif isinstance(other, Pyro):
                other.hp -= (2 * self.em)

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        ## TODO
        # Implementasikan cetak
        res = f"{self.name:20}| {self.hp:<5}"
        return res


def main():
    ## TODO
    # Lengkapi implementasi penambahan karakter!

    # Implementasi daftar karakter menggunakan dict
    characters = {}

    # Membuat variabel sebagai wadah masukan
    input_character = input("Masukkan karakter: ")

    while input_character:
        name, vision, hp, atk, em = input_character.split()
        hp, atk, em = int(hp), int(atk), int(em)

        if vision == 'Anemo':
            characters[name] = Anemo(name, hp, atk, em)
        elif vision == 'Pyro':
            characters[name] = Pyro(name, hp, atk, em)
        elif vision == 'Hydro':
            characters[name] = Hydro(name, hp, atk, em)
        else:
            print(f"[ERROR] {vision}: Vision tidak valid")
        input_character = input("Masukkan karakter: ")

    # Mencetak interaksi yang dilakukan
    inp = input("\nKarakter yang berinteraksi: ")   
    while inp != "":
        name1, name2 = inp.split()
        char1 = characters[name1]
        char2 = characters[name2]

        if char1.is_alive() and char2.is_alive():
            char1.attack(char2)
            print(f"{char1.name} menyerang {char2.name} sebesar {char1.atk}")
        else:
            if not char1.is_alive():
                print(f"{char1.name} sudah mati.")
            elif not char2.is_alive():
                print(f"{char2.name} sudah mati.")
            inp = input("\nKarakter yang berinteraksi: ")
            continue
        
        if char1.is_alive() and char2.is_alive():
            char2.attack(char1)
            print(f"{char2.name} menyerang {char1.name} sebesar {char2.atk}")
        else:
            if not char1.is_alive():
                print(f"{char1.name} sudah mati.")
            elif not char2.is_alive():
                print(f"{char2.name} sudah mati.")
            inp = input("\nKarakter yang berinteraksi: ")
            continue

        if char1.is_alive() and char2.is_alive():
            char1.elemental_skill(char2)
            char2.elemental_skill(char1)
            
            if type(char1) == type(char2):
                print("Tidak terjadi reaksi elemen")
            else:
                if isinstance(char1, Anemo) or isinstance(char2, Anemo):
                    print("Terjadi reaksi elemen Swirl!")
                    if char1.em > char2.em:
                        damager = char1.name
                        damaged = char2.name
                    elif char2.em > char1.em:
                        damager = char2.name
                        damaged = char1.name

                    if char1.em != char2.em:
                        print(f"{damager} melukai {damaged} sebesar {char1.em + char2.em}!")
                    else:
                        print("Tidak ada yang terluka")
                else:
                    print("Terjadi reaksi elemen Vaporize!")
                    if char1.em > char2.em:
                        damager = char1.name
                        damaged = char2.name
                    elif char2.em > char1.em:
                        damager = char2.name
                        damaged = char1.name

                    if char1.em != char2.em:
                        if isinstance(characters[damager], Pyro):
                            damage = int(1.5 * characters[damager].em)
                        else:
                            damage = 2 * characters[damager].em
                        print(f"{damager} melukai {damaged} sebesar {damage}!")

                    else:
                        print("Tidak ada yang terluka")
        else:
            if not char1.is_alive():
                print(f"{char1.name} sudah mati.")
            elif not char2.is_alive():
                print(f"{char2.name} sudah mati.")
                
        inp = input("\nKarakter yang berinteraksi: ")
    
    ## TODO
    # Cetak semua karakter yang masih hidup dengan Format:
    # [Nama], HP: [HP]
    print("\nKarakter yang masih hidup:")
    print("-"*27)
    print("Nama                | HP")
    print("-"*27)
    for char in characters:
        # Cetak hanya yang masih hidup
        if characters[char].is_alive():
            print(characters[char])

if __name__ == '__main__':
    main()
