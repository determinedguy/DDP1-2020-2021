import random

print("SELAMAT DATANG DI LOVEMETER")

nama_dia = input("Masukkan nama crush kamu: ")

cocok = random.random()
print("Kecocokan anda ", round(cocok*100,2), "%", sep='')
#bisa juga f"{cocok:.2f}"

if cocok > 0.8:
    print("Anda sangat cocok dengan " + nama_dia + "!")
elif 0.5 <= cocok <= 0.8:
    print("Anda lumayan cocok dengan " + nama_dia + "!")
else:
    print("Anda tidak cocok dengan " + nama_dia + " :(")