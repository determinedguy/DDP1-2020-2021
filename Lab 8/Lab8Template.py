class Anemo:
    def __init__(self, name, hp, atk, em):
        ## TODO
        # Lengkapi constructor ini
        self.name = ...
        self.atk = ...
        self.hp = ...
        self.em = ...
    
    
    def attack(self, other):
        ## TODO
        # Implementasikan attack
        pass 
    
    def elemental_skill(self, other):
        ## TODO
        # Implementasikan reaksi elemen
        pass
    
    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        ## TODO
        # Implementasikan cetak
        return
        

class Pyro:
    def __init__(self, name, hp, atk, em):
        ## TODO
        # Lengkapi constructor ini
        self.name = ...
        self.atk = ...
        self.hp = ...
        self.em = ...

    def attack(self, other):
        ## TODO
        # Implementasikan attack
        pass 

    def elemental_skill(self, other):
        ## TODO
        # Implementasikan reaksi elemen
        pass
    
    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        ## TODO
        # Implementasikan cetak
        return


class Hydro:
    def __init__(self, name, hp, atk, em):
        ## TODO
        # Lengkapi constructor ini
        self.name = ...
        self.atk = ...
        self.hp = ...
        self.em = ...

    def attack(self, other):
        ## TODO
        # Implementasikan attack
        pass 

    def elemental_skill(self, other):
        ## TODO
        # Implementasikan reaksi elemen
        pass

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        ## TODO
        # Implementasikan cetak
        return


def main():
    ## TODO
    # Lengkapi implementasi penambahan karakter!
    characters = ...

    while ...:
        name, vision, hp, atk, em = ...
        hp, atk, em = ...
        if vision == 'Anemo':
            ...
        elif vision == 'Pyro':
            ...
        elif vision == 'Hydro':
            ...
        else:
            print(f"[ERROR] {vision}: Vision tidak valid")
        


    # Mencetak interaksi yang dilakukan
    inp = input("\nKarakter yang berinteraksi: ")   
    while inp != "":
        name1, name2 = inp.split()
        char1 = characters.get(name1)
        char2 = characters.get(name2)

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
        ...

if __name__ == '__main__':
    main()
